##TASK 1 

def decimal_to_binary(decimal):
    if decimal == 0:
        return ''
    else:
        return decimal_to_binary(decimal // 2) + str(decimal % 2 )
    
print(decimal_to_binary(7))
