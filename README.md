# Personal Podcast Host

A self-hosted podcast system built with Hugo, featuring a futuristic cyberpunk theme.

## Setup

1. Install Hugo (extended version):
   ```bash
   # For Arch Linux/Manjaro
   sudo pacman -S hugo
   ```

2. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

3. Start the Hugo server:
   ```bash
   hugo server -D
   ```

## Adding New Episodes

1. Place your MP3 file in the `static/audio/` directory
2. Create a new episode:
   ```bash
   hugo new content episodes/your-episode-name.md
   ```
3. Edit the new file in `content/episodes/` with your episode details:
   ```yaml
   ---
   title= "Your Episode Title"
   date= YYYY-MM-DD
   description= "Episode description"
   audio= "your-audio-file.mp3"
   duration= "MM:SS"
   ---
   ```



## Deployment

1. Run `hugo` to build the site
1.1 Run `hugo server -D`
2. Deploy the `public` directory to your web server

## Accessing Your Podcast

- Web Interface: http://localhost:1313 (when running locally)
- RSS Feed: http://localhost:1313/feed.xml

## Features

- Futuristic cyberpunk UI
- Automatic RSS feed generation
- Mobile-responsive design
- Audio player for each episode
- Episode show notes support
