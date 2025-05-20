import srt
import re

def clean_subtitle_content(content):
    # Remove line breaks and extra spaces between words
    clean_content = ' '.join(content.split())
    # Remove HTML tags
    clean_content = re.sub(r'<.*?>', '', clean_content)
    return clean_content

def format_timestamp(timestamp):
    # Format timestamp as (HH:MM:SS.mmm)
    total_seconds = int(timestamp.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(timestamp.microseconds / 1000)
    return f'{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}'

def parse_srt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        srt_content = file.read()
    subtitle_generator = srt.parse(srt_content)
    subtitles = list(subtitle_generator)
    parsed_subtitles = []
    for subtitle in subtitles:
        clean_content = clean_subtitle_content(subtitle.content)
        start = format_timestamp(subtitle.start)
        end = format_timestamp(subtitle.end)
        parsed_subtitles.append({
            "start": start,
            "end": end,
            "content": clean_content
        })
    return parsed_subtitles

# Example usage:
# if __name__ == "__main__":
#     subtitles = parse_srt_file(r".\subtitles\test.srt")
#     for sub in subtitles:
#         print(f'[{sub["start"]} -> {sub["end"]}] {sub["content"]}')
