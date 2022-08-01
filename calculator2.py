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
# from Calculator import get_numbers 
    #  code reuse

        # L = []
        # L.append(1)
        # print(L) → [1]
        # L.append(2)
        # print(L) → [1, 2]
        
    print(my_numbers)
    return my_numbers

def sum_operator(numbers):
    # a + b + c + ...
    sum = 0
    for each in numbers:
        sum = each + sum
    return sum
    
def mult_operator(numbers): 
    # a * b * c * ...
    product = 1
    for each in numbers:
        product = each * product
    return product

def div_operator(numbers):
    # a / b / c / ...
    div = numbers[0]
    for each in numbers[1:]:
        div = div/each
    return div

def sub_operator(numbers): 
    sub = numbers[0]
    for each in numbers [1:]:
        sub = sub - each 
    return sub

my_list = [10, 1]
my_list[0]
dictionary = dict(mult=10, div=1)
dictionary = {'mult': 10, 'div': 1}
dictionary['mult']

# Trying to get numbers and ask user what they want to do
def calculate (numbers): 
    while True:
        operator = input("How would you like to calculate? Choose: Mult, Div, Sub, or Sum")
        operator = operator.lower().strip()
        calculator_operator = {'mult': mult_operator, 'div': div_operator, 'sum': sum_operator, 'sub': sub_operator}
        try:
            return calculator_operator[operator](numbers) 
        except KeyError:
            print('Try again')


    '''
    if operator == 'mult':
        return mult(numbers)
    if operator == 'div':
        return div(numbers)
    if operator == 'sum':
        return sum(numbers)
    if operator == 'sub':
        return sub(numbers)
    '''







# get numbers, calculate, and print out final number
def get_final_result (): 
    print(calculate(get_numbers()))

get_final_result ()
 




