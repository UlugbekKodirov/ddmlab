for i in {3..10}
  do
    python3 benchmarking.py --kmers $i --steps 10000
  done
