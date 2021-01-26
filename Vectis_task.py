import math
import time


def prime_validation(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x > 2 and x % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(x))
    for i in range(3, 1 + max_div, 2):
        if x % i == 0:
            return False
    return True


def largest_prime_factor(n):
    prime_factor = 1
    i = 2
    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = n
    return int(prime_factor)


start_time = time.time()
prime_count = 0
number_count = 2
prime_sum = 0
first_prime = 100003
while prime_count != first_prime:
    is_prime = prime_validation(number_count)
    if is_prime:
        prime_count += is_prime
        prime_sum += number_count
    number_count += 1
print(f"Sum of first {first_prime} prime numbers:", prime_sum)
new_value_1 = str(prime_sum)[-3:]
print("Three Right most digits:", new_value_1)
final_value = largest_prime_factor(int(new_value_1))
print(f"largest Prime Factor of {new_value_1}:", final_value)
end_time = time.time()
print("Time required :", end_time - start_time)
print("*"*25)
print(f"{final_value}@vectis.ai")
print("*"*25)