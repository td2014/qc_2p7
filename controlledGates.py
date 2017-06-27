#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 10:33:58 2017

Code to generate controlled version of a unitary gate matrix

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
from pyquil.gates import X, Y, Z, CNOT

# Start of regular code

# open a synchronous connection
qvm = api.SyncConnection()

#
# Implement Quantum Fourier Transform from tutorial
#

def controlled(uMatrix):
    
    if uMatrix.shape[0]!=uMatrix.shape[1]:
        print 'Error.  Matrix not square.'
        return -1
    
    cEye = np.eye(uMatrix.shape[0]) # Identity
    cZero = np.zeros(uMatrix.shape)
    
#    print uMatrix
#    print cEye
#    print cZero
    
    newMatrix_upper = np.concatenate( (cEye, cZero), axis=1 )
    newMatrix_lower = np.concatenate( (cZero, uMatrix), axis=1 )
    newMatrix = np.concatenate((newMatrix_upper, newMatrix_lower))
    
    return newMatrix

# Create test matrix and call function
testMatrix = np.array([[0,-1j],[1j,0]])

cMatrix = controlled(testMatrix)

# Display computed matrix
print cMatrix  
print
print
 
#
# Apply to given some wavefunctions
#
p = pq.Program() # clear existing results
p = pq.Program(CNOT(0, 1))
wvf, _ = qvm.wavefunction(p)
print "CNOT|00> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print

p = pq.Program(X(0), CNOT(0, 1))
wvf, _ = qvm.wavefunction(p)
print "CNOT|01> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print

p = pq.Program(X(1), CNOT(0, 1))
wvf, _ = qvm.wavefunction(p)
print "CNOT|10> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print

p = pq.Program(X(0), X(1), CNOT(0, 1))
wvf, _ = qvm.wavefunction(p)
print "CNOT|11> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print
print   
#
# Apply new gate
#
print "New Gate"
print
p = pq.Program() # clear existing results
p = pq.Program().defgate(name="NEW_G", matrix=cMatrix)
p.inst(("NEW_G", 0, 1))
wvf, _ = qvm.wavefunction(p)
print "NEW_G|00> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print

p = pq.Program().defgate("NEW_G", cMatrix)
p.inst(X(0))
p.inst(("NEW_G", 0, 1))
wvf, _ = qvm.wavefunction(p)
print "NEW_G|01> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print

p = pq.Program().defgate("NEW_G", cMatrix)
p.inst(X(1))
p.inst(("NEW_G", 0, 1))
wvf, _ = qvm.wavefunction(p)
print "NEW_G|10> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
print

p = pq.Program().defgate("NEW_G", cMatrix)
p.inst(X(0), X(1))
p.inst(("NEW_G", 0, 1))
wvf, _ = qvm.wavefunction(p)
print "NEW_G|11> = ", wvf
print "With outcome probabilities\n", wvf.get_outcome_probs()
  
#
# End of script
#