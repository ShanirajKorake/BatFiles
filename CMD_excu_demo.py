import curses
import subprocess

def run_command(command):
    """Run shell command and return the output as string"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()

    stdscr.addstr(0, 0, "Enter command: ")
    curses.echo()
    cmd = stdscr.getstr(0, 15).decode()
    curses.noecho()

    stdscr.clear()
    stdscr.addstr(0, 0, f"$ {cmd}\n")
    
    output = run_command(cmd)
    lines = output.split('\n')

    for idx, line in enumerate(lines):
        if idx + 1 >= curses.LINES:
            break
        stdscr.addstr(idx + 1, 0, line[:curses.COLS - 1])

    stdscr.addstr(curses.LINES - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
