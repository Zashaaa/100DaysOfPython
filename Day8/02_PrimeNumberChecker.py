# Write your code below this line ๐
def prime_checker(number):
    if 3 >= number >= 0:
        print("It's a prime number.")
    elif number % 2 == 0 or number % 3 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
