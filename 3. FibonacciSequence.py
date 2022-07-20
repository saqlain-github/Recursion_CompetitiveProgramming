#time complexity O()
def fibonacci(n):
    if n <= 1:  return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    n = 6
    print(fibonacci(n))