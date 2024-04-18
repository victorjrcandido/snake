import curses

def game_loop(window):
    window.addstr(f'Aperte uma tecla')
    while True:
        window.timeout(1000)
        char = window.getch()
        window.clear()
        if char != -1:
            window.addstr(f'Tecla Pressionada: {char}')
        else:
            window.addstr(f'Nenhuma tecla pressionada')


if __name__ == '__main__':
    curses.wrapper(game_loop)