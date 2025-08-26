# Laberinto del Gato y el Ratón

## Descripción
"Laberinto del Gato y el Ratón" es un juego de tablero desarrollado en Python donde un jugador controla al gato o al ratón, mientras el otro se mueve automáticamente usando la lógica Minimax. El objetivo del ratón es alcanzar la salida del laberinto, mientras que el gato intenta atraparlo.

El tablero incluye casillas libres, paredes (infranqueables), la posición del gato, del ratón y la salida.

## Cómo jugar
1. Ejecuta el script en Python.
2. Al iniciar, elige tu personaje:
   - `C` para jugar como el **gato**
   - `R` para jugar como el **ratón**
3. Usa las teclas `W`, `A`, `S`, `D` para moverte:
   - `W` → Arriba
   - `S` → Abajo
   - `A` → Izquierda
   - `D` → Derecha
4. Presiona `Q` para salir del juego en cualquier momento.
5. Condiciones de victoria:
   - El **ratón** gana si llega a la salida.
   - El **gato** gana si atrapa al ratón.

## Tablero
- `C` → Gato  
- `R` → Ratón  
- `S` → Salida  
- `X` → Pared (no se puede pasar)  
- `.` → Casilla libre  

El tablero por defecto es de **5x5** y se pueden agregar paredes manualmente en el código.

## Lógica del juego
El juego utiliza la estrategia **Minimax** para el movimiento automático del gato o del ratón. Esto permite que el personaje controlado por la computadora tome decisiones optimizadas basadas en:
- La distancia entre el gato y el ratón.
- La distancia del ratón a la salida.

Se evalúa cada movimiento mediante funciones de puntuación para determinar la mejor acción posible en cada turno.

## Requisitos
- Python 3.x

No requiere librerías externas.

## Ejecución
1. Clona o descarga el repositorio.
2. Abre una terminal y navega hasta la carpeta del proyecto.
3. Ejecuta el juego con:
   ```bash
   python minimax_lab.py
