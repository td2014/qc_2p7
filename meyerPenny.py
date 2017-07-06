#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 10:33:58 2017

Code to implement Meyer-Penny exploration.

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
from pyquil.gates import X, Y, Z, CNOT, H, I

# Start of regular code

# open a synchronous connection
qvm = api.SyncConnection()

###Pseudo Code:

###H(0)  # qu-bit 0 for decision
###Measure 0 [0]  Get output of decision
###X(1)
###H(1)
###CNOT(1,0)  # CNOT based on result of random experiment on qu-bit zero
###H(1)
###Measure 1,[1]  # Resulting state →  Should be heads because qu-bit 1 is in superposition state.

#
# Implement Decision Branches
#

decision_qb = 1
penny_qb = 0
decision_cr = 1 # decision classical register
penny_cr = 0

p = pq.Program() # clear
p.inst(H(decision_qb))
p.inst(X(penny_qb))
p.inst(H(penny_qb))
p.measure(decision_qb,decision_cr)
p.inst(CNOT(decision_cr,penny_qb))
p.inst(H(penny_qb))
p.measure(penny_qb,penny_cr)

# output program
print(p)
# Run and check registers
print qvm.run(p, [penny_cr]) 

#
# Apply to given some wavefunctions
#
###p = pq.Program() # clear existing results
###p = pq.Program(CNOT(0, 1))
###wvf, _ = qvm.wavefunction(p)
###print "CNOT|00> = ", wvf
###print "With outcome probabilities\n", wvf.get_outcome_probs()
###print

###p = pq.Program(X(0), CNOT(0, 1))
###wvf, _ = qvm.wavefunction(p)
###print "CNOT|01> = ", wvf
###print "With outcome probabilities\n", wvf.get_outcome_probs()
###print

#
# End of script
#