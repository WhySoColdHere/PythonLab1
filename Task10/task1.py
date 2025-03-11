print("Enter strings. For exit, just tap ENTER.")
strings = []
string = "str"
while string != '':
    string = input()
    strings.append(string)
print(sorted(strings[0:-1], key=lambda x: len(x.split())))

