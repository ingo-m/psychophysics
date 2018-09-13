# -*- coding: utf-8 -*-

"""
Plot and model projector luminance for visual neuroscience experiments.

Projector luminance (measured with a photometer) plotted as a function of
psychopy pixel intensity. Several functions are fitted to the data.

Use @MSchnei's script for the luminance measurement:
https://gist.github.com/MSchnei/bd282b1dbce85431ee61bbd955574279
"""

# Copyright (C) 2018  Ingo Marquardt
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.


# *****************************************************************************
# ***Load modules

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# *****************************************************************************


# *****************************************************************************
# *** Data to plot

# Independent variable data:
vecInd = np.linspace(-1.0, 1.0, num=17)

# NOVA coil measurement 13.09.2018, filter = ND.3
# Dependent variable (measured data), in separat rows for repetitoins of the
# measurement:
vecDep = np.array([[2.1, 4.2, 16.9, 44.5, 96.0, 163.0, 245.0, 347.0, 462.0,
                    577.0, 690.0, 813.0, 935.0, 1060.0, 1180.0, 1290.0,
                    1390.0],
                   [2.15, 4.34, 16.8, 44.4, 95.1, 161.0, 242.0, 346.0, 459.0,
                   572.0, 685.0, 808.0, 930.0, 1050.0, 1180.0, 1290.0,
                   1390.0]])

# Vision coil measurement 13.09.2018, filter = ND.3
# Dependent variable (measured data), in separat rows for repetitoins of the
# measurement:
# vecDep = np.array([[2.2, 4.3, 16.3, 42.5, 90.9, 154.0, 232.0, 329.0, 435.0,
#                     544.0, 653.0, 766.0, 881.0, 997.0, 1110.0, 1220.0, 1310.0],
#                    [2.2, 4.3, 16.2, 42.5, 90.3, 155.0, 232.0, 329.0, 435.0,
#                     545.0, 655.0, 766.0, 881.0, 997.0, 1110.0, 1210.0,
#                     1300.0]])

# Label for x-axis (independent variable):
strLblX = 'Psychopy pixel intensity'

# Label for y-axis (dependent variable):
strLblY = 'Luminance [cd/m^2]'

# Figure title:
strTlt = 'Luminance as a function of psychopy pixel intensity'

# Limits of x-axis:
vecXlim = [-1.1, 1.1]

# Limits of y-axis:
vecYlim = [-10.0, 1500.0]

# Output directory for figures:
strPathOut = '/home/john/Desktop/'

# Figure dimensions:
varSizeX = 1200.0
varSizeY = 1000.0
varDpi = 120.0
# *****************************************************************************


# *****************************************************************************
# *** Functions

def funcExp(varX, varA, varB, varC):
    """Exponential function to be fitted to the data."""
    varOut = varA * np.exp(varB * varX) + varC
    return varOut


def funcLn(varX, varA, varB):
    """Logarithmic function to be fitted to the data."""
    varOut = varA * np.log(varX) + varB
    return varOut


def funcPoly2(varX, varA, varB, varC):
    """2nd degree polynomial function to be fitted to the data."""
    varOut = (varA * np.power(varX, 2) +
              varB * np.power(varX, 1) +
              varC)
    return varOut


def funcPoly3(varX, varA, varB, varC, varD):
    """3rd degree polynomial function to be fitted to the data."""
    varOut = (varA * np.power(varX, 3) +
              varB * np.power(varX, 2) +
              varC * np.power(varX, 1) +
              varD)
    return varOut


def funcPow(varX, varA, varB, varC, varD):
    """Power function to be fitted to the data."""
    varOut = (varA * np.power((varX + varB), varC) + varD)
    return varOut
# *****************************************************************************


# *****************************************************************************
# *** Preparations

# Calculate average of dependent variable:
vecDepAvg = np.mean(vecDep, axis=0)

# Calculate standard deviations of dependent variable:
vecStd = np.std(vecDep, axis=0)
# *****************************************************************************


# *****************************************************************************
#  Exponential model fitting:

# Fit the model to the exponential function:
vecExpModelPar, vecExpModelCov = curve_fit(funcExp, vecInd, vecDepAvg)

