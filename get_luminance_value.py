# -*- coding: utf-8 -*-
"""
Given a psychopy pixel intensity value (between -1 and +1), calculate the
corresponding luminance level (in cd/m^2), based on the polynomial function
obtained from fit_luminance.py.
"""

import numpy as np
# from scipy.optimize import minimize


# %% Set parameters

# Pixel intensity:
varPix = -1.0

# Fitted parameter values:
varA = -195.9
varB = 246.3
varC = 887.4
varD = 454.4


def funcPoly3(varX, varA, varB, varC, varD):
    """3rd deg. polynomial function, relating luminance to pixel intensity."""

    varOut = (varA * np.power(varX, 3.0)
              + varB * np.power(varX, 2.0)
              + varC * np.power(varX, 1.0)
              + varD)

    return varOut


# %%  Calculate luminance

# Luminance for current pixel value:
varCd = funcPoly3(varPix, varA, varB, varC, varD)

varCd = np.around(varCd, 2)

print("Psychopy pixel intensity (between -1 and +1): " + str(varPix))
print("Corresponding luminance: " + str(varCd) + " [cd / m^2]")
