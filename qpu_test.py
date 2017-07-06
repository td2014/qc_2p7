#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 08:20:29 2017

QPU processing code.

@author: anthonydaniell
"""
###import numpy as np
###import random as rn
import os
###os.environ['PYTHONHASHSEED'] = '0'
###np.random.seed(42)
###rn.seed(12345)

# Setup for pyquil config load
os.environ['PYQUIL_CONFIG'] = '/Users/anthonydaniell/Desktop/FilesToStay/Research/QuantumComputing/qc_2p7/.pyquil_config_qpu'
# Load pyquil
from pyquil.qpu import QPUConnection, get_info

import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import H

# Start of regular code
print get_info()

# open a connection
###qpuName = ""
###qpu = QPUConnection(qpuName)
###qpu.ping() # checks to make sure the connection is good

#
# Run T1
#
###my_qubit = 5
###res_t1 = qpu.t1(my_qubit)
###wait_for_job(res_t1)
###analog_plot(res_t1)

#
# Run T2
#
###my_qubit = 5
###ramsey_res = qpu.ramsey(my_qubit)
###wait_for_job(ramsey_res)
###analog_plot(ramsey_res)

#
# End of code
#