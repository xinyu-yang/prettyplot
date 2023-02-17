# PrettyPlot

This project is created to draw pretty figures.

How to use it:

First, intall it:

```bash
git clone https://github.com/xinyu-yang/prettyplot.git
pip install -e ./prettyplot
```

Then, you can import and use it:

```python
import numpy as np
import prettyplot as ppt
from prettyplot.config import *

fig_setting = {
                "title": "The title of the figure",
                # The scale to expand, which is used to set the figure size
                "scale": (0.5, 0.5),
                "title_size": 16,
                # The size of x and y labels
                "label_size":14,
                # The size of legend
                "legend_size": 12,
                ...
              }
settings = [
    {
        "color": GNU_COLOR[0],
        "label": "sin(x)",
        "linestyle": "-",
        "marker": MARKERSTYLE[0],
    },
    ...
]

x = np.linspace(0, 2*np.pi, 20)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = ppt.line.lines([x, x], [y1, y2], settings, fig_setting)

plt.show()
```

The provided funtion provide basic functions, you can define more advanced parameters with the retured fig and ax variables.

```python
# Set the border the figure
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

# Set the background color of the image
fig.patch.set_visible(False)
ax.patch.set_visible(False)

# The legend
ax.legend(frameon=False, fontsize=12, loc="lower right")

# Plot grid
# plt.grid(linestyle="--")

# Show
plt.show()

# save figure
# fig.savefig("test.pdf", transparent=True, bbox_inches='tight')
```

There is an [example](./tests/test.ipynb) that can cover all the features.
