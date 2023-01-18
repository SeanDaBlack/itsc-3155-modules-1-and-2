lower_string = ''
upper_string = ''

user_input = input("Enter a String: ")

for i in user_input.replace(" ", ""):

    if i.isupper():
        upper_string += i
    else:
        lower_string += i

new_string = lower_string + upper_string

print(new_string)
