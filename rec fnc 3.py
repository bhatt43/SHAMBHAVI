#recursion fnc 3
def count_vowels(s,index=0):
    vowels="aeiouAEIOU"
    if index == len(s):
        return 0
    return (1 if s[index] in vowels else 0) + count_vowels(s, index+1)

string=input("Ener the string:")
vowel_count=count_vowels(string)
print("Number of vowels:", vowel_count)
