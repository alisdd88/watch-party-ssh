import time
from parser import parse_srt_file 
import sys

start_time = time.time()

def srt_time_to_seconds(srt_time):
    h, m, s = srt_time.replace(',', '.').split(':')
    s, ms = s.split('.') if '.' in s else (s, '0')
    return int(h) * 3600 + int(m) * 60 + int(s) + float('0.' + ms)

subtitles = parse_srt_file(r".\subtitles\test.srt")
for sub in subtitles:
    sub_displayed = False
    while True:
        current_time = time.time() - start_time
        start_sub = srt_time_to_seconds(sub["start"])
        end_sub = srt_time_to_seconds(sub["end"])
        if not sub_displayed and current_time >= start_sub:
            print(f'[{sub["start"]} -> {sub["end"]}] {sub["content"]}', end='\r')
            sub_displayed = True
        if current_time >= end_sub:
            print(' ' * 80, end='\r')  # Clear the line
            break
        time.sleep(0.01)

# print(start_time)

