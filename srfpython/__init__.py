from tetedenoeud import *
from srfpython.Herrmann.Herrmann import dispersion, dispersion_1, dispersion_2, groupbywtm, igroupbywtm
from srfpython.depthdisp.depthmodels import depthmodel1D, depthmodel, depthmodel_from_mod96string, \
    depthmodel_from_mod96, depthmodel_from_arrays, depthspace
from srfpython.depthdisp.dispcurves import Claw, Ulaw, surf96reader_from_surf96string, surf96reader, freqspace
from srfpython.inversion.metropolis2 import metropolis
from srfpython.utils import Timer

#test line