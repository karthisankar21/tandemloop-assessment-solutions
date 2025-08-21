a = int(input("enter a number: "))

for i in range(1, a+1):       
    num = 1
    print(f"{i}) input a = {i}, then output :", end= ' ')
    for j in range(1, i+1):
        print(num, end=" ")
        num += 2
    print()

