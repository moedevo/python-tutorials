#Program to test whether a passed letter is a vowel or no

letter = input("Enter a letter: ").upper()
vowels = ("A", "E", "I", "O", "U")
if letter in vowels:
        print("Your letter is a vowel.")
else:
        print("Your letter is not a vowel.")