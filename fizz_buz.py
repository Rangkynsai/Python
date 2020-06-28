#fizz_buzz
def fizz_buzz(integer_input):
	if integer_input % 3 == 0 and integer_input % 5 == 0:
		return "FizzBuzz"
	elif integer_input % 3 == 0:
		return "Fizz"
	elif integer_input % 5 == 0:
		return "Buzz"
	else:
		return integer_input
n = int(input())
print(fizz_buzz(n))
