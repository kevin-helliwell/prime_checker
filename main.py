import time


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_odd(number: int) -> bool:
    return number % 2 != 0


def is_prime(number: int) -> bool:
    element = 3
    count = 0
    if is_even(number):
        return False
    if is_odd(number):
        while element <= number:
            if number % element == 0:
                count += 1
            if count > 1:
                return False
            element += 2
        return True


def count_primes(number: int) -> int:
    count = 0
    index = 1
    while index <= number:
        if is_prime(index):
            count += 1
        index += 2
    return count


if __name__ == "__main__":
    testNumbers = (10_000, 25_000, 50_000, 75_000, 100_000)

    index = 0
    totalTime = 0
    while index < len(testNumbers):
        testNumber = testNumbers[index]
        start = time.perf_counter()

        numPrimes = count_primes(testNumber)
        end = time.perf_counter()

        elapsed = (end - start).__round__(2)
        totalTime += elapsed

        print(f"There are {numPrimes} primes up to {testNumber} - Completed in {elapsed}s")
        index += 1
    print(f"Total time - Completed in {totalTime.__round__(2)}s")
