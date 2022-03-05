num_array=[ ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"], ]

for row in num_array:
    for col in row:
        if(col != "4"):
         print(col)
        else:
         print("lucky seven found!")
         continue # code continues to execute.
    print("printed row")