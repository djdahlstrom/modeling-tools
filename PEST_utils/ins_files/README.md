This folder has scripts related to making PEST instruction files (used to read model outputs).

__make_instruction_file_from_smp.py__ reads a bore sample file and creates an instruction file for it. <br />
By default, it reads the file __bob_obs.dat__. Normally, the name of the input file is given on the command line (see the script).
The results can be checked using the PEST utility INSCHEK as follows: inschek bob_obs.dat.ins bob_obs.dat

