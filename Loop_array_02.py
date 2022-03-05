num_array=[ ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"], ]

for row in num_array:
    for col in row:
        if(col != "5"):
         print(col)
        else:
            #continue
            break # code breaks out only for the second [for] loop.
    print("printed row")