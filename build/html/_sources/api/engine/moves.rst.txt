**********************
Moves
**********************
Everything to do with move generators

Move
====
.. class:: interface Move<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>

Represents a type of the movement of pieces.

For example, we use four types of moves to describe the movement of standard chess pieces:
    - Sliders - move along a ray direction until they encounter another piece or the edge of the board
    - Leapers - perform single steps to specified target squares
    - Steppers - perform single (repeated) steps in a particular board direction
    - Hoppers - can move along a ray direction, but must jump over another piece.

We also use the following conditions as wrappers to describe moves:
    - CaptureOnly - move can only occur if it captures a piece
    - NoCapture - move can only occur if it doesn't capture a piece
    - Restricted - move can only occur when the piece starts in a specific region
    - RestrictedDestination - move can only occur if the destination is within a specific region
    - Composite - This is a wrapper around a list of basic moves to represent composite moves.

To add moves which could result in promotion, we use the 'AddPromotion' wrapper which takes in a list of moves which can results in promotion.

We also include a special move 'Skip' to skip moves, as in Janggi.

Methods
-------

.. function:: fun generate(board: B, coordinate: C, piece: P, player: Player): List<GM>

      Generates a list of corresponding game moves.

Region
========
.. class:: interface Region

Represents a region on the board.

Methods
--------

.. function:: fun isInRegion(coordinate: Coordinate2D): Boolean
    Returns true, if the coordinate is within the region specified. Otherwise returns false.