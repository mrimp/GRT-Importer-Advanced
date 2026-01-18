# Architecture

## Runtime goals
- Fully offline, single-file delivery (`dist/index.html`).
- No external runtime dependencies (no CDN scripts, no remote CSS/fonts).
- Safe defaults for distribution (quiet console unless `?debug=1`).

## Repo layout
- `src/template.html`  
  The HTML shell with two injection tokens.
- `src/styles.css`  
  All styles consolidated from the historical single-file build.
- `src/app.js`  
  The full runtime JavaScript (including the embedded spreadsheet parser library).
- `build/build.js` + `build/build.py`  
  No-deps build scripts that generate `dist/index.html`.

## Refactor strategy used here
This "next-level" refactor focuses on:
1) **A clean, ZIP-friendly repository layout** suitable for GitHub.
2) **Deterministic builds**: `src/*` always regenerates the same `dist/index.html`.
3) **Strict offline posture**: no network calls; all resources are embedded.

If you want a deeper refactor (splitting `src/app.js` into modules and bundling them), we can do that next while preserving the single-file `dist/index.html` output.
