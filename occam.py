#!/usr/bin/env python

"""
occam.py: The main loop that runs during the occampy inversion

"""

import classes.py as *
import functions.py as of

def occam()
	while Para.it <= Para.max_it and Para.del_rms > Para.min_change:
		of.calc_jtj(Resp.data)
		Resp.synth = occam_fwd(Model.values)
		of.calc_deviation(Model.values,Resp.synth)
		of.calc_pen_mat(Resp.data,Para)
		continue = False
		while continue is False:
			of.calc_new_model()
			of.calc_roughness()
			of.check_if_continue()
		Para.iteration()
		Resp.write(resp_fn)
		Model.write(model_fn)
