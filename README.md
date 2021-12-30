# Simulated Annealing for Minimum Domination Problem #

This code is using simulated annealing to find the most optimal piece placement such that the piece’s attack covers the whole board. The project was done for more understanding of simulated annealing. The addition to this project was so that inputs of fairy chess pieces could be used and Parlett's movement notation is used to determine the movement of the board.


Simulated Annealing
-------------------

To set up this explanation, the mountain problem will be used. Imagine that you are climbing a mountain — you could be starting at the bottom of the mountain, the middle, or just near the top. You don’t necessarily know the best way up to the top of this mountain, but you decide to just pick a direction and go anyways, regardless of if it’s going down or up. Going down represents a worse solution, and going up represents a better solution.

Annealing is a term used in metallurgy to take a heated metal and allow it to cool slowly to remove internal stresses and essentially to make the metal less brittle, and thus much stronger.

This could be used in real life process to describe the way simulated annealing works, and thus some key words / phrases you’ll need to know to start to understand what is being talked about.

Temperature — The initial probability you set: the higher the temperature, the higher chance the algorithm will accept a worse solution, i.e. going down the mountain rather than up the mountain.

Cooling Rate — The rate at which reduces the possibility that the algorithm accepts a worse solution. If you imagine a loop, it can multiply cooling rate by temperature to lower the temperature each iteration so that at the end, you’ll have a super low temperature and thus an extremely low probability the algorithm accepts a worse solution

The evaluation function used was:

![f(x)=\frac{n}{v}+\frac{1}{gv}](https://latex.codecogs.com/svg.latex?f(x)=\frac{n}{v}+\frac{1}{gv}) 

where n is number of dominated nodes, v is number of all the nodes, g is number of pieces on the board. 

Running the Code
----------------

To run the code simply just run
```
python sa_main.py
```
This will run the values to be in an size 8 board with queen as the chess piece.

To run the code with different inputs it could be done by using
```
python sa_main.py -s 10 -n nX
```
starts a value with bishop and size 10 board

You could also run
```
python sa_main.py --help
```
to see the different options it offers
