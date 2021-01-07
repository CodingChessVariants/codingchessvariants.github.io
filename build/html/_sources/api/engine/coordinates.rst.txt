**********************
Coordinates
**********************
Everything to do with coordinates

Coordinate
==========

.. class:: interface Coordinate
Marker interface to represent coordinates on a board

Coordinate2D
============

.. class:: data class Coordinate2D(val x: Int, val y: Int) : Coordinate
Coordinate on a 2D board representing the x,y offset from the bottomleft of the board

.. Important:: Coordinate2D are 0 indexed for both x and y.