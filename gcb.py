import numpy as np

def GCD(d_list):    
    ''' looking for greatest common divisor
    '''
    divisor_list = []
    for item in d_list:
        divisor = 2
        divisor_item = []          # factorisation of item
        while True:
            if item % divisor == 0 and divisor <= item:
                divisor_item.append(divisor)
                item = item // divisor                
            elif divisor > max(d_list):
                divisor_list.append(divisor_item)                
                break
            else:
                divisor += 1    
    divisor_list.sort(key=lambda item: len(item))    
    divisor = 1
    for item in divisor_list[0]:
        if all([item in check for check in divisor_list[1:len(divisor_list)]]):
            divisor *= item            
            for check in divisor_list[1:len(divisor_list)]:
                check.remove(item)    
    return divisor
            
              
def convertFracts(lst):
    if len(lst) == 0 or lst == None:
        return lst
    else:
        d_list = [item[1] for item in lst]        
        multiplication = np.prod(d_list)                    
        gcd = GCD(d_list)
        lcm = multiplication / gcd
        print(multiplication, gcd, lcm)
        lst_1 = [[item[0] * lcm / item[1], lcm] for item in lst]
        print(lst_1)
        return lst_1
    
a = [[1, 8], [1, 9], [1, 21]]
print(convertFracts(a))