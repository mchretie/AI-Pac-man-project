def something(state):


    pos = state.getPacmanPosition()
    currentScore = scoreEvaluationFunction(state)

    if state.isLose(): 
        return -float("inf")
    elif state.isWin():
        return float("inf")

    # food distance
    foodlist = state.getFood().asList()
    manhattanDistanceToClosestFood = min(map(lambda x: util.manhattanDistance(pos, x), foodlist))
    distanceToClosestFood = manhattanDistanceToClosestFood

    # number of big dots
    # if we only count the number fo them, he'll only care about
    # them if he has the opportunity to eat one.
    numberOfCapsulesLeft = len(state.getCapsules())
    
    # number of foods left
    numberOfFoodsLeft = len(foodlist)
    
    # ghost distance

    # active ghosts are ghosts that aren't scared.
    scaredGhosts, activeGhosts = [], []
    for ghost in state.getGhostStates():
        if not ghost.scaredTimer:
            activeGhosts.append(ghost)
        else: 
            scaredGhosts.append(ghost)

    def getManhattanDistances(ghosts): 
        return map(lambda g: util.manhattanDistance(pos, g.getPosition()), ghosts)

    distanceToClosestActiveGhost = distanceToClosestScaredGhost = 0

    if activeGhosts:
        distanceToClosestActiveGhost = min(getManhattanDistances(activeGhosts))
    else: 
        distanceToClosestActiveGhost = float("inf")
    distanceToClosestActiveGhost = max(distanceToClosestActiveGhost, 5)
        
    if scaredGhosts:
        distanceToClosestScaredGhost = min(getManhattanDistances(scaredGhosts))
    else:
        distanceToClosestScaredGhost = 0 # I don't want it to count if there aren't any scared ghosts

    outputTable = [["dist to closest food", -1.5*distanceToClosestFood], 
                    ["dist to closest active ghost", 2*(1./distanceToClosestActiveGhost)],
                    ["dist to closest scared ghost", 2*distanceToClosestScaredGhost],
                    ["number of capsules left", -3.5*numberOfCapsulesLeft],
                    ["number of total foods left", 2*(1./numberOfFoodsLeft)]]

    score = 1    * currentScore + \
            -1.5 * distanceToClosestFood + \
            -2    * (1./distanceToClosestActiveGhost) + \
            -2    * distanceToClosestScaredGhost + \
            -20 * numberOfCapsulesLeft + \
            -4    * numberOfFoodsLeft
    return score