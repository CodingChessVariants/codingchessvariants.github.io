**********************
Pieces
**********************
Everything to do with pieces.

WhitePawn and BlackPawn can be directly overidden to change the settings for the starting row, promotion region, and the list of pieces it can promote to.


Piece
==========

.. class:: interface Piece<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>

Represents a piece. Contains the player that owns the piece and appropriate movement types.

Methods
-------

.. function:: fun getSymbol(): String

      Returns a unique symbol of the piece for the console game.
