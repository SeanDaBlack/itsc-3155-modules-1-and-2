

user_input = input("Enter a String: ")
new_string = ''

for i in range(len(user_input)):

    new_string += user_input[len(user_input)-1-i]

print(new_string)
