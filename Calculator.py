def sum_2(): 
    x = int(input("What's x"))
    y = int(input("What's y"))

    print (x+y)


def get_numbers():  
    my_numbers = []
    while True: 
        number = input("What's a number? ")
        # '' is our sentinel value
        if number == '':
            # stop getting numbers
            break

        try:
            my_numbers.append(float(number))
        except:
            print('That is not a valid number, please try again.')


        # L = []
        # L.append(1)
        # print(L) → [1]
        # L.append(2)
        # print(L) → [1, 2]
        
    print(my_numbers)
    return my_numbers


# Trying to get numbers and ask user what they want to do
def calculate (numbers): 
    operator = input("How would you like to calculate? Choose: Mult, Div, Sub, or Sum")
    operator = operator.lower().strip()
    if operator == 'mult':
        return mult(numbers)
    if operator == 'div':
        return div(numbers)
    if operator == 'sum':
        return sum(numbers)
    if operator == 'sub':
        return sub(numbers)
# after getting list, ask user what they would like to do
# print input("How would you like to calculate?")
#*// - +
# For sum, mult, div, sub
def sum(numbers):
    # a + b + c + ...
    sum = 0
    for each in numbers:
        sum = each + sum
    return sum
    
def mult(numbers): 
    # a * b * c * ...
    product = 1
    for each in numbers:
        product = each * product
    return product
def div(numbers):
    # a / b / c / ...
    div = numbers[0]
    for each in numbers[1:]:
        div = div/each
    return div
def sub(numbers): 
    sub = numbers[0]
    for each in numbers [1:]:
        sub = sub - each 
    return sub


# get numbers, calculate, and print out final number
def get_final_result (): 
    print(calculate(get_numbers()))

get_final_result ()