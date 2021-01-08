*************************
Creating Special Rules
*************************
Special rules are 'special' because they can only occur under certain conditions. For example, Castling which can only occur if the king and rook have not moved from their initial positions.

In our variant, the unique special rule is that a player cannot move the same piece twice in a row. These rules are applied when we fetch the moves a player can make to either filter the moves, or add furthr special moves.
In this case, we are restricting the moves a player can make by removing the moves which move the same piece the player move previously.


Step 1: Implement the SpecialRules interface
===============================================
1. Create a file called "NoRepeatedMoveFromSamePieceRule.kt" in the tutorials package you have created.
2. Make this class implement the SpecialRules2D<AbstractChess> interface.

.. code-block:: kotlin

    package tutorial

    import gameTypes.chess.AbstractChess
    import moves.Move2D
    import players.Player
    import rules.SpecialRules2D

    class NoRepeatedMoveFromSamePieceRule() : SpecialRules2D<AbstractChess> {
        override fun getPossibleMoves(game: AbstractChess, player: Player, moves: MutableList<Move2D>) {
            TODO()
        }
    }

Step 2: Implement the getPossibleMoves() method
===================================================
This function should modify the given moves list by removing all the moves that contain the piece that the player moved previously.
We can get the move the player previously made like so:
.. code-block:: kotlin

    val prevMove = game.moveLog[game.moveLog.size - 2]

This means we can easily remove the moves where the same piece is moved like so:

.. code-block:: kotlin

    override fun getPossibleMoves(game: AbstractChess, player: Player, moves: MutableList<Move2D>) {
        if (game.moveLog.size <= 1) {
            return
        }
        val prevMove = game.moveLog[game.moveLog.size - 2]
        moves.removeAll { it.displayPieceMoved === prevMove.displayPieceMoved }
    }

Step 3: Overall
=================
The NoRepeatedMoveFromSamePieceRule class should now look like this.
.. code-block:: kotlin

    package tutorial

    import gameTypes.chess.AbstractChess
    import moves.Move2D
    import players.Player
    import rules.SpecialRules2D

    class NoRepeatedMoveFromSamePieceRule() : SpecialRules2D<AbstractChess> {
        override fun getPossibleMoves(game: AbstractChess, player: Player, moves: MutableList<Move2D>) {
            if (game.moveLog.size < 2) {
                return
            }

            val prevMove = game.moveLog[game.moveLog.size - 2]
            moves.removeAll { it.displayPieceMoved === prevMove.displayPieceMoved }
        }
    }
