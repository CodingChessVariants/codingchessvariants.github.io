*************************
Creating Special Rules
*************************
Special rules are 'special' because they can only occur under certain conditions. For example, Castling which can only occur if the king and rook have not moved from their initial positions.

Step 1: Implement the SpecialRules interface
===============================================
Implement getPossibleMoves() which should modify the given moves by either adding moves which satisfy the special condition, or modifying the moves to make sure they all satisfy a condition. For example, in Antichess if a player can take a piece they must take the piece.
This behaviour can be encapsualted like so:

.. code-block:: kotlin

 override fun getPossibleMoves(game: AbstractChess, player: Player, moves: MutableList<GameMove2D>) {
        val pred = { it: GameMove2D -> it is BasicGameMove && it.pieceCaptured != null }
        if (moves.any(pred)) { 
            moves.retainAll(pred)
        }
    }

This will modify the move list if it contains any capture moves to contain only capture moves.

Step 2: Add the list of special rules to your game type
========================================================
For example, in Antichess they would be added as the first parameter for AbstractChess.

.. code-block:: kotlin

  class AntiChess : AbstractChess(listOf(ForcedCaptureRule()), listOf(AntiChessWinConditions()))