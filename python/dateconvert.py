"""
Date format conversion module.
"""
from __future__ import absolute_import
import astropy.time

def MJD_to_ISOT(mjd):
    """
    Convert from MJD to ISOT format.
    """
    date = astropy.time.Time(mjd, format='mjd')
    date.format = 'isot'
    return date.value

def ISOT_to_MJD(isot):
    """
    Convert from ISOT to MJD format.
    """
    date = astropy.time.Time(isot, format='isot')
    date.format = 'mjd'
    return date.value
