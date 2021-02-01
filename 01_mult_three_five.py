
def multiples(number):
    """Takes in a number and returns the sum
    of all numbers that are multiples of 3 or five"""

    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
