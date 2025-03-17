#Revrse a String

def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))


#slicing method

string=input("Enter the string")
revrsed_string=string[::-1]
print("The Revrsed String is", revrsed_string)

#using a loop

string=input("Enter a string:")
reversed_string=""
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)