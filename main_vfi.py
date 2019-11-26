#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:39:26 2019

@author: filip
!git add "main_vfi.py"
!git commit -m "My commit"
!git push origin master.
"""
# libraries
import numpy as np

# Parameters
sigma = 1
alpha = 0.36#p 60 (McCandles)
pk = 1
delta = 0.1 # Standard value
A = 1
beta = 0.98
tol = 1/1000 # convergence criteria.
rho = 1/beta - 1 #Slide 9 lecture 14, Dynamic Macroeconomics
N = 100
# Find the steady state value of capital
K = ((A * alpha) / (pk*(rho + delta))) ** (1/(1-alpha))


# Construct the grid world
kgrid = np.linspace(0.9*K,K,N)

# Make an initial guess on the value function
V0 = np.arange(1.,N+1.)

# Compute best choice of capital tomorrow

# Compute Theta
# Compute Omega

# Construct policy functions
