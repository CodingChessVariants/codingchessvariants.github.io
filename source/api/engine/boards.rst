**********************
Boards
**********************
.. code-block:: kotlin
   fun xd() {
    interface Board<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>
    fun getBoardState(): Array<Array<P?>>
   }
   
.. code-block:: kotlin
   :emphasize-lines: 3,5

   fun test() {
      val rows = piecePlacement.split("/")

      if (rows.size != board.rows) {
          throw IllegalArgumentException("Wrong number of rows in piece placement FEN. Expected: ${board.rows} Actual: ${rows.size}")
      }

      var y = board.rows - 1

      val whitePawnPromotions = pawnPromotions.map { it(player1) }
      val blackPawnPromotions = pawnPromotions.map { it(player2) }
   }

.. class:: interface Board<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>
.. method:: fun getBoardState(): Array<Array<P?>>
.. method:: fun addPiece(coordinate: C, piece: P)
.. method:: fun removePiece(coordinate: C, piece: P)
.. method:: fun getPieces(): List<Pair<P, C>>
.. method:: fun getPieces(player: Player): List<Pair<P, C>>
.. method:: fun getPiece(coordinate: C): P?
.. method:: fun getPieceCoordinate(piece: P): C?