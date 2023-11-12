
n = 0

for outer in range(3, 0, -1):
    
    m = 0
    
    for inner in [2,0,2,3]:
        if inner == outer:
            m += 1
        
        n += 1
    
    print(m)

print(n)
