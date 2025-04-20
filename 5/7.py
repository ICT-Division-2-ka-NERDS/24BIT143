stack = []

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter element to push: "))
        stack.append(element)
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", stack.pop())
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
