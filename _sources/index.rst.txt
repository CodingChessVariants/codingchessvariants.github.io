===========================
Coding Chess Variants
===========================

Coding Chess Variants is a Kotlin chess library used to easily create a wide range of different chess variants.
It is intended to be used by both for beginner programmers and for those who are more experience and are looking for a framework to develop different chess-based games.
It can be easily integrated with different chess frontends including those which support networking.

.. figure:: /_static/images/chess-ingame.png

    :width: 60%

Features
========================
The library was designed for extendability and adaptablity.
It is possible to create a large range of interesting and unique variants using the library.

Features of our library include:

- Adaptable board: The board used in the variant is not limited to a rectangular board, but can be in higher dimensions, or a non-rectangular board such as a hexagon.

- Simple Piece Creation: The library provides a simple abstraction for adding new fairy pieces, that have unique movement rules.

- Simple, yet powerful Move Generators: Complex and simple moves are easy to implement using the clear abstraction the library gives.

In addition, the library has support for FEN notation, and an example desktop application and console application.

As part of the core codebase, KChess provides 12 different variants by default which are readily playable including both Western and East Asian chess variants, as well as 3D and Hexagonal chess games.
Their components are all completely reusable, so all the implemented pieces and rules from these variants can be used in new variants.

.. toctree::
    :maxdepth: 2
    :caption: Getting Started

    self
    gettingStarted/installation
    gettingStarted/developerSetup
    gettingStarted/supportedVariants
    gettingStarted/quickstart

.. toctree::
    :maxdepth: 2
    :caption: Tutorials
    
    tutorials/tutorialIntroduction
    tutorials/creatingNewPieces
    tutorials/initGame
    tutorials/creatingBoards
    tutorials/creatingRules
    tutorials/creatingWinConditions
    tutorials/finaliseGame
    tutorials/integrateIntoExampleFrontend

.. toctree::
    :maxdepth: 2
    :caption: Engine API

    api/engine/boards
    api/engine/coordinates
    api/engine/moves
    api/engine/gameTypes
    api/engine/moveGenerators
    api/engine/pieces
    api/engine/players
    api/engine/utils
    api/engine/api

.. .. toctree::
..     :maxdepth: 2
..     :caption: Demo

..     demo2/variants

.. .. toctree::
..     :maxdepth: 2
..     :caption: Demo Reference

..     demo/api
..     demo/demo
..     demo/lists_tables
..     demo/structure
