from ipywidgets import interact
import matplotlib.pyplot as plt
import torch

from .widgets import get_widgets
from .utils import remove_nans


def distviz(p):
    def update(x_min, x_max, x_step, **kwargs):
        x_data = torch.arange(x_min, x_max, x_step)
        y_data = torch.exp(p(**kwargs).log_prob(x_data))
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        ax.set_xlim([x_min, x_max])
        try:
            y_without_nans = remove_nans(y_data)
            y_min = y_without_nans.min()
            y_max = y_without_nans.max()
        except RuntimeError:
            y_min = None
            y_max = None
        ax.set_ylim([y_min, y_max])
        fig.canvas.draw_idle()

    fig, ax = plt.subplots()
    x = torch.arange(0, 1, .1)
    line, = ax.plot(x, x)
    ax.set_title(str(p.__name__))
    interact(update, **get_widgets(p))
