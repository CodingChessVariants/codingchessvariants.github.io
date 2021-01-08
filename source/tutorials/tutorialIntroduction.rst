************************
Tutorial Introduction
************************

For this tutorial, we will be making our own chess variant.

Our chess variant will be played on a 7x7 2D square board excluding the center square.
It will consist of a mixture of standard chess pieces as well some fairy pieces.

The standard pieces consist of:
  - Rook - moves any number of vacant squares horizontally or vertically and can capture opponent pieces at the destination.
  - Bishop - moves any number of vacant squares diagonally and can capture opponent pieces at the destination.
  - King - moves exactly one square horizontally, vertically or diagonally and can capture opponent pieces at the destination.

The variant pieces consists of:
  - Alfil - Jumps two squares diagonally and can capture opponent pieces at the destination
  - Berlin Pawn - Steps one square diagonally without capturing or captures by moving one square forward. Can step two squares diagonal forwards on the first move. 

The initial setup of the board will look like as follows:

.. figure:: /../_static/TutorialChessFigure.png
    :width: 50%

The bishops and the alfils of each player start on different coloured squares.

The game ends when:
  - A player wins once by taking all the opponent pawns
  - A player wins by checkmating the opponent's king.
  - Stalemate by no moves for a player not in checkmate
  - Stalemate by threefold repetition

The rules of the game are as follows:
  - The same piece cannot be moved twice in a row.
  - The king can be checked and must move out of check.
  - There is no castling or enpassant.
  - Pawns must promote to a queen, rook, bishop or alfil once it reaches the last rank. This carries risk as it means a pawn is lost, and therefore the opponent needs to capture one less pawn, but rewards the player by giving them a much more powerful piece.

The steps are as follows (please navigate to the specific tutorial pages!)
1. Create the fairy pieces.
2. Initialise the game.
3. Set up the board.
4. Create the special rules.
5. Create the special win conditions.
6. Add the rules and win conditions into the game.
7. Integrate into the desktop frontend.
