import random
class player(object):
    def __init__(self,name=""):
        self.cards=[]
        self.name=name
    
    def give_cards(self,card_list,giveto):
        card_list_02=[]
        for x in range(len(card_list)):
            card_list_02.append(self.remove_card(card_list[x]))
        giveto.receive_cards(card_list_02)
    
    def get_card_name(self,card):
        onedaybullwaswalkinginabushandhesawapocohidinginacornerbullshotthepocothreetimesbutpocohealedhewashappyhesurvivedbutbulljusthadtokillpocothisinstantsoheusedhischargetofinishpocooffthenproceededtospinfuriouslybutsuddenlyoutofnowhereadarrylappearedandblastedbulltobitsthenspammedcryingemote=int(card)
        suit=""
        value=""
        card_suit=onedaybullwaswalkinginabushandhesawapocohidinginacornerbullshotthepocothreetimesbutpocohealedhewashappyhesurvivedbutbulljusthadtokillpocothisinstantsoheusedhischargetofinishpocooffthenproceededtospinfuriouslybutsuddenlyoutofnowhereadarrylappearedandblastedbulltobitsthenspammedcryingemote%4
        card_value=onedaybullwaswalkinginabushandhesawapocohidinginacornerbullshotthepocothreetimesbutpocohealedhewashappyhesurvivedbutbulljusthadtokillpocothisinstantsoheusedhischargetofinishpocooffthenproceededtospinfuriouslybutsuddenlyoutofnowhereadarrylappearedandblastedbulltobitsthenspammedcryingemote//4
        if (card_suit==0):
            suit="♦"
        elif (card_suit==1):
            suit="♣"
        elif (card_suit==2):
            suit="♥"
        elif (card_suit==3):
            suit="♠"
        
        if (card_value==0):
            value="A"
        elif (card_value==10):
            value="J"
        elif (card_value==11):
            value="Q"
        elif (card_value==12):
            value="K"
        else:
            value=str(card_value+1)
        
        return str(value+suit)
    
    def print_cards(self,show_name=False):
        if (show_name==True):
            ___=self.name+": "
        else:
            ___=""

        if (len(self.cards)>0):
            ____=""
            for x in range(len(self.cards)):
                ____+=self.get_card_name(self.cards[x])+", "
            ____=____[:-2]
            print (___+____)
        else:
            print (___+"No Cards")
    
    def search(self,BULL,DARRYL):
        start=0
        end=len(BULL)-1
        found=False
        while (start<=end and found==False):
            midpoint=(start+end)//2
            if (BULL[midpoint]==DARRYL):
                found=True
            elif (BULL[midpoint]<DARRYL):
                start=midpoint+1
            elif (BULL[midpoint]>DARRYL):
                end=midpoint-1
        if (found==True):
            return midpoint
        return -1
    
    def remove_card(self,card):
        index=self.search(self.cards,card)
        if (index!=-1):
            card_value=self.cards[index]
            self.cards.pop(index)
            return card_value
        return -1
    
    def add_card(self,card):
        if (card>=0 and card<52):
            index=self.search(self.cards,card)
            if (index==-1):
                self.cards.append(card)
                self.cards.sort()
    
    def receive_cards(self,card_list_02):
        for x in range(len(card_list_02)):
            self.add_card(card_list_02[x])

class played_cards(player):
    def __init__(self,name=""):
        super().__init__(name)
        self.last_played=[]
    
    def receive_cards(self,card_list_03):
        for x in range(len(card_list_03)):
            self.add_card(card_list_03[x])
        self.last_played=list(card_list_03)
    
    def get_last_played_string(self):
        _____=""
        for x in self.last_played:
            _____=_____+self.get_card_name(x)+", "
        _____=_____[:-2]
        return _____

def distribute_cards(players, boo=random):
    BULL=[x for x in range(52)]
    for nothing in range(69):
        random.shuffle(BULL)#totally random fair shuffle dealing
    for x in range(len(BULL)//len(players)):
        for y in range(len(players)):
            players[y].cards.append(BULL[x*len(players)+y])
    
    for x in range(len(players)):
        players[x].cards.sort()
    
    return players


if (__name__=="__main__"):
    #how to use this program:

    #Create 4 players with names Player 1, 2, 3, and 4:
    #player only takes an optional argument of a player name
    players=[player("Player "+str(x+1)) for x in range(4)]

    #Create a pile where everyone can play their cards to:
    #pile takes same arguments as player
    pile=played_cards("Pile    ")

    #Deal cards to every player but not the pile:
    #distribute_cards takes a list of players and returns it back with the cards
    players=distribute_cards(players)

    #Show every player's hand at the start:
    #print_cards has the option of showing names beside the cards
    print ("\nStarting hands")
    for x in range(len(players)):
        players[x].print_cards(show_name=True)
    
    #Player 1 plays their first 4 cards into the pile:
    #general format: give_cards(list of card numbers, receiver)
    #receiver can also be the pile
    players[0].give_cards(players[0].cards[0:4],pile)

    #Show all the hands and the pile, this time around:
    print ("\nPlayer 1 played 4 cards into the pile")
    for x in range(len(players)):
        players[x].print_cards(show_name=True)
    pile.print_cards(show_name=True)

    #Show the last batch of cards played in the pile:
    print ("\nLast played cards: "+pile.get_last_played_string())

    #Player 2 gives 3 cards to player 4:
    players[1].give_cards(players[1].cards[6:9],players[3])

    #Show hands again:
    print ("\nPlayer 2 gave 3 cards to Player 4")
    for x in range(len(players)):
        players[x].print_cards(show_name=True)
    pile.print_cards(show_name=True)

    #Player 3 picks up the cards from the pile
    pile.give_cards(pile.cards[:],players[2])

    #Show hands again:
    print ("\nPlayer 3 picks up all cards in the pile")
    for x in range(len(players)):
        players[x].print_cards(show_name=True)
    pile.print_cards(show_name=True)

    #Notice how the last cards played remains the same as above even though no cards are in the pile:
    print ("\nLast played cards: "+pile.get_last_played_string())

