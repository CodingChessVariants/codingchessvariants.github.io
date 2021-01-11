**********************
Creating New Pieces
**********************

You can create new pieces easily by using move generators which give pieces their core behaviour. Special rules are applied applied to allow for special rules such as castling.

The engine has already implemented pieces which are used in Standard Chess, Capablanca Chess, Antichess, Grand chess, Xiangqi, and Janggi. These can be easily reused in your own variants .

For our chess variant, we will use the pre-implemented rook, bishop and king from Standard Chess. We will also implement our own Berlin pawn and elephant

Creating The Berlin Pawn
=======================================
The Berlin pawn is a piece which is the converse of a pawn in standard chess with a few key differences.
  - They can move one square diagonally without capturing. 
  - They can capture by moving one square straight forward.
  - On their first move, they can move two squares diagonally forwards.

Create a new **tutorial** package in the engine project (engine/src/main/kotlin). We will create two classes, one to represent the Berlin white pawn and one to represent the Berlin black pawn.

Create a file called BerlinWhitePawn.kt:
  
.. raw:: html

  <iframe
    src="https://carbon.now.sh/embed/9CBhCM1xOMCsazwXGUZf"
    style="width: 826px; height: 449px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
  </iframe>

Each piece is defined by a list of move generators which define the different moves that the pieces can usually make.

In the case of the Berlin white pawn:
  - The restricted stepper move denotes that the piece can move 2 steps in the north-east or north-west direction only when it is on the starting row (has not moved yet).
  - The promotion wrapper denotes that the moves within can result in promotion to a rook, alfil, bishop or queen when the pawn reaches the 6th row.
  - The stepper move in the add promotion wrapper denotes that the piece can move 1 step in the north-east or north-west direction.
  - The capture-only stepper in the add promotion move denotes that the piece can move 1 step north only when it is capturing a piece.

Similarly for the black pawn, create a file called BerlinBlackPawn.kt:
  
.. raw:: html

  <iframe
    src="https://carbon.now.sh/embed/LPlzCQchgD3SmPCdWU1u"
    style="width: 826px; height: 449px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
  </iframe>


Creating The Alfil
=======================================
The Alfil is a piece that can jump two squares diagonally and can leap over pieces.

Create a file called Alfil.kt:

.. raw:: html
  
  <iframe
    src="https://carbon.now.sh/embed/9QJjNMAmeA3ank2ZfSeG"
    style="width: 501px; height: 269px; border:0; transform: scale(1); overflow:hidden;"
    sandbox="allow-scripts allow-same-origin">
  </iframe>

The move generator used in this case is a leaper which will allow the Alfil to jump diagonally and leap over pieces.