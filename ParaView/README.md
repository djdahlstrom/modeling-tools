ParaView is an open-source data analysis and visualization environment. The scripts in this folder facilitate usage of ParaView in 
groundwater flow modeling. Note that ParaView has been applied to unstructured MODFLOW grids (see http://www.pesthomepage.org/getfiles.php?file=gwutil_c.pdf).

Tools and methods applied to data sets in ParaView are known as filters. The `StreamTracer` filter may be used on a grid of hydraulic head values to trace pathlines in a groundwater flow field. Capture zones are thus delimited for pumping wells or groups of such wells.

__pv_traces_to_polylines.py__ is used to convert a series of pathline traces exported from ParaView into polylines in a shapefile. This comes 
up, for example, when tracking particles using the StreamTracer filter to determine flowlines and capture zones in a 
hydraulic head field. <br />
__Dependency__:
shapefile.py available at https://github.com/GeospatialPython/pyshp

See the following URL for more information on ParaView: https://www.paraview.org/
