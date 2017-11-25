# Tests whether the classifier correctly sums two integers in range (0,5).
# Can serve as a recipe for ANNClassifier use.

from ANNClassifier import ANNClassifier
from ResultHandler import ResultHandler

# Prepare the data
training_input_data = [
    [0, 1],
    [2, 2],
    [1, 1],
    [2, 1],
    [5, 0],
    [0, 2],
    [1, 0],
    [2, 3],
    [3, 0],
    [0, 5],
    [2, 0],
    [1, 2],
    [3, 1],
    [0, 0],
    [1, 1],
    [2, 1],
    [2, 0],
    [4, 0],
    [4, 1],
    [0, 0],
]

training_output_data = [1, 4, 2, 3, 5, 2, 1, 5, 3, 5, 2, 3, 4, 0, 2, 3, 2, 4, 5, 0]

classifier = ANNClassifier()
classifier.train(training_input_data,training_output_data)

test_data = [
    [2, 3],
    [2, 1],
    [0, 4],
]

results = [5, 3, 4]

result_handler = ResultHandler()

predictions = classifier.predict(test_data)

result_handler.classes_ = classifier.MLPClassifier.classes_
for i,prediction in enumerate(predictions):
    result_handler.add_result(prediction,results[i])

result_handler.write_results_to_excel_file("Sum_result.xls","Sheet 1")