***************************
Set up Board
***************************

Right now, your TutorialChess.kt should look like this:

.. code-block:: kotlin 

  package tutorial

  import boards.Board2D
  import gameTypes.chess.AbstractChess2D

  open class TutorialChess : AbstractChess2D(
                                    listOf(),
                                    listOf()
  {
    override val board: Board2D = TODO()
    override val name = "Tutorial Chess"

    override fun initBoard() {
        TODO()
    }
  }

Step 1: Creating a board
---------------------------
Since our variant uses a 2D rectangular based board, we can use the Board2D interface to create the board.
Our restriction for the board is that the centre square is out of bounds. This can be defined by a coordinate region like so:

.. code-block:: kotlin

  private val outOfBoundsRegion = CoordinateRegion(3, 3)

Our variant uses a 7x7 board, and therefore can be defined like so:

.. code-block:: kotlin

  private val outOfBoundsRegion = CoordinateRegion(3, 3)
  override val board: Board2D = Board2D(7, 7, outOfBoundsRegion)


Step 2: Implementing initBoard()
------------------------------------
This function should setup the initial piece placements and is called everytime this game is started.
Put each player into a variable for ease of use.

.. code-block:: kotlin

  override fun initBoard() {
      val player1 = players[0]
      val player2 = players[1]
  }

1. Adding Pawns
^^^^^^^^^^^^^^^^^
We can add the Berlin Pawns to the board with a for loop like so:

.. code-block:: kotlin

  override fun initBoard() {
      val player1 = players[0]
      val player2 = players[1]
      for (i in 0..6) {
          board.addPiece(Coordinate2D(i, 1), BerlinWhitePawn(player1))
          board.addPiece(Coordinate2D(i, 5), BerlinBlackPawn(player2))
      }
  }

2. Adding the backline pieces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The rest of the pieces can be added using FEN notation using the
FEN chess notation.

.. code-block:: kotlin

  rbakbar/ppppppp/7/7/7/PPPPPPP/RBAKBAR

This represents the inital positions of pieces in this variant.
As the Berlin pawn and Alfil are fairy pieces, we must add them to the FEN mapping.


We then initialise the board using FEN notation.

.. code-block:: kotlin

  override fun initBoard() {
    val fen = FenUtility("rbakbar/ppppppp/7/7/7/PPPPPPP/RBAKBAR")
    
    fen.extendFenPieces('a', ::Alfil)
    fen.extendFenPiecesCaseSensitive('p', ::BerlinWhitePawn, ::BerlinBlackPawn)
    
    fen.initBoardWithFEN(board, players[0], players[1])
  }

Step 3: Overall
-----------------

.. code-block:: kotlin

  package tutorial

  import boards.Board2D
  import coordinates.Coordinate2D
  import gameTypes.chess.AbstractChess
  import pieces.chess.*
  import regions.CoordinateRegion
  
  open class TutorialChess : AbstractChess2D(
                                    listOf(),
                                    listOf()
  {
      private val outOfBoundsRegion = CoordinateRegion(3, 3)
      override val board: Board2D = Board2D(7, 7, outOfBoundsRegion)
      override val name = "Tutorial Chess"

        override fun initBoard() {
          val fen = FenUtility("rbakbar/ppppppp/7/7/7/PPPPPPP/RBAKBAR")
          
          fen.extendFenPieces('a', ::Alfil)
          fen.extendFenPiecesCaseSensitive('p', ::BerlinWhitePawn, ::BerlinBlackPawn)
          
          fen.initBoardWithFEN(board, players[0], players[1])
        }
  }
