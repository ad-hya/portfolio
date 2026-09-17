# Adhya Desai — Portfolio Site

A three-page personal portfolio site (Home, About, Contact) built with HTML,
CSS, and Bootstrap 5, for BUDT748 (Fall 2026).

## Live Site

- Live URL: https://ad-hya.github.io/portfolio/
- Repository: https://github.com/ad-hya/portfolio

## Structure

```
├── index.html      # Home page (hero, interests, CTA)
├── about.html      # About page (bio, education, skills)
├── contact.html    # Contact page (info + demo contact form)
├── css/
│   └── style.css   # Custom theme (cream/ink editorial style, DM Serif + DM Mono)
├── js/
│   └── main.js     # Active nav-link highlighting + demo form validation
└── screenshots/    # Screenshots of each page for submission
```

## Tech

- **Bootstrap 5.3** (navbar, grid, buttons, forms) via CDN
- **Bootstrap Icons** via CDN
- **Google Fonts** (DM Serif Display, DM Mono, Instrument Sans)
- Vanilla JavaScript for the active nav state and contact form demo
  (the form is client-side only — there is no backend, so submissions are
  validated and show a success message but are not actually sent anywhere)

## Running locally

This is a static site — no build step required. Either open `index.html`
directly in a browser, or serve it locally:

```bash
python3 -m http.server 5500
```

Then visit `http://localhost:5500`.

## Content

Bio, education, skills, experience, and contact details are sourced from
Adhya's resumes and existing portfolio (ad-hya.github.io). Design language
(cream/ink palette, DM Serif Display + DM Mono + Instrument Sans) is a
companion style to that site, adapted to the tutorial's 3-page structure.

## Deployment (GitHub Pages)

1. Push this repo to GitHub.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`,
   branch `main`, folder `/ (root)`, then **Save**.
4. The site will be live at `https://<username>.github.io/<repo-name>/`.
