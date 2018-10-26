# -*- coding: utf-8 -*-
"""
Given a target luminance level - e.g. 246 cd/m^2 - and the polynomial function
for luminance values obtained from fit_luminance.py, derive the value
that will need to be set for the color argument in the psychopy stimulation
script to obtain the target luminance.
"""

import numpy as np
# from scipy.optimize import minimize

# %% Set parameters

# Target luminance value [cd / m^2]
# Luminance of ‘Pac-Men’ stimulus in Kok & Lange (2014):
varCd = 0.43
# Background luminance in Kok & Lange (2014):
# varCd = 246.0

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


# %%  Calculate psychopy color value

#dicOptm = minimize(funcPoly3,
#                   [0.0],
#                   args=(varA, varB, varC, varD, varCd),
#                   bounds=[(-1.0, 1.0)])
#varPix = dicOptm.x[0]


# %%  Calculate psychopy color value

# Number of x values to evaluate:
varNumSmpls = 10000

# Array for differences between target luminance and luminance for each pixel
# intensity:
vecDiff = np.ones(varNumSmpls)

# Range of possible pixel values:
vecX = np.linspace(-1.0, 1.0, varNumSmpls)

# Loop through pixel values:
for idx01, varTmpX in enumerate(vecX):

    # Luminance for current pixel value:
    varTmpY = funcPoly3(varTmpX, varA, varB, varC, varD)

    # Difference between current luminance and target luminance:
    vecDiff[idx01] = np.abs(varTmpY - varCd)

# Pixel value corresponding to target luminance:
varPix = vecX[np.argmin(vecDiff)]
varPix = np.around(varPix, 2)

print("Target luminance value: " + str(varCd) + " [cd / m^2]")
print("Corresponding psychopy pixel intensity: " + str(varPix))
