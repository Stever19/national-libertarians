import os
import markdown
import yaml
from datetime import datetime

POSTS_DIR = "posts"
BLOG_FILE = "blog.html"

POST_TEMPLATE = """<!doctype html>
<html lang="el">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | National Libertarians</title>
  <meta name="description" content="{excerpt}" />
  <link rel="stylesheet" href="../assets/style.css" />
</head>
<body>
  <div class="topbar">
    <div class="container nav">
      <a class="brand" href="../index.html" aria-label="Αρχική">
        <img class="logoimg" src="../logo.png" alt="National Libertarians logo">
        <span>NATIONAL LIBERTARIANS</span>
      </a>
      <div class="menu" role="navigation" aria-label="Μενού">
        <a data-nav href="../index.html">Αρχική</a>
        <a data-nav href="../manifesto.html">Θέσεις</a>
        <a data-nav href="../why.html">Γιατί NL</a>
        <a data-nav href="../blog.html">Άρθρα</a>
        <a data-nav href="../contact.html">Επικοινωνία</a>
      </div>
    </div>
  </div>

  <div class="page">
    <div class="container card wrap article">
      <p class="note"><a href="../blog.html">← Πίσω στα Άρθρα</a></p>
      <div class="meta">{date} · {minutes} λεπτά</div>
      <h1>{title}</h1>
      {content}
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <div>© 2026 National Libertarians. <span style="opacity:.8">Content υπό υπεύθυνη επιμέλεια.</span></div>
      <div style="margin-top:8px">
        <small class="note">Σημείωση: Το site προωθεί πολιτικές ιδέες. Δεν φιλοξενεί προτροπές σε βία ή μίσος.</small>
      </div>
    </div>
  </div>

  <script src="../assets/site.js"></script>
</body>
</html>
"""


BLOG_HEADER = """<!doctype html>
<html lang="el">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Άρθρα | National Libertarians</title>
  <meta name="description" content="Πολιτικά κείμενα, ανάλυση και προτάσεις." />
  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
  <div class="topbar">
    <div class="container nav">
      <a class="brand" href="index.html" aria-label="Αρχική">
        <img class="logoimg" src="logo.png" alt="National Libertarians logo">
        <span>NATIONAL LIBERTARIANS</span>
      </a>
      <div class="menu" role="navigation" aria-label="Μενού">
        <a data-nav href="index.html">Αρχική</a>
        <a data-nav href="manifesto.html">Θέσεις</a>
        <a data-nav href="why.html">Γιατί NL</a>
        <a data-nav href="blog.html">Άρθρα</a>
        <a data-nav href="contact.html">Επικοινωνία</a>
      </div>
    </div>
  </div>

  <div class="page">
    <div class="container card wrap">
      <h1>Άρθρα</h1>
      <p class="lead">Πολιτικά κείμενα, ανάλυση και προτάσεις.</p>
      <div class="grid-3">
"""

BLOG_FOOTER = """
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <div>© 2026 National Libertarians. <span style="opacity:.8">Content υπό υπεύθυνη επιμέλεια.</span></div>
      <div style="margin-top:8px">
        <small class="note">Σημείωση: Το site προωθεί πολιτικές ιδέες. Δεν φιλοξενεί προτροπές σε βία ή μίσος.</small>
      </div>
    </div>
  </div>

  <script src="assets/site.js"></script>
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
    excerpt=excerpt,
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

