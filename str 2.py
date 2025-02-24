def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)  
        else:
            result += char  
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

text = "Hello World! 123"

print("Original:", text)
print("Lowercase:", to_lowercase(text))
print("Uppercase:", to_uppercase(text))
print("Toggle Case:", toggle_case(text))
