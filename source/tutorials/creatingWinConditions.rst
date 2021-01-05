**********************************
Creating Win Conditions
**********************************
Win conditions are evaluated every turn to see if the game should end. The win conditions should be specified in each game type.
For example, the standard win conditions are:

- Checkmate,
- Stalemate by no legal moves
- Stalemate by three-fold-repetition
- Stalemate by the 50-move rules
- Stalemate by insufficient material.

Specific win conditions can be added such as for Antichess, where the king can be taken and the winner wins when they have lost all their pieces.

To add a custom win condition, you should implement the evaluate method to decide whether the current game state satisfies the condition.
Returning null means the condition has not been satisfied. Otherwise, this method should return a specific Outcome indicating the outcome of the game.
