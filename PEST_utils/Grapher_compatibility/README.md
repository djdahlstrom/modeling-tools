PEST bore sample files store time-series data, such as time-drawdown or time-elevation data from wells. These text files contain the following information in columns:
Location
Date
Time
Value 
[an optional extra column - if an 'x' occurs here, the data point is ignored by PEST utilities]

As created by the various PEST utilties, the file is space-delimited. As such, Grapher will read the date and time into separate columns, so graphs showing variation over time cannot be readily made using these files.

The utility __make_bore_sample_grapher_compatible_cmd_arg.py__ reads a bore sample file and writes out a version that is tab-delimited with the following columns:
Location
Date+Time
Value
[extra character if it ocurred in the original]

If multiple locations occur in the input file, each is written to a separate bore sample file. The output file(s) are compatible with Grapher in that the date and time will be parsed together, allowing graphs to be made of the values without further manipulation.
