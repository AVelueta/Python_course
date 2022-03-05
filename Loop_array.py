##[FOR] nested loop ##

from itertools import count
from operator import index
from typing import Iterator


num_array=[ ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"], ]

count = 1
for row in num_array:
        print("The following numbers belong to row number: ", count )
        print(row)
        count = count+1

#        print(col)
#    print("printed row")
