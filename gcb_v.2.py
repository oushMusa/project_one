def convertFracts(lst):
    ''' make and return new list
    '''    
    print()
    if len(lst) == 0 or lst == None:
        return lst
    else:
        d_list = [item[1] for item in lst]
        divisor = lcm(d_list)        
        lst_1 = [[int(item[0] * divisor / item[1]), int(divisor)] for item in lst]
        return lst_1

def GCD(a, b):
    ''' find greatist common divisor
    '''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a    
    return int(a+b)
    
def lcm(d_lst):
    ''' find least common multiple 
    '''
    b=d_lst[0]   
    for a in d_lst[1:]:  
        d_lcm = a * b / GCD(a, b)
        b = d_lcm        
    return int(d_lcm)
    
b = [[27115, 5262], [87546, 11111111], [43216, 255689]] 
print(convertFracts(b))