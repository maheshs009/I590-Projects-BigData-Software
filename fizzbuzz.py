def fizzbuzz(n):
    if n % 2 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    elif n % 2 == 0:
        return 'Fizz'
    elif n % 3 == 0:
        return 'Buzz'
    else:
        return str(n)

def main():
    k = input("Enter a number: ")
    for n in range(1, k+1):
        j = fizzbuzz(n)
        print j

main()
