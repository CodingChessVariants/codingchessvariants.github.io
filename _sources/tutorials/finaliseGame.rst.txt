========================
Completing the Game
========================

Go back to the TutorialChess class you created. The constructor should look like this. 

.. code-block:: kotlin 

  open class TutorialChess : AbstractChess2D(
                                      listOf(),
                                      listOf()
    )

As we have created the unique special rules and win conditions, we can now add these as parameters to AbstractChess.

Step 1. Add Special Rules
----------------------------
There is only one special rule that needs to be added which is the one we created previously, NoRepeatedMoveFromSamePieceRule.
We can add this like so:

.. code-block:: kotlin

  open class TutorialChess : AbstractChess2D(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf()
  )

Step 2. Add Win Conditions
-----------------------------
There is one unique win condition that needs to be added which is the one we created previously, AllPawnsCapturedEndCondition.
We can add this like so:

.. code-block:: kotlin

  open class TutorialChess : AbstractChess2D(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf(AllPawnsCapturedEndCondition())
  )

We also need to add the other non-unique win condition that has already been implemented in the library. These are:
  - A player wins by checkmating the opponent's king.
  - Stalemate by no moves for a player not in checkmate
  - Stalemate by threefold repetition

We can add these like so: 

.. code-block:: kotlin 

  open class TutorialChess : AbstractChess2D(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf(AllPawnsCapturedEndCondition(), StandardEndConditions())
  )

Step 3. Overall
------------------
The final class should look like this:

.. code-block:: kotlin

  package tutorial

  import boards.Board2D
  import coordinates.Coordinate2D
  import gameTypes.chess.AbstractChess2D
  import pieces.chess.*
  import regions.CoordinateRegion
  import winconditions.StandardEndConditions

  open class TutorialChess : AbstractChess2D(
                                    listOf(NoRepeatedMoveFromSamePieceRule()),
                                    listOf(AllPawnsCapturedEndCondition(), StandardEndConditions()) {
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
