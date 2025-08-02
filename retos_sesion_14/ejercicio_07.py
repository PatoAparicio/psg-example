print("Tres en Raya")
def tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"
    
    def imprimir_tablero():
        for fila in tablero:
            print("|".join(fila))
            print("-" * 5)
    
    def ganador():
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return True
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return True
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return True
        return False
    
    def empate():
        return all(" " not in fila for fila in tablero)
    
    while True:
        imprimir_tablero()
        print(f"Turno del jugador {jugador}")
        fila = int(input("Fila (0-2): "))
        col = int(input("Columna (0-2): "))
            
        if fila < 0 or fila > 2 or col < 0 or col > 2:
            print("Posición fuera del rango. Usa números del 0 al 2.")
            continue
            
        if tablero[fila][col] != " ":
            print("Casilla ocupada. Intenta de nuevo.")
            continue
           
        tablero[fila][col] = jugador
            
        if ganador():
            imprimir_tablero()
            print(f"¡Jugador {jugador} gana!")
            break
        elif empate():
            imprimir_tablero()
            print("¡Empate!")
        break
             
        jugador = "O" if jugador == "X" else "X"
            
tres_en_raya()
