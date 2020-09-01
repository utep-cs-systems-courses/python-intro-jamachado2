import re

def wordCount():
    # with statement automatically takes care of closing the file
    # r is only for reading, w is only for writing
    with open('declaration.txt', 'r') as d, open('myOutput.txt', 'w') as output:

        # Dictionary to store the total number of times each word appears
        wCounter = {}
        # Reads the whole file and split the words
        for line in d.read().split():
                
                #remove_punc = line.translate(str.maketrans('','', string.punctuation)).lower().split()
                remove_punc = re.sub(r'[^\w\s]','',line).lower().split()
                for word in remove_punc:
                        if word not in wCounter:
                            wCounter[word] = 1
                        else:
                            wCounter[word] += 1
        
        for k,v in sorted(wCounter.items()):
                output.write('{} {}'.format(k,v))
                output.write('\n') 
                #print('{:14} {:4}'.format(k,v))

                
if __name__ == "__main__":
    wordCount()