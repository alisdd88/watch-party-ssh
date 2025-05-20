import time
import curses
from parser import parse_srt_file

def srt_time_to_seconds(srt_time):
    h, m, s = srt_time.replace(',', '.').split(':')
    s, ms = s.split('.') if '.' in s else (s, '0')
    return int(h) * 3600 + int(m) * 60 + int(s) + float('0.' + ms)

def main(stdscr):
    paused = False
    stopped = False
    stdscr.nodelay(True)

    def handle_input():
        nonlocal paused, stopped
        try:
            key = stdscr.getch()
            if key == ord(' '):
                paused = not paused
            elif key == 27:  # ESC
                stopped = True
        except Exception:
            pass

    curses.curs_set(0)
    stdscr.clear()
    subtitles = parse_srt_file(r".\subtitles\test.srt")
    start_time = time.time()

    status_line = 2  # Line to display playback status

    paused_time = 0
    pause_start = None

    for sub in subtitles:
        sub_displayed = False
        current_time = 0
        while True:
            handle_input()
            if paused:
                if pause_start is None:
                    pause_start = time.time()
                status = "⏸️ Paused"
            else:
                if pause_start is not None:
                    paused_time += time.time() - pause_start
                    pause_start = None
                status = "▶️ Playing"

            # Only advance current_time if not paused
            if paused:
                current_time = time.time() - start_time - paused_time
            else:
                current_time = time.time() - start_time - paused_time

            stdscr.addstr(status_line, 0, f"Status: {status}   ")
            stdscr.refresh()

            if paused:
                time.sleep(0.05)
                continue

            start_sub = srt_time_to_seconds(sub["start"])
            end_sub = srt_time_to_seconds(sub["end"])
            if not sub_displayed and current_time >= start_sub:
                stdscr.clear()
                stdscr.addstr(status_line, 0, f"Status: {status}     ")
                stdscr.addstr(0, 0, f'[{sub["start"]} -> {sub["end"]}] {sub["content"]}')
                stdscr.refresh()
                sub_displayed = True
            if current_time >= end_sub:
                stdscr.clear()
                stdscr.addstr(status_line, 0, f"Status: {status}     ")
                stdscr.refresh()
                break
            time.sleep(0.01)
 
if __name__ == "__main__":
    curses.wrapper(main)

