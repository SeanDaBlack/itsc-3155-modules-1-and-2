
user_input = int(input("Enter an Integer: "))
user_list = []
user_total = 0


for i in range(user_input):
    user_num = float(input(f"Enter number {i+1}: "))
    user_list.append(user_num)
    user_total += user_num


print("List:", user_list)
print("Average:", user_total/user_input)
