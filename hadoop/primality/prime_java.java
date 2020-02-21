import java.io.IOException;

import java.lang.Math;

import org.apache.hadoop.conf.Configuration;

import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.IntWritable;

import org.apache.hadoop.io.LongWritable;

import org.apache.hadoop.io.NullWritable;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;

import org.apache.hadoop.mapreduce.Mapper;

import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;

import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import org.apache.hadoop.util.GenericOptionsParser;


public class prime_java {

public static void main(String [] args) throws Exception{

	Configuration c=new Configuration();

	String[] files=new GenericOptionsParser(c,args).getRemainingArgs();

	Path input=new Path(files[0]);

	Path output=new Path(files[1]);

	Job j=new Job(c,"prime_java");

	j.setJarByClass(prime_java.class);

	j.setMapperClass(MapForPrime.class);

	j.setReducerClass(ReduceForPrime.class);

	j.setOutputKeyClass(Text.class);

	j.setOutputValueClass(IntWritable.class);

	FileInputFormat.addInputPath(j, input);

	FileOutputFormat.setOutputPath(j, output);


	System.exit(j.waitForCompletion(true)?0:1);

}

public static class MapForPrime extends Mapper<LongWritable, Text, Text, IntWritable>{
	IntWritable nw = IntWritable.get();

	private static final boolean getPrime(final long number) {
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


        public final void map(final LongWritable key, final Text value, final Context context)
                throws IOException, InterruptedException {
            final long number = Long.parseLong(value.toString());
            if(getPrime(number)) {
                context.write(nw, new IntWritable());
            }
        }
}

public static class ReduceForPrime extends Reducer<Text, IntWritable, Text, IntWritable>{

	@Override
        public void reduce(Text prime, Iterable<IntWritable> list, Context context) throws IOException, InterruptedException {
            int count = 0;
            for (IntWritable item : list) {
                count++;
            }
            context.write(prime, new IntWritable(count));
        }
}

}
