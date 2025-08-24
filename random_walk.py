#!/usr/bin/env python3
"""random_walk.py - simulación de marcha aleatoria 1D"""
# minimal content for reproduction (full script provided earlier in this workspace)
import numpy as np
def simulate_random_walk(N, trials=1, rng=None):
    if rng is None:
        rng = np.random.default_rng()
    steps = rng.integers(0, 2, size=(trials, N), endpoint=False)
    steps = steps * 2 - 1
    return steps.sum(axis=1)
