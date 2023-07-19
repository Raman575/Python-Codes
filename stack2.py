from Stack import ScreenInterface, stack

def main():
    interface1 = ScreenInterface(title="App home page")
    interface2 = ScreenInterface(title="Product 1 page")
    interface3 = ScreenInterface(title="Product 2 page")
    interface4 = ScreenInterface(title="Product 3 page")
    interface5 = ScreenInterface(title="Product 4 page")
    interface6 = ScreenInterface(title="Product 5 page")
                
    
    
    Stack = stack()
    Stack.push(interface1)
    Stack.push(interface2)
    Stack.push(interface3)
    Stack.push(interface4)
    Stack.push(interface5)
    Stack.push(interface6)
    
    
    Stack.pop()
    Stack.pop()
    Stack.pop()
    Stack.pop()
    
    Stack.iterate()
    print("Stack:", vars(Stack))

if __name__ == "__main__":
    main()