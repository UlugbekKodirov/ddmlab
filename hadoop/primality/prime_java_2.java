import java.io.IOException;
 
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
 
 
 
public final class prime_java_2 {
 
	public final static void main(final String[] args) throws Exception {
		final Configuration conf = new Configuration();
 
		final Job job = new Job(conf, "prime_java_2");
		job.setJarByClass(prime_java_2.class);
 
		job.setOutputKeyClass(NullWritable.class);
		job.setOutputValueClass(IntWritable.class);
 
		job.setMapperClass(MapForPrime.class);
 
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
 
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
 
		job.waitForCompletion(true);
	}
 
	public static final class MapForPrime extends Mapper<LongWritable, Text, NullWritable, IntWritable> {
		final NullWritable nw = NullWritable.get();
 
		public final void map(final LongWritable key, final Text value, final Context context)
				throws IOException, InterruptedException {
			final int number = Integer.parseInt(value.toString());
			if(isPrime(number)) {
				context.write(nw, new IntWritable(number));
			}
		}
	}

	private static final boolean isPrime(final int number) {
		if (number == 1) {
			return false;
		}
		if (number % 2 == 0 && number != 2 || number % 3 == 0 && number != 3) {
			return false;
		}
		int limit = (int) ((Math.pow(number, 0.5) + 1) / 6.0 + 1);
		for (int i = 1; i < limit; i++) {
			if(number % (6 * i - 1) == 0){
				return false;
			}
			if(number % (6 * i + 1) == 0){
				return false;
			}
		}
		return true;
	}
}
