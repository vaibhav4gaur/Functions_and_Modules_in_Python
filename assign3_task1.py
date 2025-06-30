
n = int(input("Enter a number: "))

def fact(n):

    if n == 0:

        return 1

    else :

        output = 1

        for i in range(1,n+1):

          output *= i

        return output

fact_num = fact(n)

print(f"Factorial  of {n} is : {fact_num}")