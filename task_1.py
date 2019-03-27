
def predict(word):
    word = word
    word = word.lower()
            
    Flag2 = 0
    missedletter = 0
    goodprediction = 0

    while(missedletter < 6 ):
        guess = input("Guess letter for input other than you enter before: ")
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

    word = input("Enter the word: ")

    var = predict(word)
    if var == 1:
        print("Your guess match with the word")
    if var == 0:
        print("Try next time")