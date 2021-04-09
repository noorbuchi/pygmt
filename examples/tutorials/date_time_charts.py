"""
Plotting Datetime Charts
========================

Plotting datetime charts is handled by :meth:`pygmt.Figure.basemap`.

.. note::

    This tutorial assumes the use of a Python notebook, such as IPython or Jupyter Notebook.
    To see the figures while using a Python script instead, use
    ``fig.show(method="external")`` to display the figure in the default PDF viewer.

    To save the figure, use ``fig.savefig("figname.pdf")`` where ``"figname.pdf"``
    is the desired name and file extension for the saved figure.
"""
# sphinx_gallery_thumbnail_number = 0

import numpy as np
import pygmt

########################################################################################
# Date - Time Formats into `fig.basemap`
# ----------------------
#
# Explanation of supported formats.

########################################################################################
# `numpy.datetime64`


# Code

########################################################################################
# `pandas.DatetimeIndex`

# Code

########################################################################################
# `xarray.DataArray`

# Code

########################################################################################
# Raw date-time in ISO format

# Code

########################################################################################
# Python built-in: `datetime.datetime`

# Code

########################################################################################
# Python built-in: `datetime.date`

# Code

########################################################################################
# Passing Min/Max Time into `region` parameter using `pygmt.info`
# ----------------------
#
# Explanation of supported parameters + bug at #597.

# Code

########################################################################################
# Setting Primary and Secondary Time Axes
# ----------------------
#
# Explanation.

# Code
