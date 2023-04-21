start = int(input("Enter the starting range for list: "))
end = int(input("Enter the end for list: "))
for num in range(start, end+1):
    if num % 2==0:
        print(num, end=" ")
