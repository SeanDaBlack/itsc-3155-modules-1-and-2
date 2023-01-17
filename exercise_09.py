
user_list = []
string = ''

for i in range(5):
    user_list.append(input("Enter a word: "))

for i in user_list:
    string += i + " "

print("Words:", user_list)
print("String:", string)
