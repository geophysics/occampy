#!/usr/bin/env python

"""
occam.py: The main loop that runs during the occampy inversion

"""

import classes.py as *
import functions.py as of

def occam()
	while it <= max_it and del_rms > min_change:
		resp = []
		resp = occam_fwd(data_arrays{'model_0'})
		of.calc_deviation(data_arrays{'data'},resp)
		of.calc_pen_mat(data_arrays{'model_0'},params)
		continue = True
		while continue is True:
			of.calc_new_model()
			of.calc_roughness()
			of.check_if_continue()
		of.commit_new_params()
		of.write_iteration()
