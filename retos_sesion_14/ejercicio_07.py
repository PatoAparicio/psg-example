print("Tres en Raya")
tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jugador_actual = "X"

def tres_en_raya(jugador, fila, columna):
    global tablero, jugador_actual
    
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera del rango (0-2)")
        return tablero
    
    if tablero[fila][columna] != ' ':
        print("Casilla ya está ocupada")
        return tablero
    
    tablero[fila][columna] = jugador
         
    if hay_ganador(jugador):
        print(f"¡Jugador {jugador} gana!")
        return tablero
    elif hay_empate():
        print("¡Empate!")
        return tablero
    else:
        jugador_actual = "O" if jugador == "X" else "X"
        
    return tablero

def hay_ganador(jugador):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True
    
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] == jugador:
            return True
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    
    return False

def hay_empate():
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

while True:
    print(f"\nTurno del jugador: {jugador_actual}")
    print("Tablero:")
    for fila_tablero in tablero:
        print(fila_tablero)
    
    fila = int(input("Ingresa la fila (0-2): "))
    columna = int(input("Ingresa la columna (0-2): "))
    tres_en_raya(jugador_actual, fila, columna)
    
    if hay_ganador("X") or hay_ganador("O") or hay_empate():
        print("\n¡Juego terminado!")
        break
        
  