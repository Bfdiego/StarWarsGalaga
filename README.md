# Star Wars Galaga 

Este es un proyecto sencillo que hicimos usando la librería Arcade en Python. La idea fue recrear un juego al estilo clásico de Galaga, pero con temática de Star Wars.

- Descripción del Juego

El jugador controla una nave salida del universo de Star Wars (el Halcón Milenario), que puede moverse a la izquierda y derecha y disparar para destruir enemigos que bajan en oleadas, parecido al Galaga original.

Los enemigos son naves imperiales (TIE Fighters) que se mueven y no deben llegar al fondo de la pantalla. Además de la Estrella de la Muerte, que va atacando, se mueve y es el jefe final para ganar el juego. La dificultad va subiendo a medida que el jugador avanza.

- Tecnologías usadas

* Python 3
* Arcade (para gráficos y manejo del juego)

- Cómo correr el juego

1. Clonar el repositorio o descargar los archivos.
2. Instalar dependencias:

   pip install arcade pillow
   
3. Ejecutar el juego:

   python main.py

- Estructura básica del proyecto

* `bullets/`: carpeta que contiene la lógica de los disparos del jugador y la Estrella de la Muerte.
* `enemies/`: carpeta dedicada al jefe (Estrella de la Muerte) y las naves imperiales.
* `views/`: carpeta con todas las pantallas del juego.
* `main.py`: archivo principal donde arranca el juego.
* `player.py`: contiene la lógica de la nave del jugador.
* `assets/`: carpeta con las imágenes (sprites de naves, fondo, disparos, etc).
* `settings.py`: valores fijos que se usan en el proyecto. 

Controles

* Flecha izquierda/derecha → mover la nave.
* Espacio → disparar.

En este proyecto utilizamos arcade.schedule, una función que no se revisó en clases pero que resultó muy útil para manejar la lógica de actualización del juego en intervalos de tiempo definidos. Gracias a esto pudimos separar la lógica de dibujo de la lógica de actualización, manteniendo el código más ordenado y predecible. Además, aprovechamos el sistema de Views que ofrece Arcade (arcade.View) para estructurar las distintas pantallas del juego: una StartView (pantalla de inicio), una GameView (el juego en ejecución), una PauseView (pausa) y una GameOverView (pantalla final). Esta organización permitió una navegación clara entre estados y una experiencia de usuario más completa.