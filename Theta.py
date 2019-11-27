#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:09:21 2019

@author: filip
"""
'''
function [Theta] = Theta(params)
%Theta Utility going from row i to column j
%   %Theta, slide 13. i are for rows, j for columns
%   Theta is a matrix of utility evaluated at all grid points. Given a point
%   (i) and a choice (j) for next period.
sigma = params(1);
alpha = params(2);
pk = params(3);
rho = params(4);
A = params(5);
delta = params(6);
N = params(7);
K = params(8);

kgrid = linspace(0.9*K,K,N); % Kmin, Kmax, N
Y = A * kgrid'.^alpha;

if sigma == 1
    Theta = log(Y + pk*(1-delta).*kgrid' - pk.*kgrid);
else
    Theta = (1/(1-sigma)) * (Y + pk*(1-delta).*kgrid' - pk.*kgrid)^(1-sigma);
end

% Replace too large values in Theta with large negative numbers
%{
(NB: Be careful that choices satisfy the feasibility constraint. If a node on
the grid for next period capital is not feasible you need to overwrite the
value of the objective function with a large negative n
%} 
FC = (A * kgrid.^alpha)/pk + (1-delta)*kgrid;
Theta(Theta > FC) = -1000;

end
'''
def Theta(params):
    sigma = params(1)
    alpha = params(2)
    pk = params(3)
    rho = params(4)
    A = params(5)
    delta = params(6)
    N = params(7)
    K = params(8)
    
    kgrid = np.linspace(0.9*K,K,N)
    Y = A * kgrid ** alpha
    
    if sigma == 1:
        Theta = math.log(Y + pk * (1-delta)*kgrid - pk * kgrid)
    else:
        Theta = (1/(1-sigma)) * (Y + pk*(1-delta)*kgrid - pk*kgrid)**(1-sigma)
    # Replace too large values in Theta with large negative numbers
    FC = (A * kgrid**alpha)/pk + (1-delta)*kgrid;
    Theta(Theta > FC) = -1000;
    !git add "main_vfi.py"
!git commit -m "My commit"
!git push origin master
        
        
            












    