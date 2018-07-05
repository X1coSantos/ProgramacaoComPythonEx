def tictactoe():

    def limpaScreem():
        print("\n"*1000)

    def board_inicial():
        return [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
         ]

    def win(board):
        if board[0][0] == board[1][0] == board[2][0] == "X": return True
        if board[0][1] == board[1][1] == board[2][1] == "X": return True
        if board[0][2] == board[1][2] == board[2][2] == "X": return True

        if board[0][0] == board[0][1] == board[0][2] == "X": return True
        if board[1][0] == board[1][1] == board[1][2] == "X": return True
        if board[2][0] == board[2][1] == board[2][2] == "X": return True

        if board[0][0] == board[1][1] == board[2][2] == "X": return True
        if board[0][2] == board[1][1] == board[2][0] == "X": return True

        if board[0][0] == board[1][0] == board[2][0] == "O": return True
        if board[0][1] == board[1][1] == board[2][1] == "O": return True
        if board[0][2] == board[1][2] == board[2][2] == "O": return True

        if board[0][0] == board[0][1] == board[0][2] == "O": return True
        if board[1][0] == board[1][1] == board[1][2] == "O": return True
        if board[2][0] == board[2][1] == board[2][2] == "O": return True

        if board[0][0] == board[1][1] == board[2][2] == "O": return True
        if board[0][2] == board[1][1] == board[2][0] == "O": return True

        return False

    def empate(board):
        livres = 9

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != " ": livres -= 1

        if livres <= 0:
            return True
        else: return False

    def mostra_board(board):
        for i in range(len(board)):
            for j in range(3):
                print(f"[{board[i][j]}]", end=" ")
            print()

    def set_jogador(player:int):
        if player == 1:
            return 2
        elif player == 2:
            return 1

    def set_jogada(board, jogador):

        if jogador == 1: simbolo = "X"
        elif jogador == 2: simbolo = "O"

        print(f"JOGADOR {jogador}")

        while True:
            try:

                    linha = int(input("linha: "))
                    coluna = int(input("Coluna: "))
                    if linha > 3 or coluna > 4:
                        raise ValueError("Linha ou coluna invalida")
                    if linha < 0 or coluna < 0:
                        raise ValueError("Linha ou coluna invalida")

                    if board[linha - 1][coluna - 1] != " ":
                        raise ValueError("Posição já ocupada")
                    else:
                        board[linha - 1][coluna - 1] = simbolo

                    break
            except Exception as e:
                print(e)

    def jogo(board):
        jogador = 1

        while win(board) == False and empate(board) == False:

            mostra_board(board)
            set_jogada(board, jogador)
            jogador = set_jogador(jogador)

            limpaScreem()
        else:
            mostra_board(board)
            if win(board):
                print(f"GANHOU {jogador}")
            else:
                print("EMPATE")

    board = board_inicial()
    jogo(board)

tictactoe()

