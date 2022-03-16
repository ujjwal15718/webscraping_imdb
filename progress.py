 
# def fibo(n):
#    if n==1:
#        return 0
#    elif n==2:
#        return 1
#    else:
#        return((fibo(n-1)+fibo((n-2))))
# n=int(input("enter the number that you want"))
# for i in range(1,n+1):
#    print(fibo(i))
 
# -----------------------------------------------------------------------
 
# from math import factorial 
# n = int(input("enter"))
# for i in range(n):
#     for j in range(n-i+1):
#         print(end=" ")
#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#     print()


# n=int(input("enter - "))
# for i in range(n):
#     for j in range(n-i+1):
#         print(end=" ")
#     for j in range(i+1):
#         print( i)

# pattern pascal------------------------------
# n=10
# for i in range(1, n+1): 
#     for j in range(n-i+1):
#         print(' ', end='')
#         # print(j)
#     a = 1
#     for j in range(1, i+1):
#         print(' ', a, sep='', end='')
#         a = a * (i - j) // j
#     print()


# num = int(input("Enter the number of rows:"))
  
# for n in range(num):
#     print(' '*(num-n), end='')

#     print(' '.join(map(str, str(11**n))))

# def fact(num):
#   f = 1
#   for i in range(1, num+1):
#     f = f*i
#   return f

# for i in range(5):
#   for col in range(4, i, -1):
#     print(end=" ")
#   for col in range(i+1):
#     val = int(fact(i)/(fact(col)*fact(i-col)))
#     print(val, end=" ")
#   print()





# a=20
# for i in range(a):
#     x=a//2
#     if i <=x:
#         print(i,end="")
# print()
# for i in range(a):
#     if i>x:
#         print(i,end="")








# def rec_range(n):
#     """takes a natural number n and returns a tuple of numbers starting with 0     and ending before n

 

 

# ----------------------------------

def Fibonacci( pos ):
        #check for the terminating condition
        if pos <= 1 :
                #Return the value for position 1, here it is 0
                return 0
        if pos == 2:
                #return the value for position 2, here it is 1
                return 1
 
        #perform some operation with the arguments
        #Calculate the (n-1)th number by calling the function itself
        n_1 = Fibonacci( pos-1 )
         
 
        #calculation  the (n-2)th number by calling the function itself again
#         n_2 = Fibonacci( pos-2 )
        
#         #calculate the fibo number
#         n = n_1 + n_2
 
#         #return the fibo number
#         return n
# num=int(input("enter - "))
# print(Fibonacci(num))

 






# # By recursion
# def fib(n):
#     if n == 1 or n == 2:
#         return 1 
#     else:
#         return(fib(n-1) + fib(n-2))
        
# n = 6
# for i in range(1,n+1):
#     print(fib(i))

# def rec_range(n):
#     if not n <= 1: return rec_range(n-1) + (n-1,)
#     return (0,)





# ----------------------------------------


# reverse snake pattern--------------------------------------------------------------------------
 






 
 