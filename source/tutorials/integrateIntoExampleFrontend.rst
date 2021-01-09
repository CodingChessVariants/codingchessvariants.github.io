****************************
Integrating Into a Frontend
****************************
The engine provides an interface to easily attach a frontend.

.. figure:: /../_static/images/chess-ingame.png
    :width: 70%

    Provided example front end

There is an example front end already implemented as part of the engine which can be adapted to account for any extensions or changes to the library.

For our variant, we can extend this example desktop front end to play our game.

Step 1: Add images for new pieces
-------------------------------------
The Berlin Pawn can use the same image as a standard pawn which is already included in the library.
The Alfil is usually represented as an elephant.

Navigate to the core.assets folder, and add these two images inside of it. Name them WhiteAlfil.png and BlackAlfil.png as appropriate.

.. figure:: /../_static/WhiteAlfil.png
    :width: 70%

    WhiteAlfil

.. figure:: /../_static/BlackAlfil.png
    :width: 70%

    BlackAlfil

Step 2: Map these images to textures
----------------------------------------
1. Navigate to core.src.com.mygdx.game.assets
2. In TextureAssets.kt, add new enums for the BlackAlfil and WhiteAlfil with a path to the image.

.. code-block:: kotlin

  enum class TextureAssets(val path: String) {
      
      ...

      WhiteAlfil("WhiteAlfil.png"),
      BlackAlfil("BlackAlfil.png")
  }

3. In Textures.kt, add new variables for the WhiteAlfil and BlackAlfil textures

.. code-block:: kotlin 

  val blackAlfil = assets[TextureAssets.BlackAlfil]
  val whiteAlfil = assets[TextureAssets.WhiteAlfil]

Step 3: Map textures to pieces
----------------------------------
1. Navigate to core.src.com.mygdx.game.assets.Textures.kt
2. In the 'whites' mapping, add the following mappings:

.. code-block:: kotlin 

  Alfil::class to whiteAlfil,
  BerlinWhitePawn::class to whitePawn,

3. In the 'blacks' mapping, add the following mappings:

.. code-block:: kotlin 

  Alfil::class to blackAlfil,
  BerlinBlackPawn::class to blackPawn,

Step 4: Add the button for the variant in the menu screen
------------------------------------------------------------
1. Navigate to core.src.screens.MenuScreen.
2. Add TutorialChess to the chessTypes mapping like so:

.. code-block:: kotlin
  :emphasize-lines: 13

  val chessTypes = mapOf(
    standardChessButton to StandardChess(),
    grandChessButton to GrandChess(),
    capablancaChessButton to CapablancaChess(),
    chess960Button to Chess960(),
    janggiButton to Janggi(),
    xiangqiButton to Xiangqi(),
    antiChessButton to AntiChess(),
    miniChessButton to MiniChess(),
    balbosGameButton to BalbosGame(),
    checkersGameButton to Checkers(),
    playgroundButton to ChessPlayground(),
    tutorialButton to TutorialChess()
  )

yay
-----------
Now when you start up the desktop applciation, you should be able to see an option for the variant you've created and be able to play it. 