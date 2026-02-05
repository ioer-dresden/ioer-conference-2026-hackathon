# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: worker_env
#     language: python
#     name: worker_env
# ---

# %% [markdown] editable=true tags=["remove-cell"] slideshow={"slide_type": ""}
# **Install dependencies:** In case this notebook is not running [Carto-Lab Docker](https://cartolab.theplink.org/), the cell below aims to install the needed packages for this notebook. If packages are already available, they will be ignored.

# %% tags=["remove-cell"] editable=true slideshow={"slide_type": ""}
import sys
pyexec = sys.executable
print(f"Current Kernel {pyexec}")
# !../py/modules/pkginstall.sh "{pyexec}" myst-nb

# %% [markdown] slideshow={"slide_type": ""} editable=true
# # Data Retrieval: More Examples will follow

# %% [markdown]
# ```{admonition} Summary
# :class: hint
# We will provide more jump start datasets in the coming weeks.
# ```

# %%
