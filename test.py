from mantid.simpleapi import *
import numpy as np

import os

pws = LoadIsawPeaks('data/Natrolite_runs_133752_133812.peaks', )

FilterPeaks(
    InputWorkspace="pws",
    OutputWorkspace="pws_intensity",
    FIlterVariable='Intensity',
    FilterValue=100,
    Operator='>',
)

FilterPeaks(
    InputWorkspace="pws",
    OutputWorkspace="pws_bank7",
    BankName='bank7',
    Criterion='=',
)

FilterPeaks(
    InputWorkspace="pws",
    OutputWorkspace="pws_intensity_bank7",
    FIlterVariable='Intensity',
    FilterValue=10,
    Operator='>',
    BankName='bank7',
    Criterion='=',
)