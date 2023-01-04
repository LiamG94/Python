a = "would you like breakfast?"
print("Good morning, John " + a)

a = 5
b = 12
print("Good morning, John. For breakfast, would you like {}?".format("fruit"))
print("We have {} apples, {} bananas and a total of {} pieces available.".format(a, b, a+b))

a = "Good"
b = "John"
c = "morning"
print("{third} {second}, {first}.".format(first=b, second=c, third=a))

number = 12345
divisor = 333
result = number/divisor
print("Result of {} divided by {} is {}".format(number, divisor, result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=result))

print(f"Result of {number} divided by {divisor} is {result}")

print("Good morning, John.\nWould you like breakfast?")

a = "Good morning, John.\nWould you like breakfast?"
print(len(a))

my_string = "Almost finished now folks!"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original: {my_string}")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")

print("Good morning, John.")
print("Breakfast?")

print("Good morning, John.", end = " ")
print("Breakfast?")

print("Good morning, John.\nWould you like breakfast?", )