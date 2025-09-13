#  Pyramid Pattern
#         * 
#        *** 
#       ***** 
#      ******* 
#     ********* 
#    *********** 


def pyramid(rows):
    for i in range(1, rows+1):
        for j in range(rows-i):
            print("_",end="")

        for k in range(1,2*i):
            print("*",end="")

        print()

pyramid(5)