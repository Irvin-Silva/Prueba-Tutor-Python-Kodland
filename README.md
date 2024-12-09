# Flappy Bird en Python - Pygame

Este proyecto es una implementación del popular juego *Flappy Bird* usando Pygame, un módulo de Python para el desarrollo de videojuegos. En este juego, controlas un pájaro que debe evitar los tubos que se mueven hacia él mientras navega por la pantalla. El objetivo es sobrevivir el mayor tiempo posible y obtener la mejor puntuación.

## Características principales

- **Control del pájaro**: Utiliza la tecla `ESPACIO` para hacer que el pájaro salte. La gravedad lo hará caer automáticamente, pero presionar la tecla hace que el pájaro suba.
  
- **Tubos**: Los tubos aparecen aleatoriamente y se desplazan de derecha a izquierda. Deberás esquivarlos para evitar perder el juego. La distancia entre los tubos también varía para aumentar el desafío.

- **Suelo en movimiento**: El suelo se mueve constantemente hacia la izquierda, creando una sensación de desplazamiento. También es necesario evitar chocar con él.

- **Puntuación**: Tu puntuación aumenta cada vez que el pájaro pasa con éxito entre los tubos. La puntuación se muestra en la parte superior de la pantalla.

- **Pantalla de Game Over**: Si el pájaro choca contra un tubo o el suelo, el juego termina y se muestra una pantalla con tu puntuación actual y la puntuación más alta alcanzada.

- **Incremento de dificultad**: Con cada 10 puntos, la velocidad del juego aumenta, haciendo que los tubos y el suelo se desplacen más rápido.

- **Opción de Pausa**: El juego se puede pausar en cualquier momento presionando la tecla `P`, incluso antes de que comience el juego.

## Instrucciones

### Iniciar el juego:
- Haz clic en cualquier parte de la pantalla para iniciar el juego. Después de una breve cuenta regresiva, podrás controlar al pájaro usando la tecla `ESPACIO`.

### Controlar el pájaro:
- Usa la tecla `ESPACIO` para hacer que el pájaro suba. El pájaro caerá debido a la gravedad cuando no se presione ninguna tecla.

### Evitar los tubos:
- Los tubos se generan aleatoriamente y se mueven de derecha a izquierda. Para evitar chocar con ellos, debes mover al pájaro hacia arriba o hacia abajo presionando `ESPACIO`.

### Pausar el juego:
- Puedes pausar el juego en cualquier momento presionando la tecla `P`. Para reanudar el juego, simplemente presiona `P` nuevamente.

### Fin del juego:
- El juego termina cuando el pájaro colisiona con un tubo o con el suelo. Después de que termine el juego, verás la pantalla de "Game Over", donde podrás ver tu puntuación y la más alta alcanzada. Para reiniciar el juego, presiona cualquier tecla.

## Requisitos

Antes de ejecutar el juego, asegúrate de tener **Pygame** instalado. Puedes instalarlo con el siguiente comando:

pip install pygame

Además, necesitarás las imágenes y sonidos correspondientes en el directorio `assets/` para que el juego funcione correctamente. Asegúrate de tener las siguientes imágenes y archivos de sonido:

- `assets/bluebird-upflap.png` (Pájaro, flap hacia arriba)
- `assets/bluebird-midflap.png` (Pájaro, flap medio)
- `assets/bluebird-downflap.png` (Pájaro, flap hacia abajo)
- `assets/pipe-red.png` (Tubos)
- `assets/floor.png` (Suelo)
- `assets/background-day.png` (Fondo)
- `assets/game.wav` (Música de fondo)
- `assets/hit.wav` (Sonido de colisión)

## Características adicionales

- **Cuenta regresiva de inicio**: El juego comienza con una cuenta regresiva de 3 segundos, permitiéndote prepararte antes de que inicie la acción.
  
- **Puntuación más alta**: El juego guarda tu puntuación más alta para que puedas intentar superarla en cada partida.

## ¿Cómo jugar?

1. **Haz clic para iniciar**: Al hacer clic en la pantalla, el juego comienza con una cuenta regresiva.
2. **Controla el pájaro**: Presiona la tecla `ESPACIO` para hacer que el pájaro salte.
3. **Esquiva los tubos**: Usa `ESPACIO` para mover el pájaro hacia arriba y esquivar los tubos que se mueven hacia ti.
4. **Evita el suelo**: Asegúrate de no tocar el suelo, ya que esto también terminará el juego.
5. **Puntuación**: Cada vez que el pájaro pase con éxito entre los tubos, tu puntuación aumentará. ¡Trata de alcanzar la puntuación más alta!

## ¡Diviértete!

¡Intenta batir tu récord y disfruta del juego! 🐦🎮
