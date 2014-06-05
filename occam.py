#!/usr/bin/env python

"""
occam.py: The main loop that runs during the occampy inversion

"""

import * from classes
import functions as 2D_occam_fn

def occam_loop()
    while (parameters.iteration <= parameters.max_iterations and
            parameters.change_in_rms > parameters.rms_change_tolerance):
        response = Data() # initialise response for each iteration
        2D_occam_fn.calc_matrices(data,parameters)
        response.values = occam_fwd(model)
        2D_occam_fn.calc_rms_misfit(model,response)
        2D_occam_fn.calc_penalty_matrix(response,parameters)
        converging = False
        while converging is False:
            2D_occam_fn.update_model(model)
        parameters.commit_values()
        response.write(parameters.response_filename)
        model.write(parameters.model_filename)
