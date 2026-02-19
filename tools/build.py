import os
import markdown
import yaml
from datetime import datetime

POSTS_DIR = "posts"
BLOG_FILE = "blog.html"

POST_TEMPLATE = """<!doctype html>
<html lang="el">
<head>
  <meta charset="utf-8">
  <title>{title} | National Libertarians</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <div class="container article">
    <a href="../blog.html">← Πίσω στα άρθρα</a>
    <h1>{title}</h1>
    <div class="meta">{date} · {minutes} λεπτά</div>
    <hr>
    {content}
  </div>
</body>
</html>
"""

BLOG_HEADER = """<!doctype html>
<html lang="el">
<head>
  <meta charset="utf-8">
  <title>Άρθρα | National Libertarians</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="container">
<h1>Άρθρα</h1>
<p>Πολιτικά κείμενα, ανάλυση και προτάσεις.</p>
<div class="grid-3">
"""

BLOG_FOOTER = """
</div>
</div>
</body>
</html>
"""

def parse_md(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    if raw.startswith("---"):
        _, front, body = raw.split("---", 2)
        meta = yaml.safe_load(front)
    else:
        meta = {}
        body = raw

    html = markdown.markdown(body, extensions=["extra"])
    return meta, html


def main():
    cards = []

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue

        path = os.path.join(POSTS_DIR, fname)
        meta, content = parse_md(path)

        title = meta.get("title", "Χωρίς τίτλο")
        date = meta.get("date", "")
        minutes = meta.get("minutes", "")
        excerpt = meta.get("excerpt", "")

        slug = fname.replace(".md", ".html")
        out_path = os.path.join(POSTS_DIR, slug)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(POST_TEMPLATE.format(
                title=title,
                date=date,
                minutes=minutes,
                content=content
            ))

        cards.append(f"""
<a class="card post-card" href="posts/{slug}">
  <div class="meta">{date} · {minutes} λεπτά</div>
  <h3>{title}</h3>
  <p>{excerpt}</p>
</a>
""")

    with open(BLOG_FILE, "w", encoding="utf-8") as f:
        f.write(BLOG_HEADER + "\n".join(cards) + BLOG_FOOTER)


if __name__ == "__main__":
    main()

