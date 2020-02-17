# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:04:57 2020

@author: Kabelo McKabuza
"""

from astropy.io import fits
import pylab as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Courier New'
rcParams['font.size'] = '16'

image_file = 'ds9.fits'
hdu_list = fits.open(image_file)
data = hdu_list[0].data

plt.imshow(data, cmap = 'gray')
plt.colorbar()
