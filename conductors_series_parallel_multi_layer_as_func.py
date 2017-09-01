'''

script to calculate effective hydraulic conctivity for a layered sequence in:
- series (layering normal to flow direction), and
- parallel (layering parallel to flow direction)

based on:
script to calculate effective horizontal and vertical hydraulic
conductivity based on the approach using the Hydrogeologic-unit Flow Package

Anderman and Hill, 2000.

MODFLOW-2000, THE U.S. GEOLOGICAL SURVEY
MODULAR GROUND-WATER MODEL. 
DOCUMENTATION OF THE HYDROGEOLOGIC-UNIT
FLOW (HUF) PACKAGE
By EVAN R. ANDERMAN1 and MARY C. HILL2
U.S. GEOLOGICAL SURVEY
Open-File Report 00-342

see also eqtn. 49, p. 5-12 in MF88 doc

edited by djd 8/28/2017

'''

def kx_kz_vcont(units, result):
    # return result of kx or kz
    # initialize variables
    total_tk = 0.0  # total combined thickness of units
    T = 0.0         # transmissivity of units (conductors in parallel
    denom = 0.0     # denominator of expression for conductors in series

    for i in units:
        # implement formulas from HUF documentation:
        # Equation 1 with a multiplier m_i of 1.0
        total_tk += i[0]
        T += i[1] * i[0]
        # denominator of Equation 5 
        denom += i[0] / i[1]
    # if requested, convert transmissivity to Kx
    if result == 'kx':
        kx = T / total_tk
        return kx
    # otherwise convert conductance to Kz
    elif result == 'kz':
        kz = total_tk / denom
        return kz
    # otherwise convert conductance to vcont
    elif result == 'vcont':
        #kz = total_tk / denom
        #vcont = kz / total_tk
        vcont = 1.0 / denom
        return vcont

# input file list of lists, each list represents one layer, has entry for thickness, entry for
# hydraulic conductivity, in consistent units
# 
assumed_tk = 2.5


# 1e-7 cm/s = 2.8346456E-4 ft/day
#
units = [ \
    # layer 1
    [ 0.2*assumed_tk, 98.0], \
    # layer 2
    [ 0.4*assumed_tk, 0.028], \
    # layer 3
    [ 0.2*assumed_tk, 98.0], \
    # layer 4
    [ 0.2*assumed_tk, 980.0], \
    ]

print 'effective K in parallel = ', str(kx_kz_vcont(units, 'kx'))
print 'effective K in series = ', str(kx_kz_vcont(units, 'kz'))
print 'vcont = ', str(kx_kz_vcont(units, 'vcont'))
