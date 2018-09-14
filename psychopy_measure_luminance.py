# -*- coding: utf-8 -*-

"""
Psychopy script to present and measure luminance levels (with a light meter).
Press buttons 1 and 2 to move from darker to brighter, or vice verser.
Press button 4 to switch on or off the info for the current intensity level.
"""

# Copyright (C) 2018  Ingo Marquardt & Marian Schneider
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


from psychopy import visual, monitors, core, event
import numpy as np

# %% GENERAL PARAMETERS

# set number of linear steps from black to white
steps = 17

# space linearly
colorArray = np.linspace(-1.0, 1.0, num=steps)

# repeat and reshape array so that it confirms to rgb triplet where r=g=b
colorArray = np.tile(colorArray, 3).reshape(3, -1).T

# %% MONITOR

# set monitor information:
distanceMon = 99
widthMon = 30
PixW = 1920.0  # 1920.0
PixH = 1200.0  # 1080.0

moni = monitors.Monitor('testMonitor', width=widthMon, distance=distanceMon)
moni.setSizePix([PixW, PixH])

# set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(
    size=(PixW, PixH),
    screen=0,
    winType='pyglet',  # winType : None, ‘pyglet’, ‘pygame’
    allowGUI=False,
    allowStencil=False,
    fullscr=True,  # for psychoph lab: fullscr = True
    monitor=moni,
    color = [0, 0, 0],
    colorSpace= 'rgb',
    units='pix',
    blendMode='avg'
    )

# %% STIMULUS

# Squares
testStim1 = visual.GratingStim(
    win=mywin,
    tex=None,
    units='pix',
    size=(PixW, PixH),
    colorSpace='rgb'
    )

# Text
RGBText = visual.TextStim(
    win=mywin,
    color='green',
    height=30,
    units='pix',
    opacity=1,
    pos=(0, -PixH/2+50)
    )

# %% TIME
# give the system time to settle
core.wait(0.5)

# %% RENDER_LOOP

trigCount = 0
textCount = 0
presentation = True

while presentation:

    # set colour
    testStim1.setColor(colorArray[trigCount])
    testStim1.draw()

    # update text text
    StepText = 'Step %s out of %s' % (trigCount+1, steps)
    RGBText.setText('RGB: ' + str(colorArray[trigCount]) + '\n' + StepText)
    RGBText.draw()

    mywin.flip()

    # handle key presses each frame
    for keys in event.getKeys():

        # if 2 was pressed: increase RGB value
        if keys[0] in ['2']:
            if trigCount < steps-1:
                trigCount = trigCount+1

        # if 1 was pressed: decrease RGB value
        if keys[0] in ['1']:
            if trigCount > 0:
                trigCount = trigCount-1

        # if 4 was pressed: toggle RGB value shown/hidden
        if keys[0] in ['4']:
            textCount += 1
            if textCount % 2 == 0:
                RGBText.opacity = 0
                RGBText.draw()

            elif textCount % 2 == 1:
                RGBText.opacity = 1
                RGBText.draw()

        if keys[0] in ['escape', 'q']:
            presentation = False
            mywin.close()
            core.quit()

mywin.close()
core.quit()
