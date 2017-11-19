import xlwt


class ResultHandler:
    def __init__(self, classes):
        self.__id = 0
        self.classes_ = classes
        self.__results = []
        self.__separator = ';'

    def add_result(self, prediction_vector, correct_result):
        self.__results.append((correct_result, prediction_vector))

    def write_results_to_excel_file(self, filename, sheet):
        # Create a file
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)
        # Write the header (Correct result, classes' names)
        header = ['Lp.', 'Correct result']
        for class_ in self.classes_:
            header.append(class_)

        for n,column_title in enumerate(header):
            sh.write(0,n,column_title)

        # Write the results
        for i in range (1,len(self.__results) + 1):
            sh.write(i,0,i)
            result = self.__results[i-1]
            sh.write(i,1,result[0])
            for j in range (2,len(result[1]) + 2):
                sh.write(i,j,result[1][j-2])

        # Calculate and add error rate to the file - optional
        # Save the file
        if (filename.endswith('.xlsx')):
            filename = filename[:len(filename)-1]
        if not (filename.endswith('.xls')):
            filename += '.xls'

        book.save(filename)

