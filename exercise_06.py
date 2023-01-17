
user_input1 = int(input("Enter an row from 1 - 5: "))
user_input2 = int(input("Enter an col from 1 - 5: "))

for i in range(1, 6):
    for j in range(1, 6):
        if i == user_input1 and j == user_input2:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("")
