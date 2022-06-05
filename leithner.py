lists = []
class card(object):
    def __init__(self, word, meaning ,review, boxnumber ):
        self.word = word
        self.meaning = meaning
        self.boxnumber = boxnumber
        self.review = review
    #def getmeaning(self):
     #   return self.meaning  
    def __str__(self):
        return self.word + ' : ' + self.meaning 
# Defining a function for making a list of flashcards
    def flashcard(flash, words, meanings,boxnumbers ,reviews):
        flash.append(card(words, meanings , boxnumbers , reviews))
        return flash

    def new_word():
        global lists
        y = input("Want to add a flashcard? ")
        while  y == 'y' or y == 'Y':
            word = input("Word you want to add to your Flashcards: ")
            meaning = input("Meaning of the word in flashcard: ")
            boxnumber = 0
            review = False
            lists = card.flashcard(lists, word, meaning,boxnumber , review)
            y = input("for adding another flashcard, press Y/y :")
        else:
            #print("----Following are the flashcards you made----")
            for el in lists:
   	            print(el)    
def practice():
    for el in lists:
        print(el.word)
        x = input("enter the meaning : ")
        if x == el.meaning :
            el.boxnumber =+ 1
        else :
            el.boxnumber = 1

#z = input("new or practice ")
#while z == 'new':
card.new_word()
practice()


