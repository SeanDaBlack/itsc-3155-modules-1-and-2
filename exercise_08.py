
user_list = []
single_list = []

for i in range(1, 11):
    user_list.append(int(input(f"Enter number {i}: ")))

for i in user_list:
    if user_list.count(i) == 1:
        single_list.append(i)


print("Original list:", user_list)
print("Numbers that appear only once:", single_list)
