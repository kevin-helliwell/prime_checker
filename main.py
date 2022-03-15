# Checks if a given number is prime
def prime_checker(number):

    list = []
    for i in range(1, 101):
        list.append(i)

    factors = []
    for element in list:
        if number % element == 0:
            factors.append(element)
    print(factors)

    if factors != [1, number]:
        print(f"{number} is not prime")
    else:
        print(f"{number} is prime")


# TEST
import time

start = time.perf_counter()
for i in range(1, 101):
    prime_checker(i)
end = time.perf_counter()
print(f"{(end-start)*1000} ms")
