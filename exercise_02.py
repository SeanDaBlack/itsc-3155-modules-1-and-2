

user_input1 = input("Enter a String: ")
user_input2 = input("Enter another String: ")

if user_input1.endswith(user_input2) or user_input2.endswith(user_input1):
    print(True)
else:
    print(False)
