OPERATING SYSTEM:
Linux

DEPENDENCIES:
Python
Pygame

HOW TO RUN IT:

I did not focus on automating some connection stuff, so a little manual work is needed:

First it is necessary to define in connection.py the inet interface associated with your IP address.
For example, the currently interface in connection.py is "enp0s8". You can check your interface by typing ifconfig -a in the terminal.
Do this for all peers which will execute the game.

After that, prepare the hosts.txt file. 
Insert the ip address of each peer and assign its player number (should be between 1 and 4, otherwise the program will accuse error). 
The port number is free to choose (default is 2296).
The hosts.txt file must be exactly the same across all peers!

Now, run it in each peer by typing "python game.py" in the terminal. You can play it alone or between 2-4 players. The walls without a player will reflect the ball.

ABOUT:

I implemented the 4-player Online Pong using Python along with Pygame library. It runs in a peer to peer model 
using Python low level sockets interface. The game only starts when all the peers listed in the hosts.txt are connected.

At the beginning, each player is assigned to a paddle and can move it freely in his axis using the keyboard arrow keys. The ball starts at the middle and begins
moving to a fixed direction (at first it was going to be randomized, but it caused sync problems). The ball speed is fixed. There is no scoring system,
so if a player let the ball pass through his axis, the ball just appears again at the middle of the screen.

It is possible to change some game settings (like screen resolutions) in the settings.py

KNOWN PROBLEMS:

Sync: sync problems may occur, but the game is perfectly playable.
Wall not reflecting: sometimes a wall that has no players simply does not reflect the ball. I didn't had time to fix this.
