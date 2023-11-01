def evaluate(exp):
    stack = []
    for i in exp:
        if i in ['+','-']:
            num_2 = stack.pop()
            num_1 = stack.pop()
            if i == "+":
                stack.append(num_1 + num_2)
            elif i == "-":
                stack.append(num_1 - num_2)
        else:
            stack.append(int(i))
    return stack.pop()
            
        
