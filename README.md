# Star Wars Galaga 

Este es un proyecto sencillo que hicimos usando la librería Arcade en Python. La idea fue recrear un juego al estilo clásico de Galaga, pero con temática de Star Wars.

- Descripción del Juego

El jugador controla una nave inspirada en el universo de Star Wars (como un X-Wing), que puede moverse a la izquierda y derecha y disparar para destruir enemigos que bajan en oleadas, parecido al Galaga original.

Los enemigos son naves imperiales (por ejemplo, TIE Fighters) que se mueven y atacan. La dificultad va subiendo a medida que el jugador avanza.

- Tecnologías usadas

* Python 3
* Arcade (para gráficos y manejo del juego)
* PIL (para manejo básico de imágenes)

- Cómo correr el juego

1. Clonar el repositorio o descargar los archivos.
2. Instalar dependencias:

   pip install arcade pillow
   
3. Ejecutar el juego:

   python main.py

- Estructura básica del proyecto

* `main.py`: archivo principal donde arranca el juego.
* `player.py`: contiene la lógica de la nave del jugador.
* `enemy.py`: contiene la lógica de los enemigos.
* `assets/`: carpeta con las imágenes (sprites de naves, fondo, disparos, etc).

Controles

* Flecha izquierda/derecha → mover la nave.
* Espacio → disparar.