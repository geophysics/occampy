#!/usr/bin/env python

import functions as 2D_occam_fn
import occam as main

"""
runoccam.py: the main file to be called for running an Occam inversion.

    Usage: runnoccam INPUT_FILE SETTINGS_FILE

"""


2D_occam_fn.proc_cmd_arg()

data = Data()
model = Model()
parameters = Para()

2D_occam_fn.get_inputs()

2D_occam_fn.initialise_params()

main.occam_loop(data_arrays)

2D_occam_fn.write_outputs()
