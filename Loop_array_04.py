num_array=[ ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"], ]

for row in num_array:
  for col in row:
    if(col != "7"):
      print(col)
    else:
      pass
  print("printed row")  