user_number = int(input("Enter 5-digit number: "))

first_digit = user_number // 10000
second_digit = (user_number % 10000) // 1000
third_digit = (user_number % 1000) // 100
fourth_digit = (user_number % 100) // 10
fifth_digit = user_number % 10

user_reversed_number = int(str(fifth_digit) + str(fourth_digit) + str(third_digit) + str(second_digit) + str(first_digit))

print("Your number: " + str(user_number))
print("Your reversed number: " + str(user_reversed_number))

