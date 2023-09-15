    score = state.getScore()
    pacmanPos = state.getPacmanPosition()

    if state.isWin():
        return 99999

    elif state.isLose():
        return -99999

    foodL = state.getFood().asList()
    foodNum = state.getNumFood()   
    bestFoodD = 999999
    for food in foodL:
        tmp = manhattanDistance(pacmanPos, food)
        bestFoodD = min(tmp, bestFoodD)

    
    bestCapsuleD = 999999
    capsules = state.getCapsules()
    for capsule in capsules:
        tmp = manhattanDistance(pacmanPos, capsule)
        bestCapsuleD = min(bestCapsuleD, tmp)


    return score + -1 * bestFoodD + -1 * bestCapsuleD + -4 * foodNum