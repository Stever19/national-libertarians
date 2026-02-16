# National Libertarians – Static Website

Αυτό είναι ένα απλό, γρήγορο, **πολιτικό** site (κόκκινο/μαύρο) με σελίδες + blog.

## Πώς το τρέχεις τοπικά
Απλά άνοιξε το `index.html` στον browser ή χρησιμοποίησε ένα local server:
- VS Code → Live Server
ή
- Python:
  ```bash
  python -m http.server 8000
  ```
  και άνοιξε: http://localhost:8000

## Πώς ανεβάζεις άρθρα
1. Άνοιξε `blog.html` και πρόσθεσε νέο "card" άρθρου.
2. Δημιούργησε νέο αρχείο μέσα στο `posts/` (π.χ. `posts/2026-02-17-giati-national-libertarian.html`).
3. Στο τέλος κάθε άρθρου υπάρχει κουμπί "Πίσω στα άρθρα".

## Deploy (δωρεάν)
- GitHub Pages (στατικό hosting)
- Netlify / Cloudflare Pages

Αν θες, μπορώ να στο προσαρμόσω ώστε τα άρθρα να γράφονται σε Markdown και να γίνεται αυτόματο build.
