import re
import sys

def wordCount():

    textFname = sys.argv[1]
    outputFname = sys.argv[2]
    # with statement automatically takes care of closing the file
    # r is only for reading, w is only for writing
    with open(textFname, 'r') as d, open(outputFname, 'w') as output:

        # Dictionary to store the total number of times each word appears
        wCounter = {}
        # Read the whole file and split the string into a list
        for line in d.read().split():
                # ^ Matches the start of the string
                # \w matches unicode word characters [a-zA-Z0-9_]
                # \s matches unicode whitespace characters [\t\n\r\f\v]
                # re.sub() return the string obtaied by replacing the leftmost non
                # overlapping occurrences of pattern in string by the replacement repl
                remove_punc = re.sub(r'[^\w\s]','',line).lower().split()
                for word in remove_punc:
                        # Add a word that is not in the dictionary
                        if word not in wCounter:
                            wCounter[word] = 1
                        # Get the number of times the word appears in the .txt
                        else:
                            wCounter[word] += 1

        # Sort all words in the document in descending order
        for k,v in sorted(wCounter.items()):
                output.write('{} {}'.format(k,v))
                output.write('\n') 
                #print('{:14} {:4}'.format(k,v))

# Runs everythong in the code                
if __name__ == "__main__":
    wordCount()
