#coordenadas del gato, el raton, y la salida. Posicion en la matriz (fila, columna)
gato = (0,0)
raton = (4,4)
salida = (3,0)


class Tablero: #clase que contiene el campo de juego, los obstaculos y muestra a los personajes y la salida
    def __init__(self, filas, columnas, salida):
        self.filas = filas
        self.columnas = columnas
        self.salida = salida  #posicion de la salida
        self.paredes = set()  #casillas bloqueadas/infranqueables #investigar

    def agregar_pared(self, fila, columna): #metodo/accion
        #agrega una pared en la posición indicada
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.paredes.add((fila, columna))

    def mostrar(self, gato, raton):
        #muestra el tablero con el gato, el raton, la salida y paredes
        for i in range(self.filas): #recorre todas las filas
            fila = ''
            for j in range(self.columnas): #recorre todas las colummnas
                if (i, j) == gato:
                    fila += ' C '  #imprime C en donde esta el gato
                elif (i, j) == raton:
                    fila += ' R '  #imprime R en donde esta el raton
                elif (i, j) == self.salida:
                    fila += ' S '  #imprime S en donde esta la salida
                elif (i, j) in self.paredes:
                    fila += ' X '  #imprime X en las casillas que no se pueden pasar
                else:
                    fila += ' . ' #imprime un punto si no hay nadie en esa posicion
            print(fila)
        print()

    def movimientos_validos(self, posicion):
        fila, columna = posicion
        posibles = [(fila+1, columna), (fila-1, columna), (fila, columna+1), (fila, columna-1)]
        return [(f, c) for f, c in posibles if 0 <= f < self.filas and 0 <= c < self.columnas and (f, c) not in self.paredes]

tablero = Tablero(5,5,salida) #instanciar un objeto/ crear un objeto utilizando la clase
tablero.agregar_pared(1,3) #agrega una pared en la fila 2, columna 3
tablero.agregar_pared(4,1) #agrega una pared en la fila 4, columna 1

def mover_raton_jugador(raton, comando): #permite al raton moverse entre filas y columnas
    fila, columna = raton
    nueva_fila, nueva_columna = fila, columna
    if comando == 'w' and fila > 0:
        nueva_fila -= 1 #mueve una posicion hacia arriba
    elif comando == 's' and fila < 4:
        nueva_fila += 1 #mueve una posicion hacia abajo
    elif comando == 'a' and columna > 0:
        nueva_columna -= 1 #mueve una posicion hacia la izquierda
    elif comando == 'd' and columna < 4:
        nueva_columna += 1 #mueve una posicion hacia la derecha
    
    if (nueva_fila, nueva_columna) not in tablero.paredes: #detecta si el raton intenta entrar a casillas bloqueadas
        return (nueva_fila, nueva_columna) #en caso de que la casilla sea franqueable, se mueve a esa posicion
    else:
        return (fila, columna) #en caso de que la casilla sea infranqueable, no puede avanzar a ella

def mover_gato_jugador(gato, comando): #permite al gato moverse entre filas y columnas
    fila, columna = gato
    nueva_fila, nueva_columna = fila, columna
    if comando == 'w' and fila > 0:
        nueva_fila -= 1 #mueve una posicion hacia arriba
    elif comando == 's' and fila < 4:
        nueva_fila += 1 #mueve una posicion hacia abajo
    elif comando == 'a' and columna > 0:
        nueva_columna -= 1 #mueve una posicion hacia la izquierda
    elif comando == 'd' and columna < 4:
        nueva_columna += 1 #mueve una posicion hacia la derecha
    
    if (nueva_fila, nueva_columna) not in tablero.paredes: #detecta si el raton intenta entrar a casillas bloqueadas
        return (nueva_fila, nueva_columna) #en caso de que la casilla sea franqueable, se mueve a esa posicion
    else:
        return (fila, columna) #en caso de que la casilla sea infranqueable, no puede avanzar a ella

def distancia(gato, raton):
    return abs(gato[0] - raton[0]) + abs(gato[1] - raton[1]) #elementos de la tupla

