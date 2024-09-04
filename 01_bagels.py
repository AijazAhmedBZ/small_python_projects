






import random

num_digits = 3
max_guesses = 10


def main():
    
    
    
    print("""I am thinking of a three digit number. Try to guess what it is
            Here are some clues:
            When I say:     That means:
            Pico            One digit is correct but in the wrong position.
            Fermi           One digit is correct and in the right position.
            Bagels          No digit is correct.
            I have thought up a number.
            You have 10 guesses to get it.""").__format__(max_guesses)
