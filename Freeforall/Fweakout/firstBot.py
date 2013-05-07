import socket

network = 'irc.freenode.net'
channel = '#studypython'
nick = 'StudyBot'

chanMsg = "PRIVMSG #studypython :"

alive = True

def ping(): 
    irc.send("PONG :Pong\n")

def joinChan(chan):
    irc.send("JOIN "+chan+"\n")

def sendMsg(msg):
    irc.send("PRIVMSG #studypython :"+ msg +"\n")

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network,6667))
irc.send("USER "+nick+" "+nick+" "+nick+" :fweakout bot\n")
irc.send("NICK "+nick+"\n")

joinChan(channel)

while alive:
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    print ircmsg

    if ircmsg.find(":Hello "+nick) != -1:
        irc.send(chanMsg+"Hello!\n")

    if ircmsg.find(":!git") != -1:
        irc.send(chanMsg+"https://github.com/fnurk/studypython \n")

    if ircmsg.find(":!g+") != -1:
        irc.send(chanMsg+"https://plus.google.com/communities/116969234888661099943 \n")

    if ircmsg.find(":!curr") != -1:
        irc.send(chanMsg+"https://moot.it/learnpython \n")
    
    if ircmsg.find(":!dog") != -1:
        irc.send(chanMsg+"Woof woof woof WOOF! \n")

    if ircmsg.find(":!help") != -1:
        irc.send(chanMsg+"My commands are: !git, !g+, !curr, !dog and !help \n")

    if ircmsg.find(":!d1e "+nick) != -1:
        alive = False

    if ircmsg.find("PING :") != -1:
        ping()
