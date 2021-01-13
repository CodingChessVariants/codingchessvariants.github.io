**********************************
Creating the new End Condition
**********************************

The end conditions for this chess variant are:
  - A player wins once by taking all the opponent pawns
  - A player wins by checkmating the opponent's king.
  - Stalemate by no moves for a player not in checkmate
  - Stalemate by threefold repetition

The first is a new end condition specific to this variant which we will implement here, and the remaining three are pre-existing standard end conditions.

Step 1: Create a new file
----------------------------
1. Create a new file called "AllPawnsCapturedEndCondition.kt" in the Tutorial package.
2. Create a class called AllPawnsCapturedEndCondition which implements the EndCondition2D<AbstractChess> interface

.. code-block:: kotlin 

  package tutorial

  import gameTypes.chess.AbstractChess2D
  import winconditions.EndCondition2D

  class AllPawnsCapturedEndCondition : EndCondition2D<AbstractChess2D> {
    // Leave this empty for now.
  }

Step 3: Implement the evaluate method
----------------------------------------
Now we implement the evaluate method. We want to return a win outcome for the other player if the player being evaluated has lost all their pawns, and null otherwise.

.. code-block:: kotlin

  override fun evaluate(game: AbstractChess2D, player: Player, moves: List<Move2D>): Outcome? {
    TODO()
  }

We need to check if the player has any pawns which we can do by evaluating this expression:

.. code-block:: kotlin

  game.board.getPieces(player).any { piece -> piece.first is Pawn })

This returns true if the player still has pawns. getPieces(player) returns a list of pairs of pieces to coordinates which is why we do a .first on the piece. 

If this expression is false, then we must return a win outcome for the other player

.. code-block:: kotlin

  override fun evaluate(game: AbstractChess2D, player: Player, moves: List<Move2D>): Outcome? {
    if (!game.board.getPieces(player).any { piece -> piece.first is Pawn }) {
      return Outcome.Win(game.getOpponentPlayer(player), "by opponent losing all pawns")
    }
  }

We need to check both players as:
  - The current player could win by taking the final pawn of their opponent.
  - The other player could win by the current player promoting their final pawn to another piece.

.. code-block:: kotlin

  override fun evaluate(game: AbstractChess2D, player: Player, moves: List<Move2D>): Outcome? {
    for (p in game.players) {
      if (!game.board.getPieces(p).any { piece -> piece.first is Pawn }) {
        return Outcome.Win(game.getOpponentPlayer(p), "by opponent losing all pawns")
      }
    }
  }

If the condition is not satisfied for either player, we return null. This gives us the final evaluate function. 

.. code-block:: kotlin

  override fun evaluate(game: AbstractChess2D, player: Player, moves: List<Move2D>): Outcome? {
    for (p in game.players) {
      if (!game.board.getPieces(p).any { piece -> piece.first is Pawn }) {
        return Outcome.Win(game.getOpponentPlayer(p), "by opponent losing all pawns")
      }
    }

    return null
  }

Step 4: Overall class
----------------------
The class should now look like this:

.. code-block:: kotlin

  package tutorial

  import gameTypes.chess.AbstracAbstractChess2DtChess
  import winconditions.EndCondition2D

  class AllPawnsCapturedEndCondition : EndCondition2D<AbstractChess2D> {
    override fun evaluate(game: AbstractChess2D, player: Player, moves: List<Move2D>): Outcome? {
      for (p in game.players) {
        if (!game.board.getPieces(p).any { piece -> piece.first is Pawn }) {
          return Outcome.Win(game.getOpponentPlayer(p), "by opponent losing all pawns")
        }
      }

      return null
    }
  }
