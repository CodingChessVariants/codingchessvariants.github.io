**********************
Boards
**********************
Everything to do with chess boards

Board
==========

.. class:: interface Board<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>

Methods
-------

.. function:: fun getBoardState(): Array<Array<P?>>
      
      Returns a 2D representation of the board in terms of pieces. Coordinates with no pieces are null in the resulting array. **TODO: Change getBoardState to return a Map<Coordinate, P?>**

.. function:: fun addPiece(coordinate: C, piece: P)
      
      Adds a piece P at coordinate C onto the board.

.. function:: fun removePiece(coordinate: C, piece: P)
      
      Removes a piece P at coordinate C from the board.

.. function:: fun getPieces(): List<Pair<P, C>>
      
      Returns a list of pairs representing which coordinate each piece is on. **TODO: Change getPieces to return a Map<P, C>**

.. function:: fun getPieces(player: Player): List<Pair<P, C>>
      
      Returns a list of pairs representing which coordinate each piece is on for the given player. **TODO: Change getPieces to return a Map<P, C>**

.. function:: fun getPiece(coordinate: C): P?
      
      Returns the piece on the given coordinate if there is one. Otherwise returns null.

.. function:: fun getPieceCoordinate(piece: P): C?
      
      Returns the coordinate of a given piece by reference.

Board2D
==========

.. class:: class Board2D(val rows: Int, val cols: Int) : Board<Board2D, Move2D, GameMove2D, Piece2D, Coordinate2D> 

Implementation of the Board interface for a 2d square board. The board size is rows x cols and each coordinate can have upto one Piece2D.
