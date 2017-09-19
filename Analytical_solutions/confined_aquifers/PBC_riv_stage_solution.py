from scipy import zeros, arange, sqrt, sin, pi, convolve
from scipy.special import erfc
from pylab import plot, hold, show

'''
Script to implement the solution of Pinder, Bredehoeft, Cooper for the response 
of heads in a semi-infinite, confined aquifer to river stage fluctuation 
using convolution. 

Pinder, G. F., J. D. Bredehoeft, and H. H. Cooper Jr. (1969), Determination of 
Aquifer Diffusivity from Aquifer Response to Fluctuations in River Stage, 
Water Resources Research, Vol. 5, No. 4, p. 850–855.

[Abstract](http://onlinelibrary.wiley.com/doi/10.1029/WR005i004p00850/abstract)

Variables<br />
Name | Description (units)
-------------|---------------------------------------------------------------
T  | Aquifer transmissivity (L^2/T)
Sc | Aquifer storage coefficient (unitless)
nu | Aquifer transmissivity (L^2/T)
x  | Distance from river bank to observation well 

djdahlstrom

'''

# aquifer parameters in consistent units
T = 1000.0
Sc = 1.0e-3

nu = T/Sc

# distance from river to observation well 
x = 200.0

# discretization
delta_t = 0.001
num_steps = 50

# response function
resp_f = zeros((num_steps), dtype=float)
sys_in = zeros((num_steps), dtype=float)
sys_inc = zeros((num_steps), dtype=float)
#

step = 0
time = 0.0
converged = 'False'

# construct the response function
while converged == 'False' and step < num_steps:
    time += delta_t
    resp_f[step] = erfc( x / (2 * sqrt( nu * time ) ) )
##    #tried to get fancy and save computations if nearly 1
##    if resp_f[step] > 0.999999:
##        # converged on 1 for response function - set rest of value to 1
##        for i in range(step,num_steps):
##            resp_f[i] = 1.0
##        converged = 'True'    
    step += 1

# dummy system input - sine wave
sys_in = sin(arange(2*pi/51, stop=2*pi, step=2*pi/51, dtype='float'))

# need to divide sys_in into incremental steps
for i in range(len(sys_in)):
    if i == 0:
        sys_inc[i] = sys_in[i]
    else:
        sys_inc[i] = sys_in[i] - sys_in[i-1]

# note - full convolution makes the sys_out too big (by num_steps - 1) - only
# use the first num_steps entries. 'same' and 'valid' do not yield the 
# correct result
sys_out = convolve(sys_inc, resp_f, mode='full')

plot(sys_in)
hold
plot(sys_out[0:num_steps])
show()

