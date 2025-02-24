class Queue:
    def _init_(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if not self.is_empty():
            print(f"Dequeued item: {self.queue.pop(0)}")
        else:
            print("Queue is empty. Nothing to dequeue.")

    def peek(self):
        if not self.is_empty():
            print(f"Front item: {self.queue[0]}")
        else:
            print("Queue is empty.")

    def display(self):
        if not self.is_empty():
            print("Queue elements:", self.queue)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue (Insert)")
    print("2. Dequeue (Remove)")
    print("3. Peek (Front Element)")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        queue.peek()
    elif choice == '4':
        queue.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
