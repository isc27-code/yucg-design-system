# YUCG Design System

Design reference and component library for the Yale Undergraduate Consulting Group.

- **[design.md](design.md)**: brand rules (sections 1–10) and the component library (section 11). Ask for components by name, e.g. `yucg-hero`, `yucg-logo-wall`, `yucg-kpis`.
- **[gallery/](gallery/)**: a live page that renders every component from design.md's own CSS.

## Rebuild the gallery

After editing design.md:

```bash
python3 gallery/build_gallery.py
```

This writes `gallery/yucg-components.html`; open it in a browser.

## Fonts

The brand face, YaleNew, is licensed to Yale affiliates and is **not** included here. Pages fall back to Libre Caslon Text from Google Fonts.
