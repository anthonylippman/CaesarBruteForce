import collections
import string

def caesar(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase) #Creates class with uppercase alphabet
    lower = collections.deque(string.ascii_lowercase) #Creates class with lowercase alphabet

    upper.rotate(number_to_rotate_by) #Rotate n times
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    lower = ''.join(list(lower))
    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))

def brute():
    start=0
    for number in range(26):
        print("Rot-" + str(start) + "\t" + caesar(input_string,number))
        start+=1

if __name__ == '__main__':
    input_string = input('Enter string:  ')
    brute()
