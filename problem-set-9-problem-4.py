# Module 6 - Problem Set No. 9 - Problem 4

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Morse code is a code where each letter of the English alphabet, each digit, 
and various punctuation characters are represented by a series of dots and 
dashes. The table in the morse-code.png image that is part of this repository 
shows part of the morse code conversions. Write a program that asks the user 
to enter a string, and then converts that string to Morse code.

HINTS
========================
- Use a loop to iterate through the inputted string going one letter a time.
- Use the statement below in your code. Each element in the list represents a 
  charecter from the sample Morse code chart provided in the problem. The 
  first element in the list is a space.
- So the letter 'A' or 'a' is in the list at position 13 and would be 
  morse_list[13].
- Use the string accumator pattern to concatenate all of the morese code 
  values together and display them at the end.
- There other ways to approach this problem.
- Solutions from the internet will not be accepted and a grade of zero for the 
  entire assignment will be entered

Annotated list - split over multiple lines - feel free to update as necessary

                  #     ,         .         0       1        2        3
morse_list = [' ', '--..--', '.-.-.-', '-----','.----', '..---', '...--',
                #4        5        6        7        8        9
                '....-', '.....', '-....', '--...', '---..', '----.',
                #A     B       C       D      E    F       G      H   
                '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
                #I     J       K      L       M     N     O      P
                '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
                #Q       R      S      T    U      V       W      X
                '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                #Y       Z
                '-.--', '--..']
IPO
==========
INPUTS: a sentence from the user
PROCESSES: using the morse list, and the dictionary I'm going to be assigning character to numbers using a loop
OUTPUTS: users name in morse code 

"""

def main():
    #morse code to english 
                #     ,         .         0       1        2        3
    morse_list = [' ', '--..--', '.-.-.-', '-----','.----', '..---', '...--',
                #4        5        6        7        8        9
                '....-', '.....', '-....', '--...', '---..', '----.',
                #A     B       C       D      E    F       G      H   
                '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
                #I     J       K      L       M     N     O      P
                '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
                #Q       R      S      T    U      V       W      X
                '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                #Y       Z
                '-.--', '--..']
    #character dictionary 
    char_dict = {' ':'0',',':'1','.':'2','0':'3','1':'4','2':'5','3':'6','4':'7','5':'8','6':'9','7':'10','8':'11','9':'12',
                    'A':'13','B':'14','C':'15','D':'16','E':'17','F':'18','G':'19','H':'20','I':'21','J':'22','K':'23','L':'24','M':'25',
                    'N':'26','O':'27','P':'28','Q':'29','R':'30','S':'31','T':'32','U':'33','V':'34','W':'35','X':'36','Y':'37','Z':'38'}
    str1 = list(input("Enter a sentence: "))
    #for loop 
    for i in range(0, len(str1)):
        char = str1[i]
        charNum = char_dict[char.upper()]
        morse = morse_list[int(charNum)]
        print(morse, sep = "", end = "")
main()