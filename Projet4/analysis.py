# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

from typing import Tuple
import util


def question2a() -> Tuple[float, float, float]:
    
    discount = 0.31 
    noise = 0
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

def question2b()-> Tuple[float, float, float]:
    discount = 0.31
    noise = 0.2
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

def question2c()-> Tuple[float, float, float]:
    discount = 0.32
    noise = 0
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

def question2d()-> Tuple[float, float, float]:
    discount = 0.37
    noise = 0.2
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

def question2e()-> Tuple[float, float, float]:
    discount = 1
    noise = 0.2
    living_reward = 10
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
