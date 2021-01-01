import socket,threading
class Bullservercode(threading.Thread):
    users=0
    DARRYL=[]
    max_barrel_size=25
    close_server=False
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
            if (len(bitingtext_01)>1):
                text=bitingtext_01[1]
            else:
                text="someone is trying to crash my program"

            if (text=="leave server"):#stop the function when the client decides to leave.
                #print (name+" has left the server.")
                if (name!="BullDarrylCloseServer"):
                    self.add_to_chat(name+" has left the server.")
                done_01=True
            else:
                if (text=="all-purple profile randoms have hollow skulls"):#the text is sent when someone first joins.
                    #print (name+" has joined the server.")
                    if (name!="BullDarrylCloseServer"):
                        self.add_to_chat(name+" has joined the server.")
                elif (text=="close"):
                    if (Bullservercode.close_server==False):
                        self.add_to_chat("New users can no longer join the server.")
                        Bullservercode.close_server=True
                        self_connection(host,port)

                elif (text!=""):#if any other text is sent, display it
                    #print (name+": "+text)
                    #print (self.sendback(name,text))
                    self.add_to_chat(self.sendback(name,text))
                
                if (first_time_01):
                    self.conn.send("Welcome to the server. Type to chat and type 'leave server' to disconnect.".encode())
                else:#run a function to determine what to send back
                    self.conn.send(self.sendback_02().encode())
                first_time_01=False

            self.show_chat()
        
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