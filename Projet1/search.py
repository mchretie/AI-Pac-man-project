# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from jinja2 import Undefined, UndefinedError
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    util.raiseNotDefined()
    *** YOUR CODE HERE ***"""

    # Initializing
    visited = {}            # Dictionary to keep track of visited
    stack = util.Stack()    # Stack for States   TAKES [state, path]
    currentPath = []        
    emptyStack = False      #flag

    state = problem.getStartState()    # Starting position

    # Main loop DFS
    while (not problem.isGoalState(state)) and (not emptyStack):

        # Save new visit
        if state not in visited:
            visited[state] = currentPath  
        # Looking for potential neighbor states to visit
        for child in problem.expand(state):      
            if child[0] not in visited :
                tmpPath = currentPath + [child[1]]              # Complete path options :
                newState = problem.getNextState(state, child[1])# Getting neighbor state the right way ;)
                stack.push([newState, tmpPath])                 #

        if not stack.isEmpty():              # Just checking
            state, currentPath = stack.pop() # Get next state and its path
        else:
            emptyStack = True

    return currentPath


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.
    *** YOUR CODE HERE ***"""
    # Initializing
    visited = {}            # Dictionary to keep track of visited
    queue = util.Queue()    # State visiting Queue  TAKES [state, path]
    currentPath = []        
    emptyQ = False          # flag
    state = problem.getStartState()      # Starting state   
    visited[tuple(state[:])] = currentPath

    # Main loop
    while (not problem.isGoalState(state)) and (not emptyQ):

        # Saving potential neighbors and their path
        for child in problem.expand(state):
            if tuple(child[0]) not in visited :         # 
                tmpPath = currentPath + [child[1]]      # Temp of path options
                visited[tuple(child[0])[:]] = tmpPath   # Save as visited
                queue.push([child[0], tmpPath])

        if not queue.isEmpty():
            state, currentPath = queue.pop()      # Get next state and its path
        else:
            emptyQ = True
    return currentPath


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Initializing
    visited = {}                            # Dictionary to keep track of visited states, their g(n) and path
    pQueue = util.PriorityQueue()           # PriorityQueue of states
    currentPath = []        
    emptyQ = False                          # flag
    state = problem.getStartState()         # Starting state

    gn = 0 
    hn = heuristic(state, problem)
    priority = gn + hn                              # Cost g(n)+h(n)
    stateDetails = (priority, gn, currentPath)      # Bundling up details
    visited[tuple(state)] = stateDetails            # Save visit

    # Main loop
    while (not problem.isGoalState(state)) and (not emptyQ):

        # Saving potential neighbors and their path
        for child in problem.expand(state):
            # Package up all the details
            currentCost = visited[tuple(state)][1]      # Cost so far 
            stepCost = child[2]                         # Added cost
            gn = currentCost+stepCost 
            hn = heuristic(child[0], problem)       
            newPriority = gn + hn                       # NewPriority
            tmpPath = currentPath + [child[1]]          # New Path
            stateDetails = (newPriority, gn, tmpPath)   # New Bundle

            if tuple(child[0]) not in visited :
                # Save new visit, push state with priority to queue
                visited.update({tuple(child[0]): stateDetails })
                newState = problem.getNextState(state, child[1])
                pQueue.push(newState, newPriority)
            
            # If already visited, check if alternate path has lower cost
            else:
                oldPriority = visited[tuple(child[0])][0]  
                if newPriority < oldPriority:
                    # Update State's shortest path an priority in Queue
                    visited[tuple(child[0])] = stateDetails  
                    pQueue.update(child[0], newPriority)

        if not pQueue.isEmpty():
            state = pQueue.pop()                    # Get next state
            currentPath = visited[tuple(state)][2]  # Get state's path
        else:
            emptyQ = True
    return currentPath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
