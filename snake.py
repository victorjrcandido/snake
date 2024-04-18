import curses

def game_loop(window):
    window.addstr(f'Aperte uma tecla')
    while True:
        char = window.getch()
        window.addstr(f'Tecla Pressionada: {char}')

if __name__ == '__main__':
    curses.wrapper(game_loop)