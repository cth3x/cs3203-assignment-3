def list_sum(list):
    total = 0
    for num in list:
        total += num
    return total

def list_product(list):
    total = 1
    for num in list:
        result *= num
    return total

def main():
    user_input = input("Enter a list of numbers separated by commas: ")
    
    list = [int(x) for x in user_input.split(',')]

    sum = list_sum(list)
    print("The sum is:", sum)

    product = list_product(list)
    print("The product is:", product)
