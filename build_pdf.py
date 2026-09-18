"""Builds the BUDT748 client-side assignment submission PDF:
a cover page with the live site + repo links, followed by one page per
screenshot (Home, About, Contact)."""

import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

BASE = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS = os.path.join(BASE, "screenshots")
OUT_PATH = os.path.join(BASE, "BUDT748_ClientSideSetup_Submission.pdf")

INK = HexColor("#0e0e0e")
MUTED = HexColor("#6b6b6b")
BORDER = HexColor("#e2e2e2")

LIVE_URL = "https://ad-hya.github.io/portfolio/"
REPO_URL = "https://github.com/ad-hya/portfolio"

PAGE_W = 1400
MARGIN = 70


def cover_page(c):
    height = 760
    c.setPageSize((PAGE_W, height))

    y = height - 130
    c.setFont("Helvetica-Bold", 34)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, "BUDT748 — Client-Side Web Development")

    y -= 46
    c.setFont("Helvetica", 20)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, "Three-page portfolio site — Adhya Desai")

    y -= 90
    c.setStrokeColor(BORDER)
    c.line(MARGIN, y, PAGE_W - MARGIN, y)

    def link_row(label, url, y):
        c.setFont("Helvetica-Bold", 15)
        c.setFillColor(MUTED)
        c.drawString(MARGIN, y, label.upper())
        y -= 30
        c.setFont("Helvetica", 22)
        c.setFillColor(HexColor("#1a56db"))
        c.drawString(MARGIN, y, url)
        text_width = c.stringWidth(url, "Helvetica", 22)
        c.linkURL(url, (MARGIN, y - 6, MARGIN + text_width, y + 22), relative=0)
        return y

    y -= 50
    y = link_row("Live Website", LIVE_URL, y)

    y -= 60
    y = link_row("GitHub Repository", REPO_URL, y)

    y -= 60
    c.setStrokeColor(BORDER)
    c.line(MARGIN, y, PAGE_W - MARGIN, y)

    y -= 50
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, "PAGES INCLUDED")
    y -= 30
    c.setFont("Helvetica", 16)
    c.setFillColor(INK)
    for page_name in ["Home (index.html)", "About (about.html)", "Contact (contact.html)"]:
        c.drawString(MARGIN, y, "•  " + page_name)
        y -= 26

    c.showPage()


def screenshot_page(c, title, subtitle, img_path):
    img = Image.open(img_path)
    img_w, img_h = img.size

    content_w = PAGE_W - 2 * MARGIN
    scale = min(content_w / img_w, 1.0)
    draw_w = img_w * scale
    draw_h = img_h * scale

    title_area = 150
    height = title_area + draw_h + MARGIN
    c.setPageSize((PAGE_W, height))

    y = height - 70
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, title)

    y -= 34
    c.setFont("Helvetica", 16)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, subtitle)

    img_x = (PAGE_W - draw_w) / 2
    img_y = MARGIN / 2
    c.setStrokeColor(BORDER)
    c.setLineWidth(1)
    c.rect(img_x - 1, img_y - 1, draw_w + 2, draw_h + 2, stroke=1, fill=0)
    c.drawImage(img_path, img_x, img_y, width=draw_w, height=draw_h)

    c.showPage()


def main():
    c = canvas.Canvas(OUT_PATH)
    c.setTitle("BUDT748 Client-Side Submission - Adhya Desai")

    cover_page(c)
    screenshot_page(
        c,
        "Home Page",
        LIVE_URL,
        os.path.join(SCREENSHOTS, "home.png"),
    )
    screenshot_page(
        c,
        "About Page",
        LIVE_URL + "about.html",
        os.path.join(SCREENSHOTS, "about.png"),
    )
    screenshot_page(
        c,
        "Contact Page",
        LIVE_URL + "contact.html",
        os.path.join(SCREENSHOTS, "contact.png"),
    )

    c.save()
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()
