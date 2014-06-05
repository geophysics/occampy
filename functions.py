#!/usr/bin/env python

"""
functions.py: functions called during the occampy inversion

"""

# functions used in the runoccam script

def proc_cmd_arg(parameters)
    # reads command arguments and assigns to variables


def get_inputs(parameters)
    # reads input files and creates data matrix


def initialise_params(parameters)
    # set initial values for first iteration


def write_outputs(data,model)
    # write model and response outputs to file


# functions called by the occam script

def construct_matrices(data,parameters)
    # construct the Jacobian matrices W.J.trans(W.J) and W.J.trans(W.D)
    calculate_jacobian(data,parameters)
    construct_WJTWJ()
    construct_WJTWD()

def calc_rms_misfit(data,response)
    # calculate the RMS error between new forward response and data


def calc_penalty_matrix(data,parameters)
    # construct penalty matrix


def update_model(parameters,model,data)
    # run search for new Lagrange multiplier and model
    bracket_minimum_rms(parameters,model,data)
    if parameters.bracket_rms < parameters.rms_tolerance:
        parameters.iteration_mu = parameters.bracket_mu
    else:
        minimise_rms_function(parameters,model,data)
        if parameters.minimise_rms < parameters.rms_tolerance:
            paramaters.iteration_mu = parameters.minimise_mu
        else:
            parameters.stepsize = parameters.stepsize*2
            return
    find_intersect(parameters,model,data)
    calc_roughness(model)
    if parameters.roughness > parameters.last_roughness*1.01:
        print 'Roughness problems, cutting stepsize'
        parameters.stepsize = parameters.stepsize*2
        return
    else:
        print 'Success'
        converging = True

def calc_roughness(model)
    # calculate roughness of new model


def check_convergence(parameters)
    # run checks on convergence and smoothness of model
    

# functions called from functions in this file

def bracket_minimum_rms(parameters,model,data)
    # search for Lagrange multiplier which minimises the RMS misfit
    mu_one = np.log10(parameters.mu_current) - 1
    mu_two = np.log10(parameters.mu_current)

def minimise_rms_function(parameters,model,data)
    # use a golden section search to find the minimum of the function
    # of RMS misfit vs Lagrange multiplier

def find_intersect(parameters,model,data)
    # function to find the point at which a given function reaches
    # a certain value. Used to smooth the model once an RMS in the desired
    # tolerance has been found

def calculate_jacobian()
    # calculate the Jacobian of a matrix

def construct_WJTWJ()
    # constructs the W.J.trans(W.J) matrix, where W.J is the weighted Jacobian

def construct_WJTWD()
    # constructs the W.J.trans(W.D) matrix, where W.J is the weighted Jacobian
    # and D is the data matrix