def evaluar(gato, raton, tablero):
    #si el raton gana
    if raton == tablero.salida:
        return float('inf')
    #si el gato gana
    if gato == raton:
        return -float('inf')

    #cuanto mas lejos este del gato y mas cerca de la salida, mejor
    dist_gato = abs(gato[0] - raton[0]) + abs(gato[1] - raton[1])
    dist_salida = abs(tablero.salida[0] - raton[0]) + abs(tablero.salida[1] - raton[1])

    return dist_gato - dist_salida

def minimax_raton(gato, raton, tablero, profundidad, maximizador=True):
    if profundidad == 0 or gato == raton or raton == tablero.salida:
        return evaluar(gato, raton, tablero)

    if maximizador:  #turno del ratón
        mejor = -float('inf')
        for mov in tablero.movimientos_validos(raton):
            puntaje = minimax_raton(gato, mov, tablero, profundidad-1, False) #recursion
            mejor = max(mejor, puntaje)
        return mejor
    else:  #turno del gato
        mejor = float("inf")
        nuevo_gato = mover_gato_minimax(gato, raton, tablero)
        puntaje = minimax_raton(nuevo_gato, raton, tablero, profundidad-1, True)
        mejor = min(mejor, puntaje)
        return mejor

def mover_raton_minimax(gato, raton, tablero, profundidad=2):
    mejor_puntaje = -float("inf")
    mejor_mov = raton

    for mov in tablero.movimientos_validos(raton):
        puntaje = minimax_raton(gato, mov, tablero, profundidad-1, False)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_mov = mov
    return mejor_mov

def evaluar_gato(gato, raton, tablero):
    if gato == raton: #gato atrapa al raton
        return float('inf')
    if raton == tablero.salida: #raton escapa
        return -float('inf')
    #cuanto mas cerca del raton y cuanto mas lejos de la salida, mejor
    dist_gato = abs(gato[0] - raton[0]) + abs(gato[1] - raton[1])
    dist_salida = abs(tablero.salida[0] - raton[0]) + abs(tablero.salida[1] - raton[1])
    return -dist_gato + dist_salida

def minimax_gato(gato, raton, tablero, profundidad, maximizador=True):
    if profundidad == 0 or gato == raton or raton == tablero.salida:
        return evaluar_gato(gato, raton, tablero)

    if maximizador: #turno del gato
        mejor = -float('inf')
        for mov in tablero.movimientos_validos(gato):
            puntaje = minimax_gato(mov, raton, tablero, profundidad-1, False)
            mejor = max(mejor, puntaje)
        return mejor
    else: #turno del raton
        mejor = float('inf')
        for mov in tablero.movimientos_validos(raton):
            puntaje = minimax_gato(gato, mov, tablero, profundidad-1, True)
            mejor = min(mejor, puntaje)
        return mejor

def mover_gato_minimax(gato, raton, tablero, profundidad=2):
    mejor_puntaje = -float('inf')
    mejor_mov = gato
    for mov in tablero.movimientos_validos(gato):
        puntaje = minimax_gato(mov, raton, tablero, profundidad-1, False)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_mov = mov
    return mejor_mov


personaje_jugador = input('Pulsar C para jugar como el gato o R para jugar como el raton').upper()

while True:
    tablero.mostrar(gato, raton)
    comando = input('WASD para mover, Q para salir: ').lower().strip()

    if comando == 'q': #la letra q detiene el juego
        break

    if personaje_jugador == 'R': #si el jugador elige al raton, el gato se mueve solo
        raton = mover_raton_jugador(raton, comando)
        gato = mover_gato_minimax(gato, raton, tablero)
    elif personaje_jugador == 'C': #si el jugador elige al gato, el raton se mueve solo
        gato = mover_gato_jugador(gato, comando)
        raton = mover_raton_minimax(gato, raton, tablero)

    if personaje_jugador == 'R':
        if gato == raton: #si el gato alcanza al raton se acaba la partida
            print('game over')
            break
        if raton == salida: #si el raton alcanza la salida, este gana
            print('ganaste')
            break

    if personaje_jugador == 'C':
        if gato == raton: #si el gato alcanza al raton, este gana
            print('ganaste')
            break
        if raton == salida: #si el raton alcanza la salida se acaba la partida
            print('game over')
            break