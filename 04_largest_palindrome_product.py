def is_palindrome(string):
    return string == string[::-1]


def largest_palindrome(min, max):
    palindrome = 0
    for i in range(min, max):
        for j in range(min, max):
            product = i * j
            if is_palindrome(str(product)):
                if palindrome < product:
                    palindrome = product
    return palindrome


print(largest_palindrome(101, 999))
