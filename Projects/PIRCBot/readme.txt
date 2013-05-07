This is the first project, we're going to make an IRC bot. 



Messages are sent over IRC looking like this:

:fnurk_!5efe164b@gateway/web/freenode/ip.94.254.22.75 PRIVMSG #fnurkstestsite :hello

Where 	"fnurk_" is the nickname
	"5efe164b@gateway/web/freenode/ip.94.254.22.75" is the host,
	"PRIVMSG" is the type of message and 
	"#fnurkstestsite" is the target
	"hello" is the message itself.
	the ":"s and the "!" are part of the message syntax.

Useful links:
  Pydocs:
    http://docs.python.org/2/library/socket.html#socket-objects
    http://docs.python.org/2/library/string.html#string-functions
  Wikipedia:
    http://en.wikipedia.org/wiki/List_of_Internet_Relay_Chat_commands
  Connect to 3 test channels(pick one that isn't very crowded):
    http://94.254.22.75/chat/