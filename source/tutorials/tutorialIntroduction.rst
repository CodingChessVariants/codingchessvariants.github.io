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
    :width: 70%

The rules of the game are as follows:
  - The same piece cannot be moved twice in a row.
  - The king can be checked and must move out of check.
  - There is no castling or enpassant.
  - Pawns must promote to a queen, rook, bishop or alfil once it reaches the last rank

The game ends when:
  - A player wins once by taking all the opponent pawns
  - A player wins by checkmating the opponent's king.
  - Stalemate by no moves for a player not in checkmate
  - Stalemate by threefold repetition

