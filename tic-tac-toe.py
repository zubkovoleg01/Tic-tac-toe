board = [['#', '#', '#'],
         ['#', '#', '#'],
         ['#', '#', '#']]

turn = 1

def check_win(board, symbol):
    if ((board[0][0] == board[0][1] == board[0][2] == symbol) or
        (board[1][0] == board[1][1] == board[1][2] == symbol) or
        (board[2][0] == board[2][1] == board[2][2] == symbol) or
        (board[0][0] == board[1][0] == board[2][0] == symbol) or
        (board[0][1] == board[1][1] == board[2][1] == symbol) or
        (board[0][2] == board[1][2] == board[2][2] == symbol) or
        (board[0][0] == board[1][1] == board[2][2] == symbol) or
        (board[0][2] == board[1][1] == board[2][0] == symbol)):
        return True
    return False

def make_turn(board, symbol):
    while True:
        try:
            row = int(input('Введите номер ряда (1-3): '))
            col = int(input('Введите номер столбца (1-3): '))
            if ((row in [1, 2, 3] and col in [1, 2, 3]) and
               board[row - 1][col - 1] == '#'):
                break
            else:
                print('Ошибка! Неверный ввод.')
        except ValueError:
            pass
    board[row - 1][col - 1] = symbol

def tic_tac_toe(board, turn):
    if turn > 9:
        print('Ничья!')
        return
    symbol = 'X' if turn % 2 == 1 else 'O'
    print(f'Ходят {symbol}. Ход: {turn}')
    [print(*row, sep='\t') for row in board]
    make_turn(board, symbol)
    if check_win(board, symbol):
        print(f'Победили {symbol}!')
        [print(*row, sep='\t') for row in board]
    else:
        tic_tac_toe(board, turn + 1)

tic_tac_toe(board, 1)