from mantid.simpleapi import *
import numpy as np

import os 

ws = LoadIsawPeaks('data/Natrolite_runs_133752_133812.peaks')

FilterPeaks(
    InputWorkspace=ws,
    OutputWorkspace=ws,
    FIlterVariable='BankName',
    FilterValue=17,
    Operator'=',
    )
