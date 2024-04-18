import curses

def game_loop(window):
    curses.curs_set(0)
    player = [10, 15]

    while True:
        draw_screen(window=window)
        draw_character(character=player, window=window)
        direction = get_new_direction(window=window, timeout=1000)
        if direction is not None:
            move_character(character=player, direction=direction)
        if character_hit_border(character=player, window=window):
            return


def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
        return direction
    return None


def move_character(character, direction):
    match direction:
        case curses.KEY_UP:
            character[0] -= 1
        case curses.KEY_DOWN:
            character[0] += 1
        case curses.KEY_LEFT:
            character[1] -= 1
        case curses.KEY_RIGHT:
            character[1] += 1


def character_hit_border(character, window):
    height, width = window.getmaxyx()
    # EIXO VERTICAL
    if (character[0] <= 0) or (character[0] >= (height - 1)):
        return True
    # EIXO HORIZONTAL
    if (character[1] <= 0) or (character[1] >= (width - 1)):
        return True
    return False

def draw_screen(window):
    window.clear()
    window.border(0)

def draw_character(character, window):
    window.addch(character[0], character[1], 'O')

if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Game Over!')