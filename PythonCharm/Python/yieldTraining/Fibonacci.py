def fibo(n):
    num1,cntr = 0,0
    num2 = 1

    while cntr < n:
        print(num1)
        yield num1

        temp = num1 + num2
        num1 = num2
        num2 = temp
        cntr += 1

fib_object = fibo(10)
print(list(fib_object))
