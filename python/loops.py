#while loop
# i = 0
# while i < 5:
#     print("naman")
#     i += 1

#for loops
# n = "naman"
# for i in n:
#     print(i)

# for x in range(60):
#     if x%6 == 0:
#         print(x)

# n = int(input("enter a number :"))
# m = int(input("enter a number :"))
# i = 1
# while i <= m:
#     print(i*n)
#     i += 1


# n = int(input("enter a number :"))
# for x in range(2, n+1):
#     if n%x == 0:
#         print(x)
#         break

# n = int(input("enter a number :"))
# x = 2
# while x <= n:
#     if n%x == 0:
#         print(x)
#         break
#     x += 1 

# l = [10,15,7,30,55,67]
# for x in l:
#     if x%5 != 0:
#         continue
#     print(x)

# i = 0
# while i < 5:
#     if i == 3:
#         i = i + 1
#         continue
#     print(i, i*i)
#     i += 1

#nested loop
# for i in range(1,11):
#     for j in range(i,i*10+1,i):
#         print(j,end=" ")
#     print()

#pattern of square and rectangle
# n = int(input("enter a row :"))
# m = int(input("enter a col :"))
# for row in range(n):
#     for col in range(m):
#         print("*",end = " ")
#     print()

# #pattern of triangle and pyrmaids
# n = int(input("enter a row :"))
# for row in range(n):
#     for col in range(n-row):
#         print("*",end = " ")
#     print()

# # n = int(input("enter a row :"))
# for row in range(n):
#     for col in range(row+1):
#         print("*",end = " ")
#     print()

# #pyramaid
# # n = int(input("enter a row: "))
# for row in range(n):
#     for col in range(n-row-1):
#         print(" ",end=" ")
#     for k in range(2*row+1):
#         print("*",end=" ")
#     print()

#count
# x = int(input("==>>"))
# res = 0
# while x > 0:
#     x = x//10
#     res = res + 1
# print("count", res)

#factorial
# n = int(input("===>>>"))
# res = 1
# for i in range(2,n+1):
#     res = res * i
# print("factorial",res)