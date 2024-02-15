# Prime Game
### Author: AlvyneZ

## Question
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1
 up to and including n, they take turns choosing a prime number from the set and removing
 that number and its multiples from the set. The player that cannot make a move loses
 the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria
 always goes first and both players play optimally, determine who the winner of each game
 is.

## Solution
The solution needs to count the number of prime numbers between 1 and n..
 For each round, an even count of prime numbers including 0 means Ben wins, Maria wins
 otherwise.
