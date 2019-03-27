import pandas as pd

data = pd.read_csv("words.txt",header=None)
data.columns = ['Word']

#Take the input from the user
word = input("Enter the word: ")

#Check input lies within the list of word
#small letter
Flag = 0
word = word.lower()
for i in data['Word']:
    if i == word:
        print("The word in the list")
        Flag = 1
        break
        
#Check if Flag is 1
Flag2 = 0
missedletter = 0
goodprediction = 0
if(Flag == 1):
    print("Found the word")
    while(missedletter < 6 ):
        guess = input("Guess letter for input: ")
        for s in range(len(word)):
            if word[s] == guess:
                print("Find the first match")
                Flag2 = 1
                goodprediction = goodprediction + 1
                break


        if(Flag2 == 0):
            missedletter = missedletter + 1
            print("Number od bad predictions : ",missedletter)
        if(Flag2 == 1):
            if(goodprediction == len(''.join(set(word)))):
                print("We find the word in our database")
    print("You have entered 6 wrong guess")
    
if __name__ == "__main__":
    var = predict()