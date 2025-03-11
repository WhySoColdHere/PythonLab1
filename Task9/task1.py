from common_funcs import list_of_strings_input
print("Enter strings. For exit, just tap ENTER.")
print(sorted(list_of_strings_input(), key=lambda x: len(x)))
