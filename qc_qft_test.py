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
from pyquil.gates import *

# Start of regular code

# open a synchronous connection
qvm = api.SyncConnection()

#
# Implement Quantum Fourier Transform from tutorial
#
from math import pi

def qft3(q0, q1, q2):
    p = pq.Program()
    p.inst( H(q2),
            CPHASE(pi/2.0, q1, q2),
            H(q1),
            CPHASE(pi/4.0, q0, q2),
            CPHASE(pi/2.0, q0, q1),
            H(q0),
            SWAP(q0, q2) )
    return p

# Examine program
print(qft3(0, 1, 2))

# Set up state corresponding to [0 1 0 0 0 0 0 0]
print('Calculation 1:')
state_prep = pq.Program().inst(X(0))
add_dummy_qubits = pq.Program().inst(I(1), I(2))
wavf, _ = qvm.wavefunction(state_prep + add_dummy_qubits)
print('PYQUIL State:')
print(wavf)
print

# Combine state and qft
wavf, _ = qvm.wavefunction(state_prep + qft3(0, 1, 2))
print('PYQUIL QFT:')
print(wavf.amplitudes)

# Compare to numpy computation
from numpy.fft import ifft
res = ifft([0,1,0,0,0,0,0,0], norm="ortho")
print
print('numpy IFFT:')
print(res)
print

#
# Now try a different computation:
#

# Set up state corresponding to [0 0 0 1 0 0 0 0]
print('Calculation 2:')
p = pq.Program() # clear existing results
state_prep = pq.Program().inst(X(0)).inst(X(1)).inst(I(2))
###add_dummy_qubits = pq.Program().inst(X(1), X(2))
wavf, _ = qvm.wavefunction(state_prep)
print('PYQUIL State:')
print(wavf)
print

# Combine state and qft
wavf, _ = qvm.wavefunction(state_prep + qft3(0, 1, 2))
print('PYQUIL QFT:')
print(wavf.amplitudes)

# Compare to numpy computation
from numpy.fft import ifft
res = ifft([0,0,0,1,0,0,0,0], norm="ortho")
print
print('numpy IFFT:')
print(res)

#
# Interesting, it seems:  State 001 matches IFFT, but 011 does not.
# Sign differences in convention??
#
#
arg1 = pi/4.0*1j
arg2 = pi*3.0/4.0*1j
n = 8.0
norm = 1.0/np.sqrt(n)

# m=1
m=1
a1 = norm*np.exp(arg1*m)
a2 = norm*np.exp(arg2*m)

print
print('a1 = ', a1)
print('a2 = ', a2)

#
# End of script
#
