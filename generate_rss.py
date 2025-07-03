import os
from email.utils import formatdate

# CONFIGURATION
# BASE_URL = "https://github.com/nleitao/internal_podcast/public/"  # <-- CHANGE THIS to your hosting URL
BASE_URL = "https://nleitao.github.io/internal_podcast/public/"
AUTHOR = "Your Name"
TITLE = "NPod2"
DESCRIPTION = "My personal podcast feed2"
EMAIL = "your@email.com"
OUTPUT = "feed.xml"  # Output to root folder
AUDIO_ROOT = "public"

def get_file_info(filepath):
    stat = os.stat(filepath)
    pub_date = formatdate(stat.st_mtime)
    size = stat.st_size
    return pub_date, size

items = []
for root, dirs, files in os.walk(AUDIO_ROOT):
    for fname in sorted(files, reverse=True):
        if fname.lower().endswith(".mp3"):
            rel_dir = os.path.relpath(root, AUDIO_ROOT)
            rel_path = os.path.join(rel_dir, fname) if rel_dir != "." else fname
            file_path = os.path.join(root, fname)
            pub_date, size = get_file_info(file_path)
            title = os.path.splitext(fname)[0]
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
