================================
Initialise the game variant
================================

In the tutorials package you have created, create a file called TutorialChess.kt
Create an open class called "TutorialChess" that implements the AbstractChess2D interface. We will initialise the board and implement initBoard in the next step.

.. code-block:: kotlin

  open class TutorialChess : AbstractChess2D(
                                    listOf(),
                                    listOf()
  {
    override val board: Board2D = TODO()
    override val name = "Tutorial Chess"

    override fun initBoard() {
        TODO()
    }
  }

Leave the parameters for AbstractChess2D as empty lists for now - These parameters will later be the special rules and win conditions for our variant.