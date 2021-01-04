**********************
Boards
**********************
.. class:: interface Board<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>
.. method:: fun getBoardState(): Array<Array<P?>>
.. method:: fun addPiece(coordinate: C, piece: P)
.. method:: fun removePiece(coordinate: C, piece: P)
.. method:: fun getPieces(): List<Pair<P, C>>
.. method:: fun getPieces(player: Player): List<Pair<P, C>>
.. method:: fun getPiece(coordinate: C): P?
.. method:: fun getPieceCoordinate(piece: P): C?