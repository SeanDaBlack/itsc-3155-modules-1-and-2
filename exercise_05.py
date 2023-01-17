
user_list1 = []
user_list2 = []
user_list3 = []

for i in range(5):
    user_list1.append(int(input("Enter number for list 1: ")))

for i in range(5):
    user_list2.append(int(input("Enter number for list 2: ")))

for i in range(5):
    if ((user_list1[i] in user_list2) and (user_list1[i] not in user_list3)):
        user_list3.append(user_list1[i])

print("List 1:", user_list1)
print("List 2:", user_list2)
print("Common List:", user_list3)
