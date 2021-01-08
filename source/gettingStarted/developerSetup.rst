**********************
Developer Setup
**********************
Prerequisites - JDK 8+ installed

Using The Engine With Our Frontend
======================================
Download the KChess project here and unzip it.

.. code:: bash

  # Building everything and running all tests
  ./gradlew build

  # Creating jar file to distribute the desktop application (desktop/build/libs/desktopclient.jar)
  ./gradlew :desktop:dist

  # Creating jar file to distribute the console application (console/build/libs/consoleclient.jar)
  ./gradlew :console:shadowJar

  # Creating jar file to distribute the engine to integrate with other frontends (engine/build/libs/chessengine.jar)
  ./gradlew :engine:shadowJar

  # Creating jar file to run the desktop server (server/build/libs/server.jar)
  ./gradlew :server:shadowJar

Using The Engine For Your Own Projects
======================================
Download the core engine jar here and configure your project to use the library.
