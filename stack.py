def create_stack():
   stack = []
   return stack

def push(stack,a):
    stack.append(a)
    print("Pushed Item : "+ a)

def isempty(stack):
    return len(stack) == 0

def peek(stack):
    return stack[len(stack)-1]

def pop(stack):
    stack.pop(len(stack)-1)
    return stack

stk = create_stack()
push(stk,str(10))
push(stk,str(20))
push(stk,str(30))
print(stk)
print(peek(stk))
print(pop(stk))