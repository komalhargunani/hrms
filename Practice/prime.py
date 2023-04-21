# num = int(input("enter the number: "))
#
# flag = False
# if num == 1:
#     print("2 is the smallest prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
#     if flag:
#         print("num is not a prime number")
#     else:
#         print("num is prime")


# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# Python program to display all the prime numbers within an interval
