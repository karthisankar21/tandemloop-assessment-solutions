a = int(input("enter a number: "))

for i in range(1, a+1):
    
    if i % 2 != 0:
        row = [2*n - 1 for n in range(1, i+1)]
    else:  
        row = [2*n - 1 for n in range(1, i)]
    print(f"{i}) input a = {i}, then output :", *row)


