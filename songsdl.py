#!/usr/bin/env python3

import subprocess
from pathlib import Path
import argparse


def create_song_list(input_file_path: str):
    
    
    with open(input_file_path, "r") as f:
        songs_list = list(map(str.rstrip, f))
        
        return songs_list


def run_ytdlp(song: str, output_folder: str):
    
    print(f"\n {song} \n")
    subprocess.run(
        [
            "yt-dlp",
            "-o", f"{output_folder}",
            f"ytsearch1:{song}"
        ]
    )
         
    

def flags():
    parser = argparse.ArgumentParser(description="Quickly download desired songs to a specific directory using yt-dlp")
    
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="The full/absolute path to the list of songs"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="The full/absolute path to the desired download path"
    )
    
    args = parser.parse_args()
    
    input_file = args.input
    output_folder = args.output
    
    return input_file, output_folder

def main():
    input_file, output_folder = flags()
    
    list_of_songs:list = create_song_list(input_file)   
    
    for song in list_of_songs:
        full_path = f"{output_folder}{song}.%(ext)s"
        run_ytdlp(song, full_path)
    
    
    
if __name__ == "__main__":
    try:
     main()
    except KeyboardInterrupt:
        print("user has interupted")