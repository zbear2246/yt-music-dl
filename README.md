# yt-music-dl

A simple script that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download songs as audio files.

## Requirements

- `yt-dlp`
- `node` (for JS runtime support)
- `curl` (for downloading yt-dlp)
- `Python 3` (to run `songsdl.py`)

## Setup

### 1. Install yt-dlp

You can download the latest `yt-dlp` release directly from GitHub:

```
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/.local/bin/yt-dlp
chmod +x /usr/.local/bin/yt-dlp
```

> Make sure `/usr/.local/bin` is in your `PATH` (see next section).

---

### 2. Check Your PATH

To see if `/usr/.local/bin` is in your `PATH`, run:

```
echo $PATH
```

If you see `/usr/.local/bin` listed (colon-separated), you’re good.  

If not, add it temporarily with:

```
export PATH=$PATH:/usr/.local/bin
```

To make it permanent, add that line to your shell config file:

- For **bash**: `~/.bashrc`  
- For **zsh**: `~/.zshrc`  

Example:

```
echo 'export PATH=$PATH:/usr/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

---

### 3. Configure yt-dlp

Create or edit the config file:

```
~/.config/yt-dlp/config
```

Add the following:

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

## How to Run `songsdl`

1. Move `songsdl.py` to a location in your PATH, for example:

```
sudo mv songsdl.py /usr/local/bin/songsdl
```

> Make sure to **remove the `.py` extension** so it can be called as `songsdl`.

2. Make it executable:

```
sudo chmod +x /usr/local/bin/songsdl
```

3. Run `songsdl` with the following options:

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

- `-i` / `--input` → full path to a text file containing song URLs.  
- `-o` / `--output` → full path to the folder where you want the songs downloaded.

Example usage:

```
songsdl -i /home/user/songlist.txt -o /home/user/Music
```

---

## What This Does

- Extracts audio only (`-x`)
- Converts to high-quality MP3
- Skips videos longer than 10 minutes
- Embeds metadata into files
- Cleans up leftover files
- Trims long filenames

---

## Caveats / Limitations

- This script is not perfect—if `yt-dlp` cannot find a song, it will simply skip it.  
- Some videos may not be available or extractable depending on the source.  

---

## Notes

- Designed for quick music downloads
- Keeps things simple with a global config
- More features may be added later