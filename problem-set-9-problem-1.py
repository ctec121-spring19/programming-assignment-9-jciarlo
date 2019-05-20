# Module 6 - Problem Set No. 9 - Problem 1

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that gets a string containing the person's first, middle and 
last names using input(), and then displays their first, middle and last 
initials. For example, the user enters "Bruce Lawrence Elgort", the program 
should display B.L.E. It must display exactly like this with the .'s after 
each letter with no spaces.

IPO
==========
INPUTS: users full name
PROCESSES: use of variables and the split() method to get the intials of each name 
OUTPUTS: users name in initial format 

"""

def main():

    # get input from user

    phrase = input("Enter your full name please: ")
    # initialize variable to an empty string

    initial1 = " "
    # split the sentence into a list of words
    # use a loop to iterate through the list of words

    for word in phrase.split():
        # concatenate the current value of acronym with the first
        # letter from the current word being iterated
        initial1 = initial1 + word[0]

    # convert the entire acroynum string to upper case
    initial1 = initial1.upper()
   
    # display the acroynum
    print("The intials are:",initial1[1],".",initial1[2],".",initial1[3],".")

main()
