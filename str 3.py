#checking whther one string is there in another or not
def check_substring(str1, str2):
   
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if check_substring(string1, string2):
    print("One string is present in the other.")
else:
    print("Neither string is present") 
