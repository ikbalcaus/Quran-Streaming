import os
import json
from mutagen.mp3 import MP3

def parse_filename(filename):
    surah = int(filename[:3])
    ayah = int(filename[3:6])
    return surah, ayah

def generate_json_data(directory):
    cumulative_length = 0.0
    results = []
    ayah_no = 1
    for filename in sorted(os.listdir(directory)):
        if len(filename) == 10 and filename[:6].isdigit() and filename.endswith(".mp3"):
            file_path = os.path.join(directory, filename)
            audio = MP3(file_path)
            length = audio.info.length
            surah, ayah = parse_filename(filename)
            cumulative_length += length
            results.append({
                "ayahNo": ayah_no,
                "surah": surah,
                "ayah": ayah,
                "length": round(length, 3),
                "cumulativeLength": round(cumulative_length, 3),
            })
            ayah_no += 1
    return results

if __name__ == "__main__":
    directory = "audio"
    output_file = "data.json"
    audio_lengths = generate_json_data(directory)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(audio_lengths, f, indent=4, ensure_ascii=False)
