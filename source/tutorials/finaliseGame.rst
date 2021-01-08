========================
Finalise Game
========================

Go back to the TutorialChess class you created. The constructor should look like this. 

.. code-block:: kotlin 

  open class TutorialChess : AbstractChess(
                                      listOf(),
                                      listOf()
    )

As we have created the unique special rules and win conditions, we can add these as parameters to AbstractChess.

Step 1. Add Special Rules
-------------------
There is only one special rule that needs to be added which is the one we created previously, NoRepeatedMoveFromSamePieceRule.
We can add this like so:

.. code-block:: kotlin

  open class TutorialChess : AbstractChess(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf()
  )

Step 2. Add Special Rules
-------------------
There is one unique win condition that needs to be added which is the one we created previously, AllPawnsCapturedWinCondition.
We can add this like so:

.. code-block:: kotlin

  open class TutorialChess : AbstractChess(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf(AllPawnsCapturedWinCondition())
  )

We also need to add the other non-unique win condition that has already been implemented in the library. These are:
  - A player wins by checkmating the opponent's king.
  - Stalemate by no moves for a player not in checkmate
  - Stalemate by threefold repetition

We can add these like so: 

.. code-block:: kotlin 

  open class TutorialChess : AbstractChess(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf(Checkmate(), TutorialWinCondition(), ThreeFoldRepetitionStalemate(), NoLegalMovesStalemate())
  )

Step 3. Overall
------------------
The final class should look like this:

.. code-block:: kotlin

  package tutorial

  import boards.Board2D
  import coordinates.Coordinate2D
  import gameTypes.chess.AbstractChess
  import pieces.chess.*
  import regions.CoordinateRegion
  import winconditions.Checkmate
  import winconditions.NoLegalMovesStalemate
  import winconditions.ThreeFoldRepetitionStalemate

  open class TutorialChess : AbstractChess(listOf(NoRepeatedMoveFromSamePieceRule()), listOf(Checkmate(), TutorialWinCondition(), ThreeFoldRepetitionStalemate(), NoLegalMovesStalemate())) {
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
