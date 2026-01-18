# GRT Importer Advanced (Offline)

This repository ships an **offline, self-contained** single-file web app.

## Run (no build required)
Open `dist/index.html` in your browser.

## Build (regenerates dist/index.html)
### Node (recommended)
- `npm run build`

### Python
- `python3 build/build.py`

## Offline guarantee
The built artifact (`dist/index.html`) contains all required CSS + JavaScript inline.
No external assets are required at runtime.
