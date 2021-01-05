****************************
Integrating Into a Frontend
****************************
The engine provides an interface to easily attach a frontend.

There is an example front end already implemented as part of the engine which can be adapted to account for any extensions or changes to the library.

For full details on the interface exposed by the game type, please look at the specific Engine API pages.

Game Management
================
Running a chess game is simple.

.. code-block:: kotlin

  val game = StandardChess()

  while (!game.isOver()) {
      val move = ...
      game.playerMakeMove(move)
  }

Attaching your own front end
=============================
  1. Creating a game type, for example StandardChess().

  2. You do not need a front-end player, but if you want to add further information such as usernames, colour of player etc., you may find it useful to add this. You can either use the pre-implemented front-end-player, or create your own. These can be mapped to the engine implementation of the players for ease of use.

  3. Call initGame() on the game instance once all the parameters have been set up.

  4. You can get the possible moves for a player like so: getValidMoves(player), and to trigger the engine to make a move, you can use playerMakeMove(move). The engine will change the turns of the players for you.

  5. You can check if a game is over by calling isOver(), and find the outcome (Stalemate, Checkmate, etc.) by calling GetOutCome(). 

The board, moveLog, backend players can be retrieved from the engine:
  1. Board: board field in GameType
  
  2. Players: players field in GameType
  
  3. Move Log: moveLog field in GameType
  
  4. Current player: Call getCurrentPlayer()
  
  5. Next Player: Call getNextPlayer()

It is easy to add metadata to the front end based on the interface provided, for example clock options (which have been implemented as demonstration). 

Extending the provided desktop front end
=========================================
You can add a game type you have created by adding a button for it into MenuScreen.kt.

Adding a game type:
^^^^^^^^^^^^^^^^^^^^
  1. In core.src.screens.MenuScreen.kt, create a button like so:

  .. code-block:: kotlin
    
    val sampleButton = TextButton("sample", skin)

    sampleButton.addListener(object : ChangeListener() {
      override fun changed(event: ChangeEvent?, actor: Actor?) {
          selectChessType(sampleButton)
      }
    })

  2. Add this button and your game type into the chessTypes map.

  
Adding a board:
^^^^^^^^^^^^^^^^
  1. If your board is a variation of the standard chess board (rectangular squares), or the Xiangqi board, then you can simple use boards that have already been implemented and skip to Step 3.
  2. Create a board that implements GUIBoard, and implement the method drawBoard().
  3. In GameScreen, map the board you require to your game type.

Adding images for newly created pieces:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  1. In core.assets, add the image for any new pieces.
  2. In core.src.com.mygdx.game.assets.TexttureAssets.kt, create a new enum using the path to the image you want.
  3. In core.src.com.mygdx.game.assets.Assets.kt, create a texture from the enum, and add the piece and texture to the piece mappings.

Extending the Console Frontend
===============================

TODO()