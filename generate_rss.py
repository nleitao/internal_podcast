import os
import re
from email.utils import formatdate

# CONFIGURATION
# BASE_URL = "https://github.com/nleitao/internal_podcast/public/"  # <-- CHANGE THIS to your hosting URL
BASE_URL = "https://nleitao.github.io/internal_podcast/public/"
AUTHOR = "Your Name"
TITLE = "NPod"
DESCRIPTION = "My personal podcast feed"
EMAIL = "your@email.com"
OUTPUT = "feed.xml"  # Output to root folder
AUDIO_ROOT = "public"

# Helper to create a safe filename
SAFE_CHARS = re.compile(r'[^A-Za-z0-9._-]')
def safe_filename(filename):
    name, ext = os.path.splitext(filename)
    name = name.replace(' ', '_')
    name = SAFE_CHARS.sub('', name)
    return name + ext

# Rename files to safe filenames
original_to_safe = {}
for root, dirs, files in os.walk(AUDIO_ROOT):
    for fname in files:
        if fname.lower().endswith('.mp3'):
            safe_name = safe_filename(fname)
            if fname != safe_name:
                src = os.path.join(root, fname)
                dst = os.path.join(root, safe_name)
                # Avoid overwriting
                if not os.path.exists(dst):
                    os.rename(src, dst)
                    print(f"Renamed: {fname} -> {safe_name}")
                else:
                    print(f"Warning: {dst} already exists, skipping rename of {fname}")
                original_to_safe[os.path.relpath(dst, AUDIO_ROOT)] = fname
            else:
                original_to_safe[os.path.relpath(os.path.join(root, fname), AUDIO_ROOT)] = fname

items = []
for root, dirs, files in os.walk(AUDIO_ROOT):
    for fname in sorted(files, reverse=True):
        if fname.lower().endswith(".mp3"):
            rel_dir = os.path.relpath(root, AUDIO_ROOT)
            rel_path = os.path.join(rel_dir, fname) if rel_dir != "." else fname
            file_path = os.path.join(root, fname)
            pub_date, size = os.stat(file_path).st_mtime, os.stat(file_path).st_size
            pub_date = formatdate(pub_date)
            # Use original filename for title if available
            title = os.path.splitext(original_to_safe.get(rel_path, fname))[0]
            enclosure_url = BASE_URL + rel_path.replace("\\", "/")
            item = f"""
        <item>
            <title>{title}</title>
            <enclosure url=\"{enclosure_url}\" length=\"{size}\" type=\"audio/mpeg\"/>
            <guid>{enclosure_url}</guid>
            <pubDate>{pub_date}</pubDate>
            <description>{title}</description>
        </item>
        """
            items.append(item)

rss = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<rss version=\"2.0\">
<channel>
    <title>{TITLE}</title>
    <link>{BASE_URL}</link>
    <description>{DESCRIPTION}</description>
    <language>en-us</language>
    <lastBuildDate>{formatdate()} </lastBuildDate>
    <managingEditor>{EMAIL} ({AUTHOR})</managingEditor>
    {''.join(items)}
</channel>
</rss>
"""

with open(OUTPUT, "w") as f:
    f.write(rss)

print(f"Generated {OUTPUT} with {len(items)} episodes.") 
