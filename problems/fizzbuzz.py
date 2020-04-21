# Numbers divisible by 3 are replaced with 'Fizz'
# Numbers divisible by 5 are replaced with 'Buzz'
# Numbers divisible by 15 are replaced with 'FizzBuzz'

# Print first 100 FizzBuzz numbers (1-100)

def fizzbuzz():
    for n in range(1, 101):
        response = ""
        if n % 3 == 0:
            response += "Fizz"
        if n % 5 == 0:
            response += "Buzz"
        print(response or n)

# fizzbuzz()

for n in range(1, 101):print('Fizz'[n%3*4:]+'Buzz'[n%5*4:]or n)
