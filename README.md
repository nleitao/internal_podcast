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

## About
- This is version 2 of the project. No more Hugo or static site generator.
- Just drop your MP3s in `public/`, run the script, and your podcast feed is ready.
- The feed will include all `.mp3` files found in any subfolder of `public/`.
- The script is located in the root folder.

## Configuration
- Edit `BASE_URL` in `generate_rss.py` to match where your files will be hosted (e.g., GitHub Pages, your server, etc.).
- The generated `feed.xml` can be used in any podcast app that supports RSS feeds.

## License
MIT
