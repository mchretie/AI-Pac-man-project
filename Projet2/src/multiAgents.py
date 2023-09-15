# multiAgents.py
# --------------
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


from http.client import BadStatusLine
from xxlimited import foo
from util import manhattanDistance
from game import Directions
from pacman import GameState
import util

from game import Agent



def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, state: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # fetching number of agents
        self.agNum = state.getNumAgents()

        # Returning best move
        return self.minimax(state, self.index, self.depth)[1]


    def minimax(self, state, turn, depth):
        
        # End cases for the search
        # 1. depth reached | 2. Game end
        # returning state value
        if depth == 0 or gameOver(state):
            return self.evaluationFunction(state), None

        # Pacman
        if turn == 0:
            maxEval = -9999
            bestMove = None

            # Iterating through all moves
            for move in state.getLegalActions(0):
                newState = state.getNextState(0, move)
                eval = self.minimax(newState, (turn+1)%self.agNum, depth)[0] # We just need the value that's why [0]

                # Saving best eval and corresponding move
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
            return maxEval, bestMove

        # Ghost
        else:
            minEval = 9999

            # Iterating through all moves 
            for move in state.getLegalActions(turn):
                newState = state.getNextState(turn, move)

                # If next turn ==  Pacman -> call for pacman and depth -1
                if turn == self.agNum-1:
                    eval = self.minimax(newState, 0,  depth-1)[0]
                # Else next ghost
                else:
                    eval = self.minimax(newState, (turn+1), depth)[0]

                # Saving best eval for ghost (no need for their move)
                minEval = min(minEval, eval)
            return minEval, None


# Declared in outside scope to be used by other classes
# Checks if end game situation
def gameOver(state):
    return state.isLose() or state.isWin()
    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, state: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # Fetching number of agents
        self.agNum = state.getNumAgents()

        # Returning best move with alpha -9999 and beta 9999
        return self.minimax(state, self.index, self.depth, -9999, 9999)[1]

    def minimax(self, state, turn, depth, alpha, beta):

        # End cases for the search
        # 1. depth reached | 2. Game end
        # returning state value
        if depth == 0 or gameOver(state):
            return self.evaluationFunction(state), None

        # Pacman
        if turn == 0:
            maxEval = -9999
            bestMove = None

            # Iterating through all moves
            for move in state.getLegalActions(0):
                newState = state.getNextState(0, move)
                eval = self.minimax(newState, (turn+1)%self.agNum, depth, alpha, beta)[0] # We just need the value that's why [0]

                # Saving best eval and corresponding move
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move

                # Updating alpha if needed an checking for pruning
                alpha = max(alpha, eval)
                if beta < alpha:   
                    break                
            return maxEval, bestMove

        # Ghost
        else:
            minEval = 9999

            # Iterating through all moves 
            for move in state.getLegalActions(turn):
                newState = state.getNextState(turn, move)

                # If next turn ==  Pacman -> call for pacman and depth -1
                if turn == self.agNum-1:
                    eval = self.minimax(newState, 0,  depth-1, alpha, beta)[0]
                # Else next ghost                    
                else:
                    eval = self.minimax(newState, (turn+1), depth, alpha, beta)[0]

                # Saving best eval for ghost (no need for their move)
                minEval = min(minEval, eval)

                # Updating alpha if needed an checking for pruning
                beta = min(beta, eval)
                if beta < alpha:
                    break
            return minEval, None


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, state: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        # Fetching number of agents
        self.agNum = state.getNumAgents()

        # Returning expected best move
        return self.expectimax(state, self.index, self.depth)[1]

    def expectimax(self, state, turn, depth):


        # End cases for the search
        # 1. depth reached | 2. Game end
        # returning state value
        if depth == 0 or gameOver(state):
            return self.evaluationFunction( state), None

        # Pacman
        if turn == 0:
            maxEval = -9999
            bestMove = None

            # Iterating through all moves
            for move in state.getLegalActions(0):
                newState = state.getNextState(0, move)
                eval = self.expectimax(newState, (turn+1)%self.agNum, depth)[0]

                # Saving best eval and corresponding move
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move                   
            return maxEval, bestMove

        # Ghost
        else:
            # Probality list
            probaL = []

            # Iterating through all moves 
            for move in state.getLegalActions(turn):
                newState = state.getNextState(turn, move)

                # If next turn ==  Pacman -> call for pacman and depth -1
                if turn == self.agNum-1:
                    eval = self.expectimax(newState, 0,  depth-1)[0]

                # Else next ghost                    
                else:
                    eval = self.expectimax(newState, (turn+1), depth)[0]
                
                # Calculating/updating weight of expectancy node 
                probaL.append(eval)
                res = sum(probaL)/len(probaL)
            return res, None


def betterEvaluationFunction(state: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: 

    I'm using 4 elements.
    - Score
    - Distance of the closest food 
    - Distance to closest capsule
    - Number or food
    (I was expecting to take in account the ghost and their states but these elements seem to be enough for a 6/6)

    
    "*** YOUR CODE HERE ***" """

    # checking for end game events 
    if state.isWin():
        return 99999
    elif state.isLose():
        return -99999

    # Gathering useful info
    # state score, pacman positon, food quantity
    score = state.getScore()
    pacmanPos = state.getPacmanPosition()
    foodNum = state.getNumFood()   

    # Finding shortest food distance out of food list
    foodL = state.getFood().asList()
    bestFoodD = 999999
    for food in foodL:
        tmp = manhattanDistance(pacmanPos, food)
        bestFoodD = min(tmp, bestFoodD)

    # Finding shortest capsules distance and if no capsules than 0 
    capsules = state.getCapsules()
    if not len(capsules):
            bestCapsuleD = 0
    else:
        bestCapsuleD = 999999
        for capsule in capsules:
            tmp = manhattanDistance(pacmanPos, capsule)
            bestCapsuleD = min(bestCapsuleD, tmp)

    # Through trail and error I found these weights to work
    return score + -2 * bestCapsuleD + -1 * bestFoodD + -4 * foodNum

# Abbreviation
better = betterEvaluationFunction
