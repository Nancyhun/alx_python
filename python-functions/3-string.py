def reverse_string(string):
    reversed_string = ""
    
    n = len(string)
    for i in range (n-1, -1, -1): #Note that python starts counting from 0 to n-1. Eg cat=> [c-0, a-1, t-2]
        alphabet = string[i]

        reversed_string = reversed_string + alphabet

    return reversed_string

print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))
