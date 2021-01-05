**********************
Creating New Pieces
**********************

Creating pieces requires you to also provide the moves it can make, excluding special rules which are evaluated later.

Step 1: Implement the Piece interface
=======================================
  1. If your game is 2D and uses a rectangular board, then implement the Piece2D interface
  2. Otherwise, create a new interface that implements Piece with the appropriate board, coordinates, and moves.
  3. If your piece is a Pawn or a King, then it should further implement the Pawn or King marker interfaces.

Step 2: Implement the methods
================================

Option 1: (If your piece is a standard pawn)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Your piece is a standard pawn if:
   - The game is 2D
   - It can double move on it's first turn
   - It pawn can usually only step once northwards-ly
   - It can promote
   - Can only capture north-diagonally.

In this case, you can directly implement the WhitePawn class, and set custom settings for the starting row, promotion region, and the list of pieces it can promote to.

Option 2: Otherwise
^^^^^^^^^^^^^^^^^^^^^
You must a give a list of moves the piece can do in moveTypes. Please look at the Engine API pages for Moves for further details.
For example, the standard Rook gives this as their moveTypes:

.. code-block:: kotlin
  
  override val moveTypes: List<Move2D>
        get() = listOf(Move2D.Slider(H = true, V = true, A = false, D = false))

This describes the rook's movements as a slider that can only move horizontally or vertically.


For a more complicated example, WhitePawn gives this as their moveTypes:

.. code-block:: kotlin

  override val moveTypes: List<Move2D> = listOf(
          Move2D.Restricted(Move2D.Stepper(Direction.NORTH, 2), RowRegion(startingRow)),
          Move2D.AddPromotion(
              listOf(
                  Move2D.Stepper(Direction.NORTH, 1),
                  Move2D.CaptureOnly(Move2D.Stepper(Direction.NORTH_EAST, 1, true)),
                  Move2D.CaptureOnly(Move2D.Stepper(Direction.NORTH_WEST, 1, true)),
              ),
              promotionRegion,
              pawnPromotions,
              true
          ),

The first move represents that a pawn can move 2 steps north when it starts in it's starting row.
The next moves are wrapped in AddPromotion, meaning these moves can result in promotion if they move into the PromotionRegion.
These moves describe pawn moves for stepping north once, and for capturing in both north diagonals.

The special rule, En Passant, is given later as a special rule.

You should also provide a symbol representation for your piece. These do not need to be unique.

Step 3: Special Rules
========================
Special rules are 'special' because they can only occur under certain conditions. If your piece has a special rule, please look at the tutorial section for creating special rules.
