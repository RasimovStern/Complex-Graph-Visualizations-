<div align="center">

# Complex-Graph-Visualizations

**Animated mathematical graphs built with [Manim](https://www.manim.community/) and LaTeX**

![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=white)
![Manim](https://img.shields.io/badge/manim-community-orange)
![LaTeX](https://img.shields.io/badge/LaTeX-required-008080?logo=latex&logoColor=white)
![License](https://img.shields.io/badge/license-Apache%202.0-green)

<img src="assets/GraphDemo.gif" alt="Animated demo: sine wave with a sliding dot morphing into a damped sine, then a cosine overlay" width="720">

</div>

## About

An animated walkthrough of harmonic functions, built with Manim and LaTeX. A single scene draws a sine wave, morphs it into a damped oscillation while its frequency rises, and overlays a cosine for comparison. Each curve is defined by a one-line formula, so the whole animation fits in about 50 lines of Python.

The full-quality render is available as [`assets/GraphDemo.mp4`](assets/GraphDemo.mp4).

## Table of Contents

- [About](#about)
- [What the Animation Shows](#what-the-animation-shows)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customizing the Graphs](#customizing-the-graphs)
- [License](#license)

## What the Animation Shows

The `GraphDemo` scene in [`graph_demo.py`](graph_demo.py) plays through three stages on a single set of axes ($0 \le x \le 8$, $-2 \le y \le 2$):

| Stage | Equation | What happens |
|:-----:|:--------:|--------------|
| 1 | $y = \sin x$ | The sine curve is drawn in blue and a dot slides along it from $x = 0$ to $x = 8$. |
| 2 | $y = e^{-0.2x}\sin(kx)$ | The sine morphs into a damped wave (yellow) while $k$ increases from $1$ to $2.5$, making it oscillate faster and decay. |
| 3 | $y = \cos x$ | A red cosine curve is overlaid for comparison, then fades out before the scene wraps up. |

Key Manim features used:

- **`Axes`** with numbered ticks and axis labels
- **`ValueTracker` + `always_redraw`** to animate a moving dot and a live-updating curve
- **`ReplacementTransform` / `FadeTransform`** to morph one graph and its LaTeX label into another
- **`MathTex`** to typeset the equations with LaTeX

## Repository Structure

```
Complex-Graph-Visualizations-/
├── assets/
│   ├── GraphDemo.gif      # Preview shown in this README
│   └── GraphDemo.mp4      # Full rendered animation
├── graph_demo.py          # Manim scene (GraphDemo)
├── requirements.txt       # Python dependencies
├── LICENSE                # Apache 2.0
└── README.md
```

## Requirements

- Python 3.9 or newer
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html) and its system dependencies (Cairo, Pango, FFmpeg)
- A LaTeX distribution (e.g. [MiKTeX](https://miktex.org/), [MacTeX](https://www.tug.org/mactex/) or TeX Live), needed for the `MathTex` equation labels

## Installation

```bash
git clone https://github.com/RasimovStern/Complex-Graph-Visualizations-.git
cd Complex-Graph-Visualizations-

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

Render and preview the scene at low quality (fast):

```bash
manim -pql graph_demo.py GraphDemo
```

Render at high quality (1080p, 60 fps):

```bash
manim -pqh graph_demo.py GraphDemo
```

The output video is written to `media/videos/graph_demo/<quality>/GraphDemo.mp4`.

| Flag | Meaning |
|------|---------|
| `-p` | Open the video when rendering finishes |
| `-ql` / `-qm` / `-qh` / `-qk` | Low / medium / high / 4K quality |
| `--format gif` | Export as a GIF instead of MP4 |

## Customizing the Graphs

Each curve is defined by a plain Python lambda, so swapping in your own equation is a one-line change:

```python
# Plot any function of x on the existing axes
my_graph = axes.plot(lambda x: 0.5 * x * np.sin(2 * x), color=GREEN)
my_label = MathTex(r"y = \tfrac{1}{2}x\sin(2x)").next_to(axes, UP + RIGHT)
self.play(Create(my_graph), FadeIn(my_label))
```

Other things to try:

- Change the `x_range` / `y_range` of the `Axes` to zoom in or out
- Animate a different parameter with a `ValueTracker` (e.g. the damping factor `0.2`)
- Adjust `run_time` on any `self.play(...)` call to speed up or slow down a stage

## License

This project is licensed under the [Apache License 2.0](LICENSE).
