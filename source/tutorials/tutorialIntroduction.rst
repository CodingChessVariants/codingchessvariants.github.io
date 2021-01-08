************************
Tutorial Introduction
************************

For this tutorial, we will be making our own chess variant.

Our chess variant will be played on a 7x7 2D square board excluding the center square.
It will consist of a mixture of standard chess pieces as well some variant chess pieces.

The standard pieces consist of:
  - Rook - moves any number of vacant squares horizontally or vertically and can capture opponent pieces at the destination.
  - Bishop - moves any number of vacant squares diagonally and can capture opponent pieces at the destination.
  - King - moves exactly one square horizontally, vertically or diagonally and can capture opponent pieces at the destination.

The variant pieces consists of:
  - Elephant - Jumps two squares diagonally and can capture opponent pieces at the destination
  - Berlin Pawn - Can move two squares diagonal forwards on the first move. Moves one square diagonally without capturing or captures by moving one square forward.

The initial setup of the board will look like as follows:

(ADD FIGURE HERE)

The rules of the game are as follows:
  - The king can be checked and must move when it is in check.
  - The same piece cannot be moved twice in a row.
  - There is no castling or enpassant.
  - Pawns must promote to a rook, bishop or elephant once it reaches the last rank

The game ends when:
  - A player wins once they takes all the opponents pawns
  - A player wins by checkmating the opponent
  - Stalemate by no moves for a player not in checkmate
  - Stalemate by threefold repetition

