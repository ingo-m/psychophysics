# -*- coding: utf-8 -*-
"""
Given a target contrast level - e.g. 0.05 contrast - and the polynomial
function for luminance values obtained from fit_luminance.py, derive the value
that will need to be set for the color argument in the psychopy stimulation
script as to obtain the target contrast.
"""

import numpy as np

# %% Set parameters

# set target contrast value
trgCntr = 0.05

# set fitted values for function
b0 = 431.3
b1 = 839.3
b2 = 227.0
b3 = -190.2


def calc_cntr(x, b0, b1, b2, b3):
    """Calculate contrast for given parameters of a polynomical function."""
    # get intensity
    I1 = b3 * np.power(x, 3) + b2 * np.power(x, 2) + b1 * x + b0
    I2 = b3 * np.power(-x, 3) + b2 * np.power(-x, 2) + b1 * -x + b0

    # calculate contrast
    cntr = (I1 - I2) / (I1 + I2)

    return cntr

# %%  Calculate psychopy color value
tempdiff = np.ones(10000)
for ind, x in enumerate(np.linspace(0, 1, 10000)):
    cntr = calc_cntr(x, b0, b1, b2, b3)
    tempdiff[ind] = np.abs(cntr - trgCntr)

out_x = np.linspace(0, 1, 10000)[np.argmin(tempdiff)]
out_x = np.round(out_x, 2)

print("Given the target value: " + str(trgCntr))
print("Psychopy should be set to: " + str(-out_x) + " and " + str(out_x))
