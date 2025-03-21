def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
num = int(input("Enter a Number:"))
if is_prime(num):
    print(f" {num} is a prime Number.")
else:
    print(f"{num} is not a prime Number")