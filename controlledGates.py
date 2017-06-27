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
from pyquil.gates import *

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
testMatrix = np.array([[0,1],[1,0]])

cMatrix = controlled(testMatrix)

# Display computed matrix
            
#
# End of script
#