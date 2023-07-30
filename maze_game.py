# import curses

def create_maze():
    return [
        "##########",
        "#        #",
        "#  #  G  #",
        "#  #     #",
        "#  #  ## #",
        "#  #  ## #",
        "#  #     #",
        "#  P     #",
        "#        #",
        "##########"
    ]

def move_player(maze, y, x, dy, dx):
    new_y, new_x = y + dy, x + dx
    if maze[new_y][new_x] != "#":
        maze[y] = maze[y][:x] + " " + maze[y][x + 1:]
        maze[new_y] = maze[new_y][:new_x] + "P" + maze[new_y][new_x + 1:]
        return new_y, new_x
    return y, x

def draw_maze(stdscr, maze):
    stdscr.clear()
    for y, row in enumerate(maze):
        stdscr.addstr(y, 0, row)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    maze = create_maze()
    y, x = 7, 2  # Starting position of the player

    while True:
        draw_maze(stdscr, maze)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            y, x = move_player(maze, y, x, -1, 0)
        elif key == curses.KEY_DOWN:
            y, x = move_player(maze, y, x, 1, 0)
        elif key == curses.KEY_LEFT:
            y, x = move_player(maze, y, x, 0, -1)
        elif key == curses.KEY_RIGHT:
            y, x = move_player(maze, y, x, 0, 1)
        elif key == 27:  # ASCII value of 'ESC' key
            break

        if maze[y][x] == 'G':
            draw_maze(stdscr, maze)
            stdscr.addstr(len(maze), 0, "Congratulations! You reached the goal!")
            stdscr.refresh()
            stdscr.getch()
            break

if __name__ == "__main__":
   #pythonpython curses.wrapper(main)
