This folder contains scripts related to creating content for a PEST control file. 

__make_PST_file_excerpt_from_smp.py__ reads a bore sample file and writes a portion of the Observation Data Section of a PEST control file. <br />
This script is intended to be run from the DOS command line and takes several arguments, including the number to start with  in sequestially 
numbering the observations associated with a given location. If for example, six other observations are already associated with the 
location name, provide the integer 7 as the 4th command line argument:<br />
>python make_PST_file_excerpt_from_smp.py bob_obs.dat FHS_79 1.3 7
