
user_input = input("Enter a String: ")
user_list_end = []


while user_input != "":
    user_list_end.append(list(user_input[:3]))
    user_input = user_input[3:]

print(user_list_end)
