import curses

def game_loop(window):
    character = [10, 15]
    window.addch(character[0], character[1], 'O')
    while True:
        window.timeout(1000)
        char = window.getch()
        window.clear()
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
        window.addch(character[0], character[1], 'O')       


if __name__ == '__main__':
    curses.wrapper(game_loop)