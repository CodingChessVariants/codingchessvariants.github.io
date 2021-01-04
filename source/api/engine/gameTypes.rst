**********************
Game Types
**********************

GameType
========
.. class:: interface GameType<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>

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

      Retruns the next player without incrementing the turn.

.. function:: fun playerMakeMove(move: GM)

      Makes a given move and increments the turn.
