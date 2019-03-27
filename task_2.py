import pandas as pd
def predict(data , word):
    word = word
    data = data.copy()
    word = word.lower()
    Flag = 0
    input_word_length = len(word)
    print("Lenght of input character",input_word_length)
    #Filter out the word from data which has length = input_word_length
    specific_data = data[data['Word_length']==input_word_length]
    print(specific_data.head())
    for i in specific_data['Word']:
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
            #We are not guessing , we are suggesting the highest occurence
            #Next make a corpus
            corpus = ', '.join(specific_data.Word)
            corpus = list(corpus)
            counts = dict()
            for letter in corpus:
                if letter in counts:
                    counts[letter] +=1
                else:
                    counts[letter] = 1
            #Next select the word with highest frequency
            counts_df = pd.DataFrame([counts])
            counts_df.reset_index(inplace=True)
            counts_df = counts_df.T
            counts_df.reset_index(inplace=True)
            counts_df.columns = ['Letter','Count']
            counts_df = counts_df[2:]
            print((counts_df.head))
            #print(counts_df.head())
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
                    return 1
        print("You lost all 6 chances of guess")
        return 0
                
if __name__ == "__main__":
    data = pd.read_csv("words.txt",header=None)
    data.columns = ['Word']
    data['Word_length'] = data['Word'].str.len()    
    word = input("Enter the word: ")
    var = predict(data,word)
    if var == 1:
        print("Your guess match with the word")
    if var == 0:
        print("Try next time")