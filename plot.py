import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import LogLocator
from matplotlib.ticker import ScalarFormatter
import scipy 

#color pallete

VIBGYOR_PAPER = {
    "black":   "#000000",  # FG
    "blue":    "#5f67a4",  # CG
    "orange":  "#D55E00",  # DPD
    "green":   "#7ECC79",  # pll
    "pink":    "#CC79A7",  # pd
    "cyan":    "#79CCC8",  # cb1
    "red":     "#E41A1C",  # cb2
    "yellow":  "#FBAF00",  # cb3
    "brown":   "#8C510A",  # cb4
}

plt.rcParams.update({
    # --- LaTeX rendering ---
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern"],

    # --- Font sizes ---
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,

    # --- Axes style ---
    "axes.linewidth": 1.0,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,

    # --- Tick sizes ---
    "xtick.major.size": 5,
    "ytick.major.size": 5,
    "xtick.minor.size": 3,
    "ytick.minor.size": 3,
    "xtick.major.width": 1.2,
    "ytick.major.width": 1.2,

    # --- Line style ---
    "lines.linewidth": 2,
    "lines.markersize": 5,

    # --- Legend ---
    "legend.borderpad": 0.3,
    "legend.labelspacing": 0.3,
    "legend.markerscale": 1.5,
    "legend.frameon": False,

    # --- Optional LaTeX preamble (useful for math consistency) ---
    "text.latex.preamble": r"\usepackage{amsmath}"
})


#VACF

fig, ax = plt.subplots(figsize=(3.3, 2.6))  # half-height of original

ax.plot(vacf_AA[:, 0]/1e3, vacf_AA[:, 1]*1e6, label='FG', color="black", linestyle='--')
ax.plot(vacf_CG[:, 0]/1e3, vacf_CG[:, 1]*1e6, label='CG', color=VIBGYOR_PAPER["blue"])
ax.plot(vacf_dpd_pll[:, 0]/1e3, vacf_dpd_pll[:, 1]*1e6,
        label="$\\gamma^{\\mathrm{DPD}}_{\\parallel}$", color=VIBGYOR_PAPER["orange"])
ax.plot(vacf_pll[:, 0]/1e3, vacf_pll[:, 1]*1e6,
        label="$\\gamma_{\\parallel}$", color=VIBGYOR_PAPER["green"])
ax.plot(vacf_pd[:, 0]/1e3, vacf_pd[:, 1]*1e6,
        label="$\\gamma_{\\perp}$", color=VIBGYOR_PAPER["pink"])

ax.text(
    -0.12, 1.05, "a)",
    transform=ax.transAxes,
    fontsize=12,
    fontweight='bold',
    va='top',
    ha='left'
)
ax.set_xscale('log')
ax.set_xlim(0.01, 5)
ax.set_xlabel(r'$t\,[\mathrm{ps}]$')
ax.set_ylabel(r'$C_{vv}(t)\,[10^{-3}\mathrm{nm}^2\,\mathrm{ps}^{-2}]$')

ax.legend()

plt.tight_layout()
plt.savefig("vacf.png", dpi=600, bbox_inches="tight")
plt.show()
plt.close()