# Calculate fitted values:
vecFittedExp = funcExp(vecInd,
                       vecExpModelPar[0],
                       vecExpModelPar[1],
                       vecExpModelPar[2])

# Create string for model parameters of exponential function:
varTmpA = np.around(vecExpModelPar[0], 0)
varTmpB = np.around(vecExpModelPar[1], 2)
varTmpC = np.around(vecExpModelPar[2], 0)
strModelExp = 'y = ' + \
              str(varTmpA) + \
              ' e ^ ( ' + \
              str(varTmpB) + \
              ' * x ) + ' + \
              str(varTmpC)
# *****************************************************************************


# *****************************************************************************
# *** Logarithmic model fitting

# Fit the model to the logarithmic function:
vecLnModelPar, vecLnModelCov = curve_fit(funcLn, vecInd, vecDepAvg)

# Calculate fitted values:
vecFittedLn = funcLn(vecInd,
                     vecLnModelPar[0],
                     vecLnModelPar[1])

# Create string for model parameters of exponential function:
varTmpA = np.around(vecLnModelPar[0], 0)
varTmpB = np.around(vecLnModelPar[1], 0)
strModelLn = 'y = ' + \
             str(varTmpA) + \
             ' * ln(x) + ' + \
             str(varTmpB)
# *****************************************************************************


# *****************************************************************************
# *** Polynomial model fitting 2nd degree

# Fit the model to the 2nd degree polynomial function:
vecPoly2ModelPar, vecPoly2ModelCov = curve_fit(funcPoly2, vecInd, vecDepAvg)

# Calculate fitted values:
vecFittedPoly2 = funcPoly2(vecInd,
                           vecPoly2ModelPar[0],
                           vecPoly2ModelPar[1],
                           vecPoly2ModelPar[2])

# Create string for model parameters of exponential function:
varTmpA = np.around(vecPoly2ModelPar[0], 2)
varTmpB = np.around(vecPoly2ModelPar[1], 2)
varTmpC = np.around(vecPoly2ModelPar[2], 2)
strModelPoly2 = 'y = ' + \
                str(varTmpA) + \
                ' * x^2 + ' + \
                str(varTmpB) + \
                ' * x + ' + \
                str(varTmpC)
# *****************************************************************************


# *****************************************************************************
# *** Polynomial model fitting 3rd degree

# Fit the model to the 3rd degree polynomial function:
vecPoly3ModelPar, vecPoly3ModelCov = curve_fit(funcPoly3, vecInd, vecDepAvg)

# Calculate fitted values:
vecFittedPoly3 = funcPoly3(vecInd,
                           vecPoly3ModelPar[0],
                           vecPoly3ModelPar[1],
                           vecPoly3ModelPar[2],
                           vecPoly3ModelPar[3])

# Create string for model parameters of exponential function:
varTmpA = np.around(vecPoly3ModelPar[0], 1)
varTmpB = np.around(vecPoly3ModelPar[1], 1)
varTmpC = np.around(vecPoly3ModelPar[2], 1)
varTmpD = np.around(vecPoly3ModelPar[3], 1)
strModelPoly3 = 'y = ' + \
                str(varTmpA) + \
                ' * x^3 + ' + \
                str(varTmpB) + \
                ' * x^2 + ' + \
                str(varTmpC) + \
                ' * x + ' + \
                str(varTmpD)
# *****************************************************************************


# *****************************************************************************
# *** Power function fitting

# Fit the model to the 3rd degree polynomial function:
vecPowModelPar, vecPowModelCov = curve_fit(funcPow, vecInd, vecDepAvg)

# Calculate fitted values:
vecFittedPow = funcPow(vecInd,
                       vecPowModelPar[0],
                       vecPowModelPar[1],
                       vecPowModelPar[2],
                       vecPowModelPar[3])

# Create string for model parameters of exponential function:
varTmpA = np.around(vecPowModelPar[0], 1)
varTmpB = np.around(vecPowModelPar[1], 1)
varTmpC = np.around(vecPowModelPar[2], 1)
varTmpD = np.around(vecPowModelPar[3], 1)
strModelPow = 'y = ' + \
              str(varTmpA) + \
              ' * (x + ' + \
              str(varTmpB) + \
              ') ^ ' + \
              str(varTmpC) + \
              ' + ' + \
              str(varTmpD)
