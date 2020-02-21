for i in {8..9}
  do
    spark-submit --master spark://group4m1.dyn.mwn.de:7077  --class compression --executor-memory 8g --executor-cores 5 --num-executors 5 kmers_without_repartition.py --kmers $i --input uniref90_preprocessed.fasta --output kmer${i}_numexecutors5_classcompression &
  done

