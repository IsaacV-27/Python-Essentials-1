def primos(num):
    
    for m in range (1, num):
        if m+1 >= num:
            return num
            break
        for x in range (1, num):
            if num / m == x:
                return False
                break
        
for i in range(1, 20):
    if primos( i+1 ):
        print(i+1, end= " ")
