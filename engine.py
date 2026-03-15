import numpy as np
from scipy.optimize import linprog
import time

def calculate_basic_persuasion(benefit, prior):
    """Calculates persuasion for a simple 2-state world."""
    # In a simple nudge, the optimal value is the benefit 
    # if the sender can shift the belief past the threshold (0.5)
    if prior > 0:
        return benefit
    return 0

def solve_complex_persuasion(n_states):
    """
    Demonstrates the computational complexity of Information Design.
    Solves for N states using Linear Programming.
    """
    start_time = time.time()
    
    # Objective: Maximize expected utility for the Sender
    # We create random utilities for each state
    sender_utilities = np.random.rand(n_states)
    
    # Constraints: Probabilities must sum to 1
    c = -sender_utilities  # Negative because linprog minimizes
    A = np.ones((1, n_states))
    b = [1]
    
    res = linprog(c, A_eq=A, b_eq=b, bounds=(0, 1), method='highs')
    
    end_time = time.time()
    runtime = end_time - start_time
    
    return runtime, res.fun * -1 # Return time and the max utility