'''

Morse code encoder and decoder

Run the program, navigate the menue using 1,2 or 3
then enter the string you want to convert.

'''

import time

#Morse code dictionary
morse_code_dict = {
    
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'

}


# Function to translate user string to morse code list
def morse_code_translate(user_input):

    new_output = ""

    for letter in user_input.upper():
        if letter in morse_code_dict:
            new_output += morse_code_dict[letter] + " "
    

    return new_output.split()    

#Main loop
main = True
while main == True:

    #Welcome message
    print("\nWelcome to the morse code translator \n")
    menue_response = input("Input 1 to encode text \nInput 2 to decode morse code \nInput 3 to exit\n\n")

    #Encode mode
    if menue_response == "1":
        
        #Get user string and convert to morse
        user_input = input("Enter your letters: ")
        morse_result = morse_code_translate(user_input)        


        # Iterate over morse list
        for value in morse_result:

            print(value)
            time.sleep(1)

        #Clear list for new input
        morse_result.clear()

            
    #Exit
    if menue_response == "3":
        main = False


# Confirm program end
print("Fin")


'''

Morse code encoder and decoder

Run the program, navigate the menue using 1,2 or 3
then enter the string you want to convert.

'''