
user_input = ""
user_list = []
user_even_list = []

while (user_input != "QUIT"):
    user_input = input("Enter an Integer or QUIT to quit: ")
    if user_input.isnumeric():
        user_list.append(int(user_input))

for i in user_list:
    if i % 2 == 0:
        user_even_list.append(i)

print("All nums:", user_list)
print("Even nums:", user_even_list)
