import random,socket,threading
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

def distribute_cards(players):
    BULL=[x for x in range(52)]
    for nothing in range(69):
        random.shuffle(BULL)#totally random fair shuffle dealing
    for x in range(len(BULL)//len(players)):
        for y in range(len(players)):
            players[y].cards.append(BULL[x*len(players)+y])
    
    for x in range(len(players)):
        players[x].cards.sort()
    
    return players

def convert_cards_to_string(players):
    if (len(players)<=1):
        return "game has not started yet??????????????"

    HSUBLYRRADLLUB="green button yellow button red button win lane win game \\n "
    for WHY_WAS_X_TAKEN in range(len(players)):
        if (WHY_WAS_X_TAKEN!=0):
            HSUBLYRRADLLUB+=" \\n "
        HSUBLYRRADLLUB+=(players[WHY_WAS_X_TAKEN].name+".")
        BULLDARRYLBUSH=""
        for x in range(len(players[WHY_WAS_X_TAKEN].cards)):
            if (x!=0):
                BULLDARRYLBUSH+=" "
            BULLDARRYLBUSH+=(str(players[WHY_WAS_X_TAKEN].cards[x]))
        HSUBLYRRADLLUB+=str(BULLDARRYLBUSH)
    return HSUBLYRRADLLUB


class Bullservercode(threading.Thread):
    users=0
    DARRYL=[]
    usernames=[]
    max_barrel_size=25
    close_server=False
    #players=[player("Player "+str(x+1)) for x in range(4)]
    #pile=played_cards("Pile    ")
    #players=distribute_cards([player("Player "+str(x+1)) for x in range(4)])
    players=[]
    pile=played_cards("Pile    ")
    def __init__(self,conn,addr):
        super().__init__()
        self.conn=conn
        self.addr=addr
    def run(self):
        done_01=False
        first_time_01=True
        text=""
        name=""
        while (done_01==False):
            bitingtext=self.conn.recv(4096)#client sends first - they send their information to the server.
            bitingtext_01=bitingtext.decode().split(",.delete bea's gadget,")
            name=bitingtext_01[0]
            if (name not in Bullservercode.usernames):
                Bullservercode.usernames.append(name)
            
            if (len(bitingtext_01)>1):
                text=bitingtext_01[1]
            else:
                text="someone is trying to crash my program"

            if (text=="leave server"):#stop the function when the client decides to leave.
                #print (name+" has left the server.")
                if (name!="BullDarrylCloseServer"):
                    self.add_to_chat(name+" has left the server.")
                if (name in Bullservercode.usernames):
                    Bullservercode.usernames.remove(name)
                done_01=True
            else:
                if (text=="all-purple profile randoms have hollow skulls"):#the text is sent when someone first joins.
                    #print (name+" has joined the server.")
                    if (name!="BullDarrylCloseServer"):
                        self.add_to_chat(name+" has joined the server.")
                elif (text=="start"):
                    if (Bullservercode.close_server==False):
                        #self.add_to_chat("New users can no longer join the server.")
                        Bullservercode.close_server=True
                        Bullservercode.players=distribute_cards([player(Bullservercode.usernames[x]) for x in range(len(Bullservercode.usernames))])
                        Bullservercode.pile=played_cards("Pile    ")
                        self_connection(host,port)
                        


                elif (text!="" and Bullservercode.close_server==True):#if any other text is sent, display it
                    #print (name+": "+text)
                    #print (self.sendback(name,text))
                    #self.add_to_chat(self.sendback(name,text))
                    if (text[:8]=="transfer"):
                        text_02=text.split(" ")
                        if (len(text_02)>=4):
                            if (len(text_02[1:3])==len([function for function in text_02[1:3] if function.isnumeric()==True])):#funny way to see if all the elements are numbers with horizontal coding
                                text_02[1]=int(text_02[1])-1#MAKE SURE YOU ARE AWARE THAT THIS ADDS 1 TO THE INDEX I SWEAR YOU WILL FORGET AND WONDER WHY THE INDEX IS OUT OF RANGE LATER.
                                text_02[2]=int(text_02[2])-1########################################################################################

                                #if ("-" in text_02[3:]):
                                transfer_cards=[]
                                dashes=text_02[3:]
                                for x in range(len(dashes)):
                                    if ("-" in dashes[x]):
                                        dashes[x]=dashes[x].split("-")
                                        if (dashes[x][0].isnumeric() and dashes[x][1].isnumeric()):
                                            transfer_cards.extend(list(range(int(dashes[x][0]),int(dashes[x][1])+1)))
                                    else:
                                        if (dashes[x].isnumeric()):
                                            transfer_cards.append(int(dashes[x]))

                                if (text_02[1]!=text_02[2] and text_02[1]>-2 and text_02[1]<len(Bullservercode.players) and text_02[2]>-2 and text_02[2]<len(Bullservercode.players)):
                                    if (text_02[1]==-1):
                                        Bullservercode.pile.give_cards(transfer_cards,Bullservercode.players[text_02[2]])
                                    elif (text_02[2]==-1):
                                        Bullservercode.players[text_02[1]].give_cards(transfer_cards,Bullservercode.pile)
                                    else:
                                        Bullservercode.players[text_02[1]].give_cards(transfer_cards,Bullservercode.players[text_02[2]])
                    elif (text[:4]=="deal"):
                        #Bullservercode.players=distribute_cards([player(Bullservercode.usernames[x]) for x in range(Bullservercode.users)])
                        Bullservercode.players=distribute_cards([player(Bullservercode.usernames[x]) for x in range(len(Bullservercode.usernames))])
                        Bullservercode.pile=played_cards("Pile    ")
                
                if (first_time_01):
                    self.conn.send("Welcome to the server. Type to chat and type 'leave server' to disconnect.".encode())
                else:#run a function to determine what to send back
                    #self.conn.send(self.sendback_02().encode())
                    all_players=list(Bullservercode.players)
                    all_players.append(Bullservercode.pile)
                    self.conn.send(convert_cards_to_string(all_players).encode())
                first_time_01=False

            #self.show_chat()
        Bullservercode.users-=1#count of how many users are currently connected.
    def sendback(self,name,text):
        if (text=="users"):
            return "Users currently connected: "+str(Bullservercode.users)
        elif (text=="server"):
            return "KING GOLM"
        elif (text=="truth"):
            return "BULL > POCO"
        return (name+": "+text)
    def sendback_02(self):
        output_message=""
        for x in range(len(Bullservercode.DARRYL)):
            if (x!=0):
                output_message+=(" \\n ")
            output_message+=Bullservercode.DARRYL[x].strip()
        return output_message
    def add_to_chat(self,text):
        Bullservercode.DARRYL.append(text)
        Bullservercode.DARRYL=Bullservercode.DARRYL[-1*Bullservercode.max_barrel_size:]
    def show_chat(self):
        print ("\n"*60)
        for x in range(len(Bullservercode.DARRYL)):
            print (Bullservercode.DARRYL[x])

def self_connection(host_01,port_01):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host_01,port_01))
    client.send(("BullDarrylCloseServer"+",.delete bea's gadget,"+"all-purple profile randoms have hollow skulls").encode())

    bitingtext=client.recv(4096)#client already sent first above so this is the receiving part.
    text=bitingtext.decode()

    client.send(("BullDarrylCloseServer"+",.delete bea's gadget,"+"leave server").encode())
    client.close()



host="localhost"
port=42069
max_users=2
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host,port))

done=False
first_time=True
BULL="hurry up and decide whether you want more people"

while (done==False):
    
    #if (BULL=="yes"):#continue waiting for another user
    if (Bullservercode.close_server==False):
        if (first_time):
            BULL="why does my program have a chance to crash?"
        server.listen(1)
        conn,addr=server.accept()
        newthread=Bullservercode(conn,addr)
        Bullservercode.users+=1
        newthread.start()
    elif (Bullservercode.close_server==True):#exit the while loop and make new users unable to join.
        done=True
    first_time=False
    BULL="hurry up and decide whether you want more people"

#after the while loop users currently in the server can still send messages.
server.close()




'''
if 69:
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
'''