# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A minimal personal podcast feed generator. Drop MP3 files into `public/`, run one Python script, and push to GitHub Pages. No framework, no build system.

## Workflow

```bash
# After adding MP3s to public/
python3 generate_rss.py

# Then commit and push
git add .
git commit -m "Add new episode(s)"
git push -u origin main
```

## How the feed is generated

`generate_rss.py` walks `public/` recursively, finds all `.mp3` files, and:
1. **Auto-renames** files with unsafe characters (spaces, special chars) to safe filenames in place — the original filename is preserved as the episode title.
2. Sorts episodes in reverse filename order (newest episodes appear first in the feed).
3. Uses `st_mtime` (file modification time) as the episode publish date.
4. Writes `feed.xml` to the repo root.

The feed is served via GitHub Pages at `https://nleitao.github.io/internal_podcast/`. The `BASE_URL` in the script must match the GitHub Pages URL for enclosure links to work in podcast apps.

## Configuration

Edit these constants at the top of `generate_rss.py`:
- `BASE_URL` — hosting URL (currently `https://nleitao.github.io/internal_podcast/public/`)
- `TITLE`, `DESCRIPTION`, `AUTHOR`, `EMAIL` — feed metadata
- `OUTPUT` — output filename (default `feed.xml`)

## Splitting large MP3s with ffmpeg

```bash
# Check duration
ffmpeg -i public/somefile.mp3

# Split: first half (0 → 36 min)
ffmpeg -i public/somefile.mp3 -t 00:36:00 -c copy public/somefile_part1.mp3

# Split: second half (36 min → end)
ffmpeg -i public/somefile.mp3 -ss 00:36:00 -c copy public/somefile_part2.mp3
```

## Folder layout under `public/`

Episodes are organized by topic/source:
- `courses/` — lectures and educational content
- `jocko_psy_war/` — Jocko motivational clips
- `music/` — music tracks
- `others/` — miscellaneous (interviews, etc.)
- `Spanish_Lessons/` — language learning

Subfolder names appear in the enclosure URL but not in the episode title.

## GitHub Pages setup

After cloning, enable GitHub Pages in the repo settings (source: `main` branch, root `/`). The RSS feed URL to subscribe to is `https://nleitao.github.io/internal_podcast/feed.xml`.
