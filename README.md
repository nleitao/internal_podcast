# NPod Podcast Feed Generator (v2)

## How to Use (v2)

1. **Add your MP3 files**
   - Place your `.mp3` files into any folder or subfolder inside the `public/` directory.
   - Organize by season, topic, or however you like (e.g., `public/season1/episode1.mp3`).

2. **Generate the RSS feed**
   - Run the Python script from the root folder:
     ```bash
     python3 generate_rss.py
     ```
   - This will create/update `feed.xml` in the root folder, listing all your podcast episodes.

3. **Publish**
   - Add and commit your changes, then push to GitHub:
     ```bash
     git add .
     git commit -m "Add new episode(s)"
     git push -u origin main
     ```
   - E já está! (That's it!)

## Audiobooks

The feed generator accepts MP3 files. Convert M4B audiobooks to MP3 and split
them at chapter boundaries before generating the feed. Keep the original M4B
locally; originals in `public/audiobooks/` are ignored by Git.

[Dungeon Crawler Carl, Book 1](public/audiobooks/README.md) is available as 16
numbered episodes, approximately 40–60 minutes each. They use 96 kbps stereo MP3
at 44.1 kHz, with each file under 50 MiB. Listen from Part 01 through Part 16;
select oldest first when sorting by publication date.

After adding the converted episodes, run `python3 generate_rss.py` and commit
the MP3 files and updated `feed.xml`.

## SPLIT BIG FILE INTO 2
   
1) Check the duration of the MP3
ffmpeg -i public/Fuses_e_Vises_-_Joo_Paulo_Oliveira_Sobreiro_Capital.mp3


Look for:

Duration: HH:MM:SS.xx


Example: 01:12:30 (1 hour 12 minutes).

2) Split into two parts (by time)

Say you want two equal halves and the total is ~72 minutes.

First half (0 → 36 min)
ffmpeg -i public/Fuses_e_Vises_-_Joo_Paulo_Oliveira_Sobreiro_Capital.mp3 \
  -t 00:36:00 -c copy \
  public/Fuses_e_Vises_part1.mp3

Second half (36 min → end)
ffmpeg -i public/Fuses_e_Vises_-_Joo_Paulo_Oliveira_Sobreiro_Capital.mp3 \
  -ss 00:36:00 -c copy \
  public/Fuses_e_Vises_part2.mp3
   
   
   
   ## About
- This is version 2 of the project. No more Hugo or static site generator.
- Just drop your MP3s in `public/`, run the script, and your podcast feed is ready.
- The feed will include all `.mp3` files found in any subfolder of `public/`.
- The script is located in the root folder.

## Configuration
- Edit `BASE_URL` in `generate_rss.py` to match where your files will be hosted (e.g., GitHub Pages, your server, etc.).
- The generated `feed.xml` can be used in any podcast app that supports RSS feeds.


## IF YOU ARE STARTING / CLONING THIS REPO, DONT FORGET TO CONFIG GITHUB PAGES! AFTER YO DO THAT YOU NEED TO USE THE GITHUB.IO LINK TO YOUR .XML FILE


## License
MIT
