class Stack:
    def _init_(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed onto the stack.")

    def pop(self):
        if not self.is_empty():
            print(f"Popped item: {self.stack.pop()}")
        else:
            print("Stack is empty. Nothing to pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top item: {self.stack[-1]}")
        else:
            print("Stack is empty.")

    def display(self):
        if not self.is_empty():
            print("Stack elements:", self.stack[::-1])  # Display from top to bottom
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

# Menu-driven program
stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to push: ")
        stack.push(item)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
