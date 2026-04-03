# yt-music-dl

A simple script that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download songs as audio files by searching YouTube automatically — no URLs needed.

## Requirements

- `yt-dlp`
- `node` (for yt-dlp's JS challenge solver)
- `Python 3` (to run `songsdl.py`)

## Setup

### 1. Install yt-dlp

Download the latest `yt-dlp` release directly from GitHub:
```
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o ~/.local/bin/yt-dlp
chmod +x ~/.local/bin/yt-dlp
```

> Make sure `~/.local/bin` is in your `PATH` (see next section).

---

### 2. Check Your PATH

To see if `~/.local/bin` is in your `PATH`, run:
```
echo $PATH | grep ~/.local/bin
```

If you see `~/.local/bin` listed, you're good. If not, add it permanently:
```
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

---

### 3. Install Node.js

Node is used by yt-dlp to solve YouTube's JS challenges, which helps avoid download failures. Install it with:
```
sudo apt install nodejs
```

---

### 4. Configure yt-dlp

Create the config directory:
```
mkdir ~/.config/yt-dlp
```

Open or create `~/.config/yt-dlp/config` and paste this in:
```
--js-runtimes node
-x
--audio-format mp3
--audio-quality 0

# Skip long videos (no 1 hour loops)
--match-filter "duration < 600"

# Prevent leftover temp/video files
--embed-metadata
--no-keep-video

--trim-filenames 100
```

---

## Download songsdl

Clone the repo and move the script to your PATH:
```
git clone https://github.com/zbear2246/yt-music-dl.git
cd yt-music-dl
mv songsdl.py ~/.local/bin/songsdl
chmod +x ~/.local/bin/songsdl
```

Remove the `.py` extension so it can be called as just `songsdl`.

---

## How to Run `songsdl`

Run `songsdl` with the following options:
```
songsdl -h
```

You should see:
```
usage: songsdl [-h] -i INPUT -o OUTPUT

Quickly download desired songs to a specific directory using yt-dlp

options:
  -h, --help           show this help message and exit
  -i, --input INPUT    The full/absolute path to the list of songs
  -o, --output OUTPUT  The full/absolute path to the desired download path
```

- `-i` / `--input` → full path to a plain text file containing your song list.
- `-o` / `--output` → full path to the folder where you want the songs downloaded.

Example:
```
songsdl -i /home/user/songlist.txt -o /home/user/Music/
```

Make sure your output path ends with a `/` so files are saved correctly inside the folder.

---

## Song List Format

Your input file should be a plain text file with one song per line, written as:
```
ARTIST - SONG NAME
```

Example:
```
Iron Maiden - The Trooper
Queen - Bohemian Rhapsody
Metallica - Master of Puppets
```

yt-dlp will search YouTube for each line automatically. Using the `ARTIST - SONG NAME` format gives the best results.

---

## What This Does

- Searches YouTube automatically — no URLs needed
- Extracts audio only and converts to high-quality MP3
- Skips videos longer than 10 minutes
- Embeds metadata into files
- Cleans up leftover files
- Trims long filenames

---

## Caveats / Limitations

- If yt-dlp cannot find a song, it will simply skip it.
- Some videos may not be available or extractable depending on the source.
- YouTube actively works to block downloaders, so downloads may occasionally fail even on an up-to-date install. Keeping yt-dlp updated helps.
- YouTube may rate-limit or block requests if you download a large number of songs back to back.
- Some regions may have restricted access to certain videos due to geographic limitations.