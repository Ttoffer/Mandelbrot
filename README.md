# Maths — Mandelbrot Set (HTML)

This folder contains a **single static web page**, `index.html`, that introduces the **Mandelbrot Set** and shows how it is generated from the iteration

<p><strong>z<sub>0</sub> = 0, &nbsp; z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c</strong></p>

for complex numbers **c**.

The page is designed to work as a **desktop and mobile-friendly educational page** with **Hal AI by CJF** branding, a browser favicon, and an **Apple touch icon** for iPhone and iPad home-screen use.

## What the page covers

- **What the Mandelbrot Set is** — the set of complex numbers **c** for which the orbit stays bounded under repeated iteration.
- **How the fractal image is generated** — each pixel represents a complex number, and the colouring shows how quickly the orbit escapes.
- **Bounded vs unbounded behaviour** — including the practical computer rule that once **|z| > 2**, the orbit will escape.
- **Interactive explorer** — zoom in, zoom out, reset, pan, and run an automatic zoom tour.
- **Orbit visualiser** — sample points showing orbits that stay bounded, escape, or lie near the boundary.
- **Why the zoom appears endless** — a reader-friendly explanation of the set’s rich boundary structure.
- **Mathematical relevance** — links to complex dynamics, Julia sets, chaos, stability, and mathematical visualisation.

## Interactive features

- **Tap / click** on the Mandelbrot image to zoom in at that point.
- **Drag** to pan the view.
- **Mouse wheel** zoom works on PC.
- **Zoom + / Zoom - / Reset** buttons provide direct control.
- **Auto Tour** continuously zooms in and back out to give the “no visible limit” effect.
- **Classic Focus** jumps to a well-known detailed region of the set.
- **Extra detail** slider increases the base iteration count for sharper boundary detail.

## How to view

Open `index.html` in any modern browser, or publish the folder on **GitHub Pages** and open the site URL.

**iPhone / iPad:** In Safari, tap **Share → Add to Home Screen**. The file `apple-touch-icon.png` is provided at **180 × 180** for the home-screen icon, and the mobile web app title is set to **Mandelbrot**.

## Assets in this folder

| File | Purpose |
|------|---------|
| `index.html` | Main interactive Mandelbrot page |
| `README.md` | Project summary and usage notes |
| `header-logo.svg` | Official Hal AI by CJF header logo used on the page |
| `favicon.svg` | Browser tab icon |
| `apple-touch-icon.png` | **180 × 180** Apple home-screen icon for iPhone and iPad |

## Notes

- No build step is required.
- The page is entirely client-side HTML, CSS, SVG, canvas, and JavaScript.
- Deep zooms are limited by browser performance and floating-point precision, not by the mathematics itself.

---

*Educational summary only — intended as a clear visual introduction to the Mandelbrot Set.*
