from valueIterationAgents import ValueIterationAgent
from mdp import MarkovDecisionProcess
import util


class PolicyIterationAgent(ValueIterationAgent):
    def __init__(self, mdp: MarkovDecisionProcess, discount=0.9, iterations=100,value_iteration_tolerance=.01):
        """
        Your policy iteration agent should take an mdp on
        construction, run the indicated number of iterations
        or stop on convergeance and then act according to the
        resulting stored policy.

        Some useful mdp methods you will use:
            mdp.getStates()
            mdp.getPossibleActions(state)
            mdp.getTransitionStatesAndProbs(state, action)
            mdp.getReward(state, action, nextState)
            mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, 0)
        self.policy = {
            state: mdp.getPossibleActions(state)[0]
            if not mdp.isTerminal(state)
            else None
            for state in mdp.getStates()
        }
        self.value_iteration_tolerance = value_iteration_tolerance
        self.runPolicyIteration(iterations)
        pass

    def runPolicyIteration(self, iterations: int):
        """ do NOT modify this function """
        converged = False
        self.iterations_to_converge = 0
        while not converged and self.iterations_to_converge < iterations:
            self.iterations_to_converge += 1
            self.updateValues()
            converged = self.updatePolicy()
        
    def updateValues(self):
        """Update the values until convergeance. Instead of 
        maximizing over the arms when computing new values, 
        you should select the action defined by the agent's 
        current policy stored in self.policy. 
        You can consider that the values converged when the
        biggest change in value is smaller than 
        self.value_iteration_tolerance."""
        

       

        thresholdPass = float('inf')
        
        while thresholdPass > self.value_iteration_tolerance:
            
            thresholdPass = float('-inf')
            Uprime =  self.values.copy()

            for state in self.mdp.getStates():
                
                if self.mdp.isTerminal(state):
                    continue
                
                action = self.policy[state]   

                res1 = self.getQValue(state, action)

                self.values[state] = res1

                tmp = abs( res1 - Uprime[state] )

                thresholdPass = max(tmp, thresholdPass)
        

    def updatePolicy(self):
        """In this method you should update the agent's policy, 
        stored in self.policy, and return a boolean 
        indicating whether the policy has converged."""

        oldPolicy = self.policy.copy()
        #converged = True

        # self.mdp.getStates()

        for state in self.policy:
            self.policy[state] = self.computeActionFromValues(state)

            #if converged and oldPolicy[state]!= None and abs( float(self.getValue[state]) - oldPolicy[state]) > self.value_iteration_tolerance:
                #converged = False

        #return converged
        return oldPolicy == self.policy  
       

    def getPolicy(self, state):
        return self.policy[state]

    def getAction(self, state):
        return self.policy[state]
