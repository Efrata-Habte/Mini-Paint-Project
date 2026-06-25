# Mini Paint - Vector Drawing Application

A real-time interactive 2D vector drawing application built with Python, OpenGL, and GLFW.

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

For keyboard shortcuts, see [QUICK_REFERENCE.txt](QUICK_REFERENCE.txt)

## Features

- **Drawing Tools**: Lines, Polylines, Regular Polygons
- **Transformations**: Translate, Rotate, Scale shapes
- **Selection**: Click to select and manipulate shapes
- **Colors**: 7 colors with quick cycling
- **Real-time**: 60 FPS OpenGL rendering

## System Requirements

- Python 3.8+
- pip package manager
- OpenGL 3.3+ capable graphics hardware

## What You Can Do

1. **Draw Shapes**
   - Lines (2 clicks)
   - Polylines (multiple clicks, finish with Enter/Right-click)
   - Polygons (3-12 sides, configurable)

2. **Edit Shapes**
   - Select by clicking
   - Move with Translation
   - Rotate around center
   - Scale (uniform or non-uniform)

3. **Customize**
   - Change polygon sides with P (direct input) or [ / ]
   - Cycle colors with C
   - Delete with Delete key

## Keyboard Shortcuts

| Key | Action |
|---|---|
| 1-5 | Select tool |
| P | Set polygon sides (new!) |
| [ / ] | Adjust polygon sides |
| T / R / S | Transform modes |
| C | Cycle color |
| Del | Delete shape |
| Esc | Cancel |

See [QUICK_REFERENCE.txt](QUICK_REFERENCE.txt) for complete reference.

## Documentation

- **[USER_GUIDE.md](USER_GUIDE.md)** - Complete user guide with all features
- **[QUICK_REFERENCE.txt](QUICK_REFERENCE.txt)** - Quick keyboard shortcut reference

## Architecture

- `main.py` - Entry point
- `mini_paint/application.py` - Main application and event handling
- `mini_paint/viewport.py` - Coordinate system mapping
- `mini_paint/shapes.py` - Shape definitions
- `mini_paint/renderer.py` - OpenGL rendering
- `mini_paint/hud.py` - On-screen UI
- `mini_paint/math_utils.py` - Matrix operations

## Technical Highlights

- ✅ Proper screen-to-world coordinate mapping
- ✅ 2D affine transformations with matrix composition
- ✅ Modern OpenGL 3.3+ with shaders
- ✅ Efficient hit detection
- ✅ Real-time rendering at 60 FPS
- ✅ Full type hints throughout

---

**Happy drawing! 🎨**
