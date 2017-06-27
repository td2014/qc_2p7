#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 10:33:58 2017

@author: anthonydaniell
"""
import numpy as np
import random as rn
import os
os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
rn.seed(12345)

# Setup for pyquil config load
os.environ['PYQUIL_CONFIG'] = '/Users/anthonydaniell/Desktop/FilesToStay/Research/QuantumComputing/qc_2p7/.pyquil_config'
# Load pyquil
import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import H

# Start of regular code

# open a synchronous connection
qvm = api.SyncConnection()

#
# Implement Quantum Fourier Transform from tutorial
#

def throw_octahedral_die(q0=0, q1=1, q2=2):
    p = pq.Program()
    p.inst( H(q2),
            H(q1),
            H(q0),
            MEASURE (0,0),
            MEASURE (1,1),
            MEASURE (2,2))
    return p

# Examine program
print(throw_octahedral_die())

wavf, _ = qvm.wavefunction(throw_octahedral_die())

for k,v in wavf.get_outcome_probs().iteritems():
    if v>0.5:
        state=k
        
rollVal = int(state, 2)
print('Dice Roll = ', rollVal+1)
            


#
# End of script
#