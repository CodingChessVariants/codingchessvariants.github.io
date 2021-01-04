===========================
Coding Chess Variants
===========================

Coding Chess Variants is a Kotlin chess library used to easily create a wide range of different chess variants.
It is intended to be used by both for beginner programmers and for those who are more experience and are looking for a framework to develop different chess-based games.
It can be easily integrated with different chess frontends including those which support networking.

Features
========================
    - Feature 1 - xd
    - Feature 2 - xd
    - Feature 3 - xd


Inline markup in reStructuredText is pretty powerful. You can have *emphasis*,
**strong emphasis**, ``inline literals``, external hyperlinks with embedded
URIs (`Python web site <http://www.python.org>`__) standalone hyperlinks
(http://www.python.org), footnote references [1]_ and so much more. Sometimes,
you even have some |problematic| text that doesn't do the right things but
Sphinx still builds your page.

Often, you'll have multiple paragraphs of text in your documentation, possibly
an explanation how stuff works. Here are some explicit interpreted text roles:
a PEP reference (:PEP:`287`); a :sub:`subscript`; a :sup:`superscript`; and
explicit roles for :emphasis:`standard` :strong:`inline` :literal:`markup`.

.. note::
    You may want to know what admonitions look like.

.. important::
    I just wanted to interrupt your very relevant insight, to assert my
    importance.

Or, maybe, you want to present a code block to the user.

.. code-block:: python
    :linenos:
    :emphasize-lines: 6,9

    """Just a small code example"""

    class Demo:
        def __init__(self):
            super().__init__()
            self.ready = True

        def how_ready_are_we(self) -> str:
            return "very" if self.ready else "not at all"

.. toctree::
    :maxdepth: 2
    :caption: Getting Started

    self
    gettingStarted/installation
    gettingStarted/quickstart

.. toctree::
    :maxdepth: 2
    :caption: Tutorials

    tutorials/tutorial
    tutorials/integrateIntoExampleFrontend
    tutorials/creatingNewPieces
    tutorials/creatingDifferentRules
    tutorials/creatingDifferentWinConditions
    tutorials/integrateIntoExampleFrontend

.. toctree::
    :maxdepth: 2
    :caption: Engine API

    api/engine/boards
    api/engine/coordinates
    api/engine/gameMoves
    api/engine/gameTypes
    api/engine/moves
    api/engine/pieces
    api/engine/players
    api/engine/utils

.. toctree::
    :maxdepth: 2
    :caption: Demo Reference

    demo/api
    demo/demo
    demo/lists_tables
    demo/structure
