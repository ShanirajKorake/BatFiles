import os
import curses

def list_files(stdscr, path="."):
    curses.curs_set(0)
    stdscr.clear()
    files = os.listdir(path)
    index = 0
    
    while True:
        stdscr.clear()
        stdscr.addstr(0,0,f"📂 {path} (Press 'q' to exit)", curses.A_BOLD)

        for i, file in enumerate(files):
            if i == index:       
                stdscr.addstr(i+1,2,f" {file}", curses.A_REVERSE)
            else:
                stdscr.addstr(i + 1, 2, f" {file}")

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_DOWN and index < len(files)-1:
            index += 1
        elif key == curses.KEY_UP and index > 0:
            index -= 1

curses.wrapper(list_files)
    
        
# if __name__ == "__main__":
#     list_files()
