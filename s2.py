#Given a Python List [10,501,22,37,100,999,87,351] your task is to Count all the Prime Numbers and 
#create a new Python List which willcontain all the Prime Numbers in it?
def count_primes_in_list(numbers):
    primes = []

    for num in numbers:
        if num == 2:
            primes.append(num)
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print (num)
                primes.append(num)

    return len(primes)
z = [10,501,22,37,100,999,87,351]
print (count_primes_in_list(z))