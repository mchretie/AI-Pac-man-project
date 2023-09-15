# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


from typing import Optional

from learningAgents import ValueEstimationAgent
from mdp import MarkovDecisionProcess
import util


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.values = util.Counter()
        self.runValueIteration(iterations)

    def runValueIteration(self, iterations: int):

        states = self.mdp.getStates()

        # iterates through and calls an update on all states
        for i in range(iterations):
            tmp =util.Counter()

            for state in states:
                action = self.getAction(state)

                if action is not None:
                    tmp[state] = self.getQValue(state, action)
                  
            self.values = tmp
            
            

    def getValue(self, state) -> float:
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action) -> float:
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """

        Qval = 0
            
        for TstateVals in self.mdp.getTransitionStatesAndProbs(state, action):
            
            # fetches needed elements
            Tstate, proba = TstateVals
            reward = self.mdp.getReward(state, action, Tstate)
            value = self.getValue(Tstate)

            # applies equation
            Qval += proba * (reward + self.discount * value)
            
        return Qval
        
        

    def computeActionFromValues(self, state) -> Optional[str]:
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        
        if self.mdp.isTerminal(state):
            return None
        else:
            actions = self.mdp.getPossibleActions(state)
            bestValue = float('-inf')
            
            # Iterates through and saves best actions
            for action in actions:
                value = self.getQValue(state, action)

                if value >=  bestValue:
                    bestValue = value
                    bestAction = action

            return bestAction

        


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
