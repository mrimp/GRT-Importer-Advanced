#!/usr/bin/env python3
"""Offline, no-deps builder.

This repository keeps runtime fully self-contained and offline.
The build step injects src/styles.css and src/app.js into src/template.html.

Reads:
  - src/template.html
  - src/styles.css
  - src/app.js
Writes:
  - dist/index.html (release artifact)
  - index.html (convenience copy)

No external libraries.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
DIST = ROOT / "dist"

CSS_TOKEN = "/*__INJECT_CSS__*/"
JS_TOKEN = "/*__INJECT_JS__*/"


def build() -> None:
    template = (SRC / "template.html").read_text("utf-8")
    css = (SRC / "styles.css").read_text("utf-8")
    js = (SRC / "app.js").read_text("utf-8")

    if CSS_TOKEN not in template or JS_TOKEN not in template:
        raise SystemExit("Template is missing injection tokens")

    out = template.replace(CSS_TOKEN, css).replace(JS_TOKEN, js)

    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / "index.html").write_text(out, "utf-8")
    (ROOT / "index.html").write_text(out, "utf-8")


if __name__ == "__main__":
    build()
    print("Built dist/index.html")
