import curses
import random
import time

dificulty = int(input("Enter dificulty - 1 - easy, 2 - medium, 3 - hard: "))

def game_loop(window):
    curses.curs_set(0)
    snake = [[10, 15], [10, 14], [10, 13], [10, 12]]
    current_direction = curses.KEY_RIGHT
    fruit = get_new_fruit(window=window)
    playing = True
    score = 0

    while playing:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_fruit(fruit=fruit, window=window)
        match dificulty:
            case 1:
                direction = get_new_direction(window=window, timeout=1000)
            case 2:
                direction = get_new_direction(window=window, timeout=40)
            case 3:
                direction = get_new_direction(window=window, timeout=5)

        if direction is None:
            direction = current_direction
        elif direction_is_opposite(direction=direction, current_direction=current_direction):
            direction = current_direction
        move_snake(snake=snake, direction=direction)
        current_direction = direction       
        if snake_hit_border(snake=snake, window=window):
            break 
        if snake_hit_fruit(snake=snake, fruit=fruit):
            fruit = get_new_fruit(window=window)
            score += 10
            grow_snake(snake=snake)
        if snake_hit_self(snake=snake):
            break
            
    game_over(window=window, score=score)

def game_over(window, score):
    draw_screen(window=window)
    s = f'Game over! Score {score}!'
    x = 1
    y = 1
    window.addstr(y, x, s)
    window.refresh()
    time.sleep(2)
        
def snake_hit_self(snake):
    head = snake[0]
    body = snake[1:]
    if head in body:
        return True

def grow_snake(snake):
    tail = snake[-1].copy()
    snake.append(tail)

def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height-2), random.randint(1, width-2)]

def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
        return direction
    return None

def direction_is_opposite(direction, current_direction):
    match direction:
        case curses.KEY_UP:
            return current_direction == curses.KEY_DOWN
        case curses.KEY_LEFT:
            return current_direction == curses.KEY_RIGHT
        case curses.KEY_DOWN:
            return current_direction == curses.KEY_UP
        case curses.KEY_RIGHT:
            return current_direction == curses.KEY_LEFT

def move_snake(snake, direction):
    head = snake[0].copy()
    snake.insert(0, head)
    move_character(character=head, direction=direction)
    snake.pop()

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

def snake_hit_border(snake, window):
    head = snake[0]
    return character_hit_border(character=head, window=window)

def snake_hit_fruit(snake, fruit):
    return fruit in snake
    
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

def draw_snake(snake, window):
    head = snake[0]
    body = snake[1:]
    draw_character(character=head, window=window, char="@")
    for body_part in body:
        draw_character(character=body_part, window=window, char="s")

def draw_fruit(fruit ,window):
    draw_character(character=fruit, window=window, char="#")        

def draw_character(character, window, char):
    window.addch(character[0], character[1], char)

if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Game Over!')