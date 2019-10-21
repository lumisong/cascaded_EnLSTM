import matplotlib.pyplot as plt
import numpy as np


def draw_comparing_diagram(pred, pred_std, target, ylabel, title):
    x = np.arange(len(target))
    plt.figure(figsize=(60, 50))
    plt.plot(target, label='target', color='black', alpah=0.4)
    plt.errorbar(x, pred[:, 0], yerr=pred_std[:, 0], color='red', alpha=0.7)
    plt.tittle()
    plt.legend()
    plt.tight_layout()
    plt.savefig('{}.png')