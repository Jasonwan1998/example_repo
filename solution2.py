# get the number of input line
line = input()

# create list
input_list = []

# insert element into list
for x in range(line):
    input_list.append(input().split())


allValid = True
errorCodes = True
errorCodes = []

# do checking
for record in input_list:
    allValid = record[1]
    if record[1] is not True:
        errorCode.append(record[2])
    
if allValid is True:
    print("Yes")

else:
    print("No")
    errorCode.append(record[2])