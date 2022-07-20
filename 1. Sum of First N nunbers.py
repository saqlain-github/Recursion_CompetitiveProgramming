def sumN(x):
    if x <= 0 :
        return 0
    return x + sumN(x-1)

def  factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    x= 4
    print(sumN(x))
    print(factorial(5))