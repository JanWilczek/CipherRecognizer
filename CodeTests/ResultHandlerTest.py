from ResultHandler import ResultHandler

rh = ResultHandler(['apples','bananas','oranges'])
rh.add_result([0, 2, 5],'bananas')
rh.add_result([1, 4, 8],'oranges')
rh.add_result([8, 7, 9],'bananas')
rh.add_result([5, 1, 3],'oranges')
rh.add_result([10, 1, 0],'apples')

rh.write_results_to_excel_file("testfile1.xlsx","sheet1")
