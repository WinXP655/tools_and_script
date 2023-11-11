import random

def generate_board(width, height, bombs):
    board = [[0 for _ in range(width)] for _ in range(height)]
    bomb_coords = random.sample(range(width * height), bombs)

    for bomb_coord in bomb_coords:
        row = bomb_coord // width
        col = bomb_coord % width
        board[row][col] = -1

        for i in range(max(0, row - 1), min(height, row + 2)):
            for j in range(max(0, col - 1), min(width, col + 2)):
                if board[i][j] != -1:
                    board[i][j] += 1

    return board

def display_board(board, reveal=False):
    for row in board:
        row_str = ''
        for cell in row:
            if cell == -1 and reveal:
                row_str += '* '
            elif cell == 0 or reveal:
                row_str += str(cell) + ' '
            else:
                row_str += '. '
        print(row_str)

def main():
    width = 8
    height = 8
    bombs = 10

    board = generate_board(width, height, bombs)
    display_board(board, reveal=True)

if __name__ == "__main__":
    main()