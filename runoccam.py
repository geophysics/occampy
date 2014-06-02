#!/usr/bin/env python

import functions.py as of
import occam as *

"""
runoccam.py: the main file to be called for running an Occam inversion

"""


of.proc_cmd_arg()

of.get_inputs()

of.initialise_params()

occam(data_arrays)

of.write_outputs()
