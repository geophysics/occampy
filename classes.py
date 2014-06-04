#!/usr/bin/env python

"""
classes.py: class definitions for occampy

"""

class Model():
    """
    Model class.
    Methods: initialisation, write model output file
    Attributes: geometry, values
    
    """


class Data():
    """
    Response class for synthetic and measured data. 
    Methods: write response output file
    Attributes: stations, errors, values

    """
class Para():
    """
    Paramaters-class.
    Methods: populate parameters, update parameters, output parameters to log
    Attributes: previous RMS, current RMS, target RMS, iteration number,
    max iterations, current Lagrange multiplier, previous Lagrange multiplier,
    step-size, debug level, current roughness, previous roughness, 
    convergence state, data file name, output filenames
	
    """
