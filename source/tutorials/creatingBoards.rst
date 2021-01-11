***************************
Setting Up The Board
***************************

Right now, your TutorialChess.kt should look like this:

.. code-block:: kotlin 

  package tutorial

  import boards.Board2D
  import gameTypes.chess.AbstractChess
  open class TutorialChess : AbstractChess(
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
The rest of the pieces can be added like so.

.. code-block:: kotlin

  override fun initBoard() {
    val player1 = players[0]
    val player2 = players[1]
    for (i in 0..6) {
        board.addPiece(Coordinate2D(i, 1), BerlinWhitePawn(player1))
        board.addPiece(Coordinate2D(i, 5), BerlinBlackPawn(player2))
    }
    board.addPiece(Coordinate2D(0, 0), Rook(player1))
    board.addPiece(Coordinate2D(6, 0), Rook(player1))
    board.addPiece(Coordinate2D(0, 6), Rook(player2))
    board.addPiece(Coordinate2D(6, 6), Rook(player2))

    board.addPiece(Coordinate2D(1, 0), Bishop(player1))
    board.addPiece(Coordinate2D(4, 0), Bishop(player1))
    board.addPiece(Coordinate2D(1, 6), Bishop(player2))
    board.addPiece(Coordinate2D(4, 6), Bishop(player2))

    board.addPiece(Coordinate2D(2, 0), Alfil(player1))
    board.addPiece(Coordinate2D(5, 0), Alfil(player1))
    board.addPiece(Coordinate2D(2, 6), Alfil(player2))
    board.addPiece(Coordinate2D(5, 6), Alfil(player2))

    board.addPiece(Coordinate2D(3, 0), King(player1))
    board.addPiece(Coordinate2D(3, 6), King(player2))
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
  
  open class TutorialChess : AbstractChess(
                                    listOf(),
                                    listOf()
  {
      private val outOfBoundsRegion = CoordinateRegion(3, 3)
      override val board: Board2D = Board2D(7, 7, outOfBoundsRegion)
      override val name = "Tutorial Chess"

      override fun initBoard() {
          val player1 = players[0]
          val player2 = players[1]
          for (i in 0..6) {
              board.addPiece(Coordinate2D(i, 1), BerlinWhitePawn(player1))
              board.addPiece(Coordinate2D(i, 5), BerlinBlackPawn(player2))
          }
          board.addPiece(Coordinate2D(0, 0), Rook(player1))
          board.addPiece(Coordinate2D(6, 0), Rook(player1))
          board.addPiece(Coordinate2D(0, 6), Rook(player2))
          board.addPiece(Coordinate2D(6, 6), Rook(player2))

          board.addPiece(Coordinate2D(1, 0), Bishop(player1))
          board.addPiece(Coordinate2D(4, 0), Bishop(player1))
          board.addPiece(Coordinate2D(1, 6), Bishop(player2))
          board.addPiece(Coordinate2D(4, 6), Bishop(player2))

          board.addPiece(Coordinate2D(2, 0), Alfil(player1))
          board.addPiece(Coordinate2D(5, 0), Alfil(player1))
          board.addPiece(Coordinate2D(2, 6), Alfil(player2))
          board.addPiece(Coordinate2D(5, 6), Alfil(player2))

          board.addPiece(Coordinate2D(3, 0), King(player1))
          board.addPiece(Coordinate2D(3, 6), King(player2))
      }
  }
