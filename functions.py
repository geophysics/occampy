#!/usr/bin/env python

"""
functions.py: functions called during the occampy inversion

"""

# functions used in the runoccam script

def proc_cmd_arg(Para)
	# reads command arguments and assigns to variables


def get_inputs(Para)
	# reads input files and creates data matrix


def initialise_params(Para)
	# set initial values for first iteration


def write_outputs(Resp.synth,Model)
	# write model and response outputs to file


# functions called by the occam script

def calc_jtj(Resp.data)
	# construct the matrices WJTWJ and WJTWD, where WJ is the matrix of partials, WD is the weighted data


def calc_deviation(Resp.data,Resp.synth)
	# calculate the RMS error between new forward response and data


def calc_pen_matrix(Resp.data,Para)
	# construct penalty matrix


def calc_new_model(Para)
	# run search for new Lagrange multiplier and model


def calc_roughness(Model.values)
	# calculate roughness of new model


def check_if_continue(Para)
	# run checks on convergence and smoothness of model



# functions called from functions in this file

def minbrk()
	# search for Lagrange multiplier which minimises the RMS misfit
