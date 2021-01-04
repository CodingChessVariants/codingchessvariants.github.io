**********************
Utils
**********************

This is a list of utils we made

FENUtility
==========

Forsyth–Edwards Notation (FEN) is a standard notation for describing a particular board position of a chess game.

Our shortened FEN notation takes 3 fields:

1. Piece placement

2. Active colour

3. Castling Availibilty

For example a valid FEN string for standard chess would be "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"

.. class:: class FenUtility(val FENstring: String)

Optional parameters:
    ``Int whiteStartingRow`` - the starting row of the white pawn from which they can move 2 steps

    ``Int whitePromotionRow`` - the row at which the white pawn will be promoted 

    ``Int blackStartingRow`` - the starting row of the white pawn from which they can move 2 steps

    ``Int blackPromotionRow`` - the row at which the white pawn will be promoted

    ``List<KFunction1<Player, Piece2D>> pawnPromotions`` - a list of pieces a pawn can be promoted to 

.. function:: fun initBoardWithFEN(board: Board2D, player1: Player, player2: Player)

Takes a board and initialises it with the FENstring's piece placement. Throws ``IllegalArgumentException`` if the piece placement does not fit the size of the board.


ChessNotationInput
==================

This is about ChessNotationInput 