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
T = 500.0
Sc = 3.2e-3

nu = T/Sc

# distance from river to observation well 
x = 150.0

# discretization
delta_t = 0.002
num_steps = 60

# response function
response_f = zeros((num_steps), dtype=float)
# input (forcing) function
input_f = zeros((num_steps), dtype=float)
# incremental changes in forcing function
input_inc = zeros((num_steps), dtype=float)
#

step = 0
time = 0.0

# construct the response function throughout the simulation time
while step < num_steps:
    time += delta_t
    response_f[step] = erfc( x / (2 * sqrt( nu * time ) ) )
    step += 1

# dummy system input - sine wave
input_f = sin(arange(2*pi/51, stop=2*pi, step=2*pi/51, dtype='float'))

# divide the forcing function into incremental steps
for i in range(1,len(input_f)):
    input_inc[i] = input_f[i] - input_f[i-1]

# note - full convolution makes the sys_out too big (by num_steps - 1) - only
# use the first num_steps entries. 'same' and 'valid' do not yield the 
# correct result
resp = convolve(input_inc, response_f, mode='full')

plot(input_f)
hold
plot(resp[0:num_steps])
show()

