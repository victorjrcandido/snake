import curses

def game_loop(window):
    window.border(0)
    curses.curs_set(0)

    hight, width = window.getmaxyx()

    character = [10, 15]
    window.addch(character[0], character[1], 'O')
    while True:
        window.timeout(1000)
        char = window.getch()
        window.clear()
        window.border(0)
        match char:
            case curses.KEY_UP:
                character[0] -= 1
            case curses.KEY_DOWN:
                character[0] += 1
            case curses.KEY_LEFT:
                character[1] -= 1
            case curses.KEY_RIGHT:
                character[1] += 1
            case _:
                pass
        if (character[0] <= 0 or character[0] == hight-1 or
            character[1] <= 0 or character[1] == width-1):
            window.clear()
            return

        window.addch(character[0], character[1], 'O')


if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Game Over!')