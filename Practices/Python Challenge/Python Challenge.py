


'''

Challenge 1

x = 1
a = 38
for i in range(a):
    x = x * 2

print(x)

or print(2**38)

'''


'''

Challenge 2

alphabet = "abcdefghijklmnopqrstuvwxyz"
n_alphabet = "cdefghijklmnopqrstuvwxyzab"


string = input("String? ")
new_string = ""

for letter in string:
    if letter in alphabet:
        index_of_letter = alphabet.find(letter)
        new_string += n_alphabet[index_of_letter]
    else:
        new_string += letter
print(new_string)

tab = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print(string.translate(tab))

'''


new_string = ""

the_code = open("the code.txt", "r")

for letter in the_code.read():
    if letter in "!@#$%^&*()_+[]{}\n":
        new_string += ""
    else:
        new_string += letter
print(new_string)


