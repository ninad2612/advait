def infix_to_postfix(expression):
  
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    
    stack = []
    postfix = []

    
    temp_count = 0
    def new_temp():
        nonlocal temp_count
        temp_count += 1
        return f't{temp_count}'

    
    for char in expression:
        
        if char.isalnum():
            postfix.append(char)
        
        
        elif char == '(':
            stack.append(char)
        
        
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  
        
        
        else:
            
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char) 
    
    
    while stack:
        postfix.append(stack.pop())
    
    
    postfix_expression = ''.join(postfix)
    
    return postfix_expression

def postfix_to_three_address(postfix_expression):
    stack = []
    three_address_code = []

    temp_count = 0
    def new_temp():
        nonlocal temp_count
        temp_count += 1
        return f't{temp_count}'
    

    for char in postfix_expression:
        if char.isalnum():
            stack.append(char)
        else:
            op = char
            temp1 = stack.pop()
            temp2 = stack.pop()
            result_temp = new_temp()
            three_address_code.append((op, temp2, temp1, result_temp))
            stack.append(result_temp)
    
    return three_address_code


expression = input("Enter the infix expression: ")
postfix_expression = infix_to_postfix(expression)
print("Postfix expression:", postfix_expression)

three_address_code = postfix_to_three_address(postfix_expression)
print("Three-address code:")
for op, temp1, temp2, result_temp in three_address_code:
    print(f"{result_temp} = {temp2} {op} {temp1}")
