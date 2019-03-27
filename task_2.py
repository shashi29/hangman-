import pandas as pd
import time
def predict(data , word):
    word = word
    data = data.copy()
    word = word.lower()
    Flag = 0
    input_word_length = len(word)
    print("Lenght of input character",input_word_length)
    #Filter out the word from data which has length = input_word_length
    specific_data = data[data['Word_length']==input_word_length]
    print(specific_data.head)
            
    Flag2 = 0
    missedletter = 0
    goodprediction = 0
    
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
        counts_df = counts_df[3:]
        counts_df.sort_values(by='Count',axis=0,inplace=True,ascending=False)
        #print((counts_df.head))
        #print(counts_df.head())
        #guess = input("Guess letter for input: ")
        #first_letter = counts_df['Letter'].values[0]
        #print("First prediction of the letter",first_letter)
        store_index = []
        count = 0
        for char in counts_df['Letter']:
        #counts_df = counts_df.iloc[1:]
            print(counts_df.head)
            for index,s in enumerate(range(len(word))):
                if word[s] == char:
                    print("The predicted letter is",char)
                    count = +1
                    print("Find the first match")
                    store_index.append(index)
                    goodprediction = goodprediction + 1
                    print("Prediction happens correctly",goodprediction)
                    if goodprediction == input_word_length:
                        print("Number of iteration takes to predict",count)
                        return 1
        
    return 0
                
if __name__ == "__main__":
    start = time.time()
    data = pd.read_csv("words.txt",header=None)
    data.columns = ['Word']
    data['Word_length'] = data['Word'].str.len()
    correct_pred = 0
    for word in data['Word']:
        var = predict(data,word)
        if var == 1:
            print("Your guess match with the word")
            correct_pred =+1
        if var == 0:
            print("Try next time")
            
    print("Total number of correct prediction",correct_pred)
    end = time.time()
    print("Total time for prediction",end - start)