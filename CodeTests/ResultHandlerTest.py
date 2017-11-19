from ResultHandler import ResultHandler

rh = ResultHandler(['apples','bananas','oranges'])
rh.add_result([0, 2, 5],4)
rh.add_result([1, 4, 8],0)
rh.add_result([8, 7, 9],7)
rh.add_result([5, 1, 3],5)

rh.write_results_to_excel_file("testfile1.xlsx","sheet1")
