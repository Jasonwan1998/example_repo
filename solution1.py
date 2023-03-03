# get input from users
T_num = input()
T_list = input().split()
req_num = input()
req_list = input().split()

# check the request number <= stock number
if (T_num > req_num):
    print("No")
    exit()

# check whether T-shirt fulfil the requirement
for x in T_list:
    for a in req_list:
        if x != a[-1]:
            print("No")
            exit()

print("Yes")
        





