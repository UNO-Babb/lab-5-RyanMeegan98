#LetterFrequency.py
#Name:Ryan Meegan
#Date:Feb 23 2025
#Assignment:Letter Freq

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0] * 26  

    
    for letter in message:
        if letter in alpha:  
            index = alpha.index(letter)  
            freq[index] += 1  

    
    output = "Letter,Frequency\n"  
    for i in range(26):
        print(alpha[i], ":", freq[i])  
        output += f"{alpha[i]},{freq[i]}\n"  

    writeToFile(output)

def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    with open("frq.csv", 'w') as freqFile:
        freqFile.write(fileText)

    print("Frequency data saved to frq.csv")

def main():
    msg = input("Enter a message: ")
    countLetters(msg)

if __name__ == '__main__':
    main()
