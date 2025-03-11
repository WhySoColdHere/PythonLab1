print("Enter strings. For exit, just tap ENTER.")
strings = []
string = "str"
while string != '':
    string = input()
    strings.append(string)
strings = strings[0:-1]
print(sorted(strings, key=lambda x: len(x)))
