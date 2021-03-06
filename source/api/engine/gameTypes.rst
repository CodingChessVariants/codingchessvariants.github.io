**********************
Game Types
**********************

GameType
========
.. class:: interface GameType<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: Move<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>

Represents a game variant (e.g. Standard Chess, Capablanca Chess, Xiangqi).
Controls the flow of a game and keeps track of all the game moves in the move log, 
which player has the current turn and the final result of the game.

Methods
-------

.. function:: fun initGame()

      Initialises the game. Places pieces on the initial position of the board.

.. function:: fun isOver(): Boolean

      Returns true if the game is over.

.. function:: fun getOutcome(player: Player): Outcome?

      Returns the outcome of the game for the given player, which can be either Win or Draw.
      Returns null if the game is not over.

.. function:: fun getOutcome(): Outcome?

      Returns the outcome of the game for the current player, which can be either Win or Draw.
      Returns null if the game is not over.

.. function:: fun getValidMoves(player: Player): List<GM>

      Returns a list of all possible valid moves of the given player.

.. function:: fun getValidMoves(): List<GM>

      Returns a list of all possible valid moves of the current player.

.. function:: fun makeMove(gameMove: GM)

      Makes the given move and add it to the move log.

.. function:: fun undoMove()

      Reverts the last move and removes it from the move log.

.. function:: fun inCheck(player: Player) : Boolean

      Returns true if the given player's King is in check.

.. function:: fun prevPlayer()

      Decrements the turn.

.. function:: fun nextPlayer()

      Increments the turn.

.. function:: fun getCurrentPlayer(): Player

      Returns the current player.

.. function:: fun getNextPlayer(): Player

      Returns the next player without incrementing the turn.

.. function:: fun playerMakeMove(move: GM)

      Makes a given move and increments the turn.

SpecialRules
=============

Represents special rules that are specific to games, such as Castling and En Passant.

Methods
--------

.. function:: fun getPossibleMoves(game: @UnsafeVariance T, player: Player, moves: MutableList<GameMove2D>)

      Returns the possible moves generated as a result of the special rule.


Win Conditions
================

Represents conditions for stalemates or checkmates. These are evaluated every turn to see if the game should end. The win conditions should be specified in each game type.
The standard win conditions have already been implemented. These are:

- Checkmate,
- Stalemate by no legal moves
- Stalemate by three-fold-repetition
- Stalemate by the 50-move rules
- Stalemate by insufficient material.


Methods
-------

.. function:: fun evaluate(game: @UnsafeVariance T, player: Player, moves: List<GameMove2D>): Outcome?
      
      Returns an outcome if the game should end if it satisfies the condition, otherwise returns null.