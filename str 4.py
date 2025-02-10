#function that removes one string from another string
def remove_string_from_another(main_str, remove_str):
    
    result = main_str.replace(remove_str, "")
    return result

main_string = input("Enter the main string: ")
string_to_remove = input("Enter the string to remove: ")

updated_string = remove_string_from_another(main_string, string_to_remove)
print(f"Updated string after removal: {updated_string}")
