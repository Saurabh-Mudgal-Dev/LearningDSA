class StackADT:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data == []:
            return None
        return self.data.pop()
    
    def peek(self):
        if self.data == []:
            return None
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
    def display(self):
        return self.data

def main():
    s = StackADT()
    while True:
        print("enter 1 to add element, 2 to delete, 3 to peek\n4 to check if stack is empty, 5 to find size, 6 to display\n7 to print")
        ch = int(input("enter your choice"))
        if ch == 1:
            ele = int(input("enter element to add to stack"))
            s.push(ele)
        elif ch == 2:
            if len(s.data) == 0:
                print("underflow")
            else:
                print(s.pop())
        elif ch == 3:
            if len(s.data) == 0:
                print("nothing to peek")
            else:
                print(s.peek())
        elif ch == 4:
            if s.is_empty():
                print("stack is empty")
            else:
                print("stack is not empty")
        elif ch == 5:
            print(s.size())
        elif ch == 6:
            print(s.display())
        elif ch == 7:
            break
        else:
            print("please enter valid choice")

if __name__ == "__main__":
    main()