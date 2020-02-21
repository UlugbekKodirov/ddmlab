# spark-submit --master spark://group4m1.dyn.mwn.de:7077 --executor-memory 6g --executor-cores 4 decision_tree.py
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Decision Tree Classification Example.
"""
from __future__ import print_function

from pyspark import SparkContext
# $example on$
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
from pyspark.sql import SparkSession
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.mllib.regression import LabeledPoint
# $example off$

spark = SparkSession \
     .builder \
     .appName("Protein Decision Tree") \
     .getOrCreate()



def getPredictionsLabels(model, test_data):
   predictions = model.predict(test_data.map(lambda r: r.features))
   return predictions.zip(test_data.map(lambda r: r.label))
def printMetrics(predictions_and_labels, output_file):
   metrics = MulticlassMetrics(predictions_and_labels)
   output_file.write('Precision of True '+str(metrics.precision(1))+'\n')
   output_file.write('Precision of False' + str(metrics.precision(0))+'\n')
   output_file.write('Recall of True  '+str(metrics.recall(1))+'\n')
   output_file.write('Recall of False   '+str(metrics.recall(0))+'\n')
   output_file.write('F-1 Score         '+str(metrics.fMeasure())+'\n')
   output_file.write('Confusion Matrix\n'+str(metrics.confusionMatrix().toArray())+'\n')

   print('Precision of True '+str(metrics.precision(1)))
   print('Precision of False'+str(metrics.precision(0)))
   print('Recall of True  '+str(metrics.recall(1)))
   print('Recall of False   '+str(metrics.recall(0)))
   print('F-1 Score         '+str(metrics.fMeasure()))
   print('Confusion Matrix\n'+str(metrics.confusionMatrix().toArray()))


if __name__ == "__main__":
    # load our vectorized dataset as dataframe
    sdf = spark.read.csv('./transmembrane/vecProteinLabel_ratio_1to1_top250_4mers.csv', header=True, inferSchema=True, enforceSchema=False)
    datas = sdf.rdd.map(lambda x: LabeledPoint(x[0], x[1:]))
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = datas.randomSplit([0.7, 0.3])
    # train a DecisionTree model.

    for maxDepth in range(25, 26):
        #maxDepth = 5
        maxBins = 200
        impurity = 'gini'
        model = DecisionTree.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={}, impurity=impurity,
                                             maxDepth=maxDepth,
                                             maxBins=maxBins)
    # evaluation of the model
        output_name = "decision_tree" + str(maxDepth) + "_" + str(maxBins) + "_" + impurity + '_ratio_1_1_top250_4mers'
        output_file = open("/mnt/"+output_name, "w")

        predictions_and_labels = getPredictionsLabels(model, testData)
        printMetrics(predictions_and_labels, output_file)
