class MyString:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, MyString):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        else:
            raise TypeError("Unsupported type for concatenation.")
        return self

    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def __str__(self):
        return self.value

if __name__ == "__main__":
    s1 = MyString("Hello")
    s2 = MyString(" World")

    print("Original s1:", s1)
    print("Original s2:", s2)

    s1 += s2
    print("After Concatenation:", s1)

    s1.toLower()
    print("To Lower Case:", s1)

    s1.toUpper()
    print("To Upper Case:", s1)
