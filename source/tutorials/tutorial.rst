**********************************
Tutorial
**********************************

Here we will demonstrate the steps for creating this chess variant.

Step 1. Create the Fairy Pieces (new pieces)
-----------------------------------------------------------
  a. Navigate to engine.src.main.kotlin.pieces
  
  b. Create a new package called "tutorial"

  c. 

1. Create the fairy pieces
2. Initialise the game, and set up the board
3. 
  
Step 2: Add a new Game type
----------------------------
In GameTypes, add your new chess variant. This should take in a list of rules and a list of win conditions.

  a. You variant can implement a more generic AbstractChess.
  
  b. Or it can implement a more specific chess variant from StandardChess. You can use this if you are using a 2D board, has standard castling rules, en passant, has promotable pieces, and standard win conditions.

Implement the initGame() method.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The initGame method should initialise the board.
  a. If your game implements StandardChess, you can use FEN notation to set up the game in the class declaration, like so:
  
    .. code-block:: kotlin

      class sampleChess() : StandardChess(FenUtility("rqkr/pppp/PPPP/RQKR w -", whiteStartingRow = 1, whitePromotionRow = 3, blackStartingRow = 2, blackPromotionRow = 0))
      
    And the initGame() method should look like this:

    .. code-block:: kotlin

      override fun initGame() {
          val player1 = players[0]
          val player2 = players[1]
          fen.initBoardWithFEN(board, player1, player2)
      }

  b. If your game implements AbstractChess, you must manually add each piece to the board by it's position, like so:
  
    .. code-block:: kotlin

      override fun initGame() {
          val player1 = players[0]
          val player2 = players[1]
          for (i in 0..9) {
              board.addPiece(Coordinate2D(i, 2), GrandWhitePawn(player1))
              board.addPiece(Coordinate2D(i, 7), GrandBlackPawn(player2))
          }
          board.addPiece(Coordinate2D(0, 0), Rook(player1))

          ...
        }

Step 3: Add the frontend
--------------------------
- Desktop: Integrate your own frontend or extend the existing front end to accomadate your new variant.
- Console: Extend the console front end to play your variant in the console. 