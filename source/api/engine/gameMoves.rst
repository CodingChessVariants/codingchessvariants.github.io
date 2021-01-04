**********************
Game Moves
**********************
Everything to do with game moves

GameMove
==========
.. class:: interface GameMove<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM : GameMove<B, M, GM, P, C>, P : Piece<B, M, GM, P, C>, C : Coordinate>

GameMove2D
==========

.. class:: sealed class GameMove2D(open val player: Player) : GameMove<Board2D, Move2D, GameMove2D, Piece2D, Coordinate2D> {

Implementation of the Board interface for a 2d square board.
Contains the starting and ending coordinates, the piece moved,
the piece captured and the piece promoted to.
