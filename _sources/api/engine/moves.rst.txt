**********************
Moves
**********************
Everything to do with moves

Move
==========
.. class:: interface Move<B : Board<B, M, GM, P, C>, M : MoveGenerator<B, M, GM, P, C>, GM : Move<B, M, GM, P, C>, P : Piece<B, M, GM, P, C>, C : Coordinate>

GameMove2D
==========

.. class:: sealed class Move2D(open val player: Player) : Move<Board2D, Move2D, Move2D, Piece2D, Coordinate2D>

Implementation of the Move interface for a 2d square board.
Contains the starting and ending coordinates, the piece moved,
the piece captured and the piece promoted to.
