


class ResultHandler:
    def __init__(self, classes):
        self.__id = 0
        self.classes_ = classes
        self.__results = []
        self.__separator = ';'

    def add_result(self, prediction_vector, correct_result):
        self.__results.append((correct_result, prediction_vector))

    def write_results_to_file(self, filename):
        # Create a file
        # Write the header (Correct result, classes' names)
        # Write the results
        # Calculate and add error rate to the file
        return 0
