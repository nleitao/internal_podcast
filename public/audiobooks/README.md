# Dungeon Crawler Carl — Book 1

16 podcast episodes, split at the original chapter boundaries. All audio is included, from the opening credits through the epilogue and end credits.

- Format: MP3, 96 kbps constant bitrate, 44.1 kHz, stereo.
- Source duration: 13:31:33.062.
- Episode duration: approximately 40–60 minutes; each file is under 50 MiB.
- Listen in numbered order, Part 01 through Part 16 (choose oldest first if your podcast app sorts by publication date).
- The original M4B stays on disk and is excluded from Git by `.gitignore`.

## Episode boundaries

Times below refer to the original audiobook; the end of each part is the start of the next.

| Part | Source start | Source end | Chapters | Size (MiB) |
| --- | --- | --- | --- | ---: |
| [01](Dungeon_Crawler_Carl_Book_1_Part_01.mp3) | 00:00:00.000 | 00:44:26.647 | Opening Credits through Part I - Chapter 2 | 30.5 |
| [02](Dungeon_Crawler_Carl_Book_1_Part_02.mp3) | 00:44:26.647 | 01:31:26.896 | Chapter 3 through Chapter 4 | 32.3 |
| [03](Dungeon_Crawler_Carl_Book_1_Part_03.mp3) | 01:31:26.896 | 02:30:03.650 | Chapter 5 through Chapter 8 | 40.2 |
| [04](Dungeon_Crawler_Carl_Book_1_Part_04.mp3) | 02:30:03.650 | 03:25:10.354 | Chapter 9 through Chapter 12 | 37.8 |
| [05](Dungeon_Crawler_Carl_Book_1_Part_05.mp3) | 03:25:10.354 | 04:24:37.610 | Chapter 13 through Chapter 18 | 40.8 |
| [06](Dungeon_Crawler_Carl_Book_1_Part_06.mp3) | 04:24:37.610 | 05:18:08.534 | Chapter 19 through Chapter 21 | 36.7 |
| [07](Dungeon_Crawler_Carl_Book_1_Part_07.mp3) | 05:18:08.534 | 06:07:39.572 | Chapter 22 through Chapter 24 | 34.0 |
| [08](Dungeon_Crawler_Carl_Book_1_Part_08.mp3) | 06:07:39.572 | 06:52:54.100 | Chapter 25 through Chapter 26 | 31.1 |
| [09](Dungeon_Crawler_Carl_Book_1_Part_09.mp3) | 06:52:54.100 | 07:41:36.214 | Chapter 27 through Chapter 29 | 33.4 |
| [10](Dungeon_Crawler_Carl_Book_1_Part_10.mp3) | 07:41:36.214 | 08:38:55.900 | Chapter 30 through Chapter 32 | 39.4 |
| [11](Dungeon_Crawler_Carl_Book_1_Part_11.mp3) | 08:38:55.900 | 09:30:05.740 | Chapter 33 through Chapter 35 | 35.1 |
| [12](Dungeon_Crawler_Carl_Book_1_Part_12.mp3) | 09:30:05.740 | 10:17:27.188 | Chapter 36 through Chapter 38 | 32.5 |
| [13](Dungeon_Crawler_Carl_Book_1_Part_13.mp3) | 10:17:27.188 | 11:14:43.879 | Chapter 39 through Chapter 41 | 39.3 |
| [14](Dungeon_Crawler_Carl_Book_1_Part_14.mp3) | 11:14:43.879 | 12:03:04.352 | Chapter 42 through Chapter 43 | 33.2 |
| [15](Dungeon_Crawler_Carl_Book_1_Part_15.mp3) | 12:03:04.352 | 12:51:16.396 | Chapter 44 through Chapter 46 | 33.1 |
| [16](Dungeon_Crawler_Carl_Book_1_Part_16.mp3) | 12:51:16.396 | 13:31:33.062 | Chapter 47 through End Credits | 27.7 |

## Conversion

Each part was transcoded with FFmpeg using the following settings (start and duration are in seconds):

```bash
ffmpeg -ss START -i "1.Dungeon Crawler Carl, Book 1.m4b" -t DURATION \
  -map 0:a:0 -map_metadata 0 -map_chapters -1 \
  -c:a libmp3lame -b:a 96k -ar 44100 -ac 2 -id3v2_version 3 \
  -metadata "title=Dungeon Crawler Carl - Book 1 - Part NN of 16" \
  -metadata "track=N/16" Dungeon_Crawler_Carl_Book_1_Part_NN.mp3
```

Every MP3 was decoded in full to check for errors, and its duration was checked against its source interval (allowing for MP3 encoder padding).