# *****************************************************************************


# *****************************************************************************
# *** Create plots

# List with model predictions:
lstModPre = [vecFittedExp,
             vecFittedLn,
             vecFittedPoly2,
             vecFittedPoly3,
             vecFittedPow]

# List with model parameters:
lstModPar = [strModelExp,
             strModelLn,
             strModelPoly2,
             strModelPoly3,
             strModelPow]

# We create one plot per function:
for idxPlt in range(0, len(lstModPre)):

    # Create figure:
    fig01 = plt.figure(figsize=((varSizeX * 0.5) / varDpi,
                                (varSizeY * 0.5) / varDpi),
                       dpi=varDpi)

    axs01 = fig01.add_subplot(111)

    # Line colour:
    vecClr = np.divide(np.array([56.0, 132.0, 184.0]), 255.0)
    vecClrSd = np.divide(np.array([250.0, 138.0, 53.0]), 255.0)

    # Plot depth profile for current input file:
    plt01 = axs01.plot(vecInd,
                       vecDepAvg,
                       color=vecClr,
                       alpha=0.9,
                       label='Mean (SD)',
                       linewidth=5.0,
                       antialiased=True)

    # Plot error shading:
    plot02 = axs01.fill_between(vecInd,  #noqa
                                np.subtract(vecDepAvg,
                                            vecStd),
                                np.add(vecDepAvg,
                                       vecStd),
                                alpha=0.2,
                                edgecolor=vecClr,
                                facecolor=vecClr,
                                linewidth=0,
                                antialiased=True)

    # Plot model prediction:
    plt03 = axs01.plot(vecInd,
                       lstModPre[idxPlt],
                       color=vecClrSd,
                       alpha=0.9,
                       label=lstModPar[idxPlt],
                       linewidth=3.0,
                       antialiased=True)

    # Limits of the x-axis:
    # axs01.set_xlim([np.min(vecInd), np.max(vecInd)])
    axs01.set_xlim([vecXlim[0], vecXlim[1]])

    # Limits of the y-axis:
    axs01.set_ylim([vecYlim[0], vecYlim[1]])

    # Which y values to label with ticks:
    vecYlbl = np.linspace(0, vecYlim[1], num=4, endpoint=True)
    # Round:
    # Set ticks:
    axs01.set_yticks(vecYlbl)

    # Which x values to label with ticks:
    vecXlbl = np.linspace(vecXlim[0], vecXlim[1], num=3, endpoint=True)
    # Round:
    vecXlbl = np.around(vecXlbl, decimals=0)
    # Set ticks:
    axs01.set_xticks(vecXlbl)

    # Adjust labels:
    axs01.tick_params(labelsize=16)
    axs01.set_xlabel(strLblX, fontsize=13)
    axs01.set_ylabel(strLblY, fontsize=13)
    # axs01.set_title(strTlt, fontsize=13)

    # Add legend:
    axs01.legend(loc=0, prop={'size': 9})

    # Add vertical grid lines:
    axs01.xaxis.grid(which=u'major',
                     color=([0.2, 0.2, 0.2]),
                     linestyle=':',
                     linewidth=0.2)

    # Add horizontal grid lines:
    axs01.yaxis.grid(which=u'major',
                     color=([0.2, 0.2, 0.2]),
                     linestyle=':',
                     linewidth=0.2)

    # Reduce framing box:
    axs01.spines['top'].set_visible(False)
    axs01.spines['right'].set_visible(False)
    axs01.spines['bottom'].set_visible(True)
    axs01.spines['left'].set_visible(True)

    # Make plot & axis labels fit into figure (this may not always work,
    # depending on the layout of the plot, matplotlib sometimes throws a
    # ValueError ("left cannot be >= right").
    try:
        plt.tight_layout(pad=0.5)
    except ValueError:
        pass

    # Save figure:
    fig01.savefig((strPathOut + 'plot_' + str(idxPlt) + '.png'),
                  dpi=varDpi,
                  facecolor='w',
                  edgecolor='w',
                  transparent=False,
                  frameon=None)

    # Close figure:
    plt.close(fig01)
# *****************************************************************************
