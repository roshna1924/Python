# Write a program that returns every other char of a given string starting with first using a function

'''
def string_alternative(str):
    str.split()
    return str[::2]
'''

def string_alternative(str):
    b=""
    for i in range(len(str)):
        if (i % 2) == 0:
         b += str[i]
    return b

if __name__ == '__main__':
    str = input("Enter String: ")
    print(string_alternative(str))
