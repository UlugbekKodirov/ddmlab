object protein_scala{
        def main(args: Array[String]){
            import org.apache.spark.sql.Dataset
            import org.apache.spark.sql.Row
            import org.apache.spark.sql.SparkSession
            import org.apache.spark.sql.functions._
            val spark = SparkSession.builder.getOrCreate()
            import spark.implicits._
            def generate_ngram(seq_str : String, pattern_length: Byte) : Array[Long] = {
                val seq = seq_str.split("")
                val term_len = pattern_length - 1
                var serialized_ngram = new Array[Long](seq.length-term_len)
                var i = 0
                for (i <- 0 until seq.length - term_len) {
                    serialized_ngram(i) = 0
                    var j = 0
                    for (j <- 0 until pattern_length) {
                        serialized_ngram(i) = serialized_ngram(i) << 5
                        serialized_ngram(i) += (seq(i+j)(0).toLong-64)
                    }
                }                
                return serialized_ngram
            }
            def decode_ngram(serial : Long) : String = {
                var i = 0
                var seq = ""
                while (((serial >> i) & 31L)!= 0){
                    seq = (((serial >> i) & 31L)+64).toChar.toString + seq;
                    i+=5;
                }
                return seq
            }
            import org.apache.spark.sql.functions.udf
            val generate_ngramUDF = udf(generate_ngram _) 
            val decode_ngramUDF = udf(decode_ngram _)
            val nmer = args(0)      
            val uniref = spark.read.csv("/uniref90_pro3.fasta")
            val uniref_serialized = uniref.select(explode(generate_ngramUDF($"_c0", lit(nmer))).as("serial"))
            val uniref_count = uniref_serialized.groupBy($"serial").agg(count(lit(1)).as("count"))
            val uniref_deserialized = uniref_count.withColumn("n-mer", decode_ngramUDF($"serial"))
            import java.util.Calendar
            uniref_deserialized.coalesce(1).write.csv("output/protein/uniref"+Calendar.getInstance().getTimeInMillis)
         }
     }
