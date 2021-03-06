import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = 50
    start_time = time.time()
    t = fibonacci(n)
    elapsed_time = time.time() - start_time
    print(elapsed_time, ' seconds')

if __name__ == '__main__':
    main()
