**********************
Moves
**********************
Everything to do with move generators

.. class:: interface Move<B : Board<B, M, GM, P, C>, M : Move<B, M, GM, P, C>, GM: GameMove<B, M, GM, P, C>, P: Piece<B, M, GM, P, C>, C: Coordinate>

Represents a type of the movement of pieces.

For example, we use three types of moves to describe the movement of standard chess pieces:
    - Sliders - move along a ray direction until they encounter another piece or the edge of the board
    - Leapers - perform single steps to specified target squares
    - Steppers - perform single (repeated) steps in a particular board direction

.. function:: fun generate(board: B, coordinate: C, piece: P, player: Player): List<GM>

      Generates a list of corresponding game moves.