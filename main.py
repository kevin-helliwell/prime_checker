# Checks if a given number is prime
def prime_checker(number):

    # Generates list of all numbers up to and including given number
    list = []
    for i in range(1, number + 1):
        list.append(i)

    # Generates list of factors for given number
    factors = []
    for element in list:
        if number % element == 0:
            factors.append(element)

    # Checks if not prime
    if factors != [1, number]:
        return False
    # Otherwise, must be prime
    else:
        return True


# Number of primes at a certain number
def number_of_primes(number):
    list = []
    for i in range(1, number + 1):
        if prime_checker(i) == True:
            list.append(i)
    return f"There are {len(list)} prime numbers at {number}. {list}"


# # TEST
# import time

# # Timer start
# start = time.perf_counter()

# # Checks number of total primes at a prime number
# for i in range(1000):
#     if prime_checker(i) == True:
#         print((number_of_primes(i)))

# # Timer end
# end = time.perf_counter()
# print(f"Completed in {(end-start)} seconds")
