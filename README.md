# Maths — Mandelbrot Set (HTML)

This folder contains **static HTML** (no build step). The main page is `index.html`, which introduces the **Mandelbrot Set** and shows how it is generated from the iteration

<p><strong>z<sub>0</sub> = 0, &nbsp; z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c</strong></p>

for complex numbers **c**.

The main page is designed to work as a **desktop and mobile-friendly educational page** with **Hal AI by CJF** branding, a browser favicon, and an **Apple touch icon** for iPhone and iPad home-screen use.

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

## Companion pages

Both are linked from `index.html` (or open the HTML files directly).

- **`micro-build.html`** — **100×100** default view, painted in a **spiral from the centre** (32 pixels per frame). Short note on how **c** comes from `(px, py)`; when the build finishes, **hover** the canvas for a per-pixel escape summary and neighbours.

- **`pixel-walkthrough.html`** — One worked pixel from the default view: **x + i y**, **|z|**, centre/scale, and step-by-step orbit to escape (including **z²** arithmetic).

## How to view

Open `index.html` in any modern browser, or publish the folder on **GitHub Pages** and open the site URL.

**iPhone / iPad:** In Safari, tap **Share → Add to Home Screen**. The file `apple-touch-icon.png` is provided at **180 × 180** for the home-screen icon, and the mobile web app title is set to **Mandelbrot**.

## Assets in this folder

| File | Purpose |
|------|---------|
| `index.html` | Main interactive Mandelbrot page |
| `micro-build.html` | Small spiral “build” animation, c-mapping note, hover-to-inspect pixels |
| `pixel-walkthrough.html` | Worked example: one pixel, modulus from x + i y, step-by-step orbit to escape |
| `README.md` | Project summary and usage notes |
| `header-logo.svg` | Official Hal AI by CJF header logo used on the page |
| `favicon.svg` | Browser tab icon |
| `apple-touch-icon.png` | **180 × 180** Apple home-screen icon for iPhone and iPad |

## Notes

- No build step is required.
- The pages are entirely client-side HTML, CSS, SVG, canvas, and JavaScript.
- Deep zooms are limited by browser performance and floating-point precision, not by the mathematics itself.

---

*Educational summary only — intended as a clear visual introduction to the Mandelbrot Set.*
