#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 08:12:18 2017

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

# Program object
p = pq.Program() # clear existing results
coin_flip = pq.Program().inst(H(0)).measure(0, 0)
num_flips = 5

# Run the program object
res = qvm.run(coin_flip, [0], num_flips)
# Display result
print 'res = ', res

# Run again:  Get the wavefunction
coin_flip = pq.Program().inst(H(0)).measure(0,0)
wavf, classical_mem = qvm.wavefunction(coin_flip, classical_addresses=range(9))

# Reprocible (for testing only)
seeded_cxn = api.SyncConnection(random_seed=17)
print(seeded_cxn.run(pq.Program(H(0)).measure(0, 0), [0], 20))
print

seeded_cxn2 = api.SyncConnection(random_seed=17)
# This will give identical output to the above
print(seeded_cxn2.run(pq.Program(H(0)).measure(0, 0), [0], 20))

#
# Implement Quantum Fourier Transform
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

# Set up state corresponding to [0 0 0 1 0 0 0 0]
state_prep = pq.Program().inst(X(0))
add_dummy_qubits = pq.Program().inst(X(1), I(2))
wavf, _ = qvm.wavefunction(state_prep + add_dummy_qubits)
print('PYQUIL State:')
print(wavf)
print

# Combine state and qft
wavf, _ = qvm.wavefunction(state_prep + qft3(0, 1, 2))
print('PYQUIL FFT:')
print(wavf.amplitudes)

# Compare to numpy computation
from numpy.fft import ifft
res = ifft([0,0,0,1,0,0,0,0], norm="ortho")
print
print('numpy FFT:')
print(res)

#
# End of script
#