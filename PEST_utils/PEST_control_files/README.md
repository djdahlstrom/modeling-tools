This folder contains python scripts and supporting files related to creating content for a PEST control file. 

__make_PST_file_excerpt_from_smp.py__ reads a bore sample file and writes a portion of the Observation Data Section of a PEST control file related to the data in the bore sample file. As such, it is assumed that every data point in the bore sample file is to be used as an observation by PEST. If there are more data points than intended or they do not occur at the same times as the model output you with to compare them with, use the PEST utiltily __SMP2SMP__ to interpolate the observed data to the times of the model outputs. <br />
This script is intended to be run from the DOS command line and takes several arguments, including the number to start with  in sequestially 
numbering the observations associated with a given location. If for example, six other observations are already associated with the 
location name, provide the integer 7 as the 4th command line argument:<br />
``python make_PST_file_excerpt_from_smp.py bob_obs.dat FHS_79 1.3 7``
