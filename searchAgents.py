from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
import searchAgents
class CornersProblem(search.SearchProblem):
 
  
  def __init__(self, startingGameState):
    
    self.walls = startingGameState.getWalls()
    self.startingPosition = startingGameState.getPacmanPosition()
    top, right = self.walls.height-2, self.walls.width-2 
    self.corners = ((1,1), (1,top), (right, 1), (right, top))

    visited_corners = tuple(self.startingPosition == corner for corner in self.corners)
    return (self.startingPosition, visited_corners)
    
  def isGoalState(self, state):
    
    return all(state[1])
       
  def getSuccessors(self, state):
   
    successors = []
    currentPosition, visited_corners = state
    for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
      x,y = currentPosition
      dx, dy = Actions.directionToVector(action)
      nextx, nexty = int(x + dx), int(y + dy)
      hitsWall = self.walls[nextx][nexty]
      
      if not hitsWall:
        nextPosition = (nextx, nexty)
        new_visited_list = list(visited_corners)
        for i, corner in enumerate(self.corners):
          if nextPosition == corner:
            new_visited_list[i] = True
        
        new_visited_tuple = tuple(new_visited_list)
        successors.append(((nextPosition, new_visited_tuple), action, 1))

    self._expanded += 1
    return successors

  def getCostOfActions(self, actions):
   
    if actions == None: return 999999
    x,y= self.startingPosition
    for action in actions:
      dx, dy = Actions.directionToVector(action)
      x, y = int(x + dx), int(y + dy)
      if self.walls[x][y]: return 999999
    return len(actions)


def cornersHeuristic(state, problem):
  
  corners = problem.corners 
  walls = problem.walls 
  
  
  position, visited_corners = state
  
  unvisited = []
  for i, corner in enumerate(corners):
    if not visited_corners[i]:
      unvisited.append(corner)
      
  if not unvisited:
    return 0

  max_dist = 0
  for corner in unvisited:
    dist = util.manhattanDistance(position, corner)
    if dist > max_dist:
      max_dist = dist
      
  return max_dist



def foodHeuristic(state, problem):
 
  position, foodGrid = state
  
  foodList = foodGrid.asList()
  if not foodList:
    return 0

  max_dist = 0
  for food in foodList:
      dist = util.manhattanDistance(position, food)
      if dist > max_dist:
          max_dist = dist
  return max_dist



  def findPathToClosestDot(self, gameState):
    startPosition = gameState.getPacmanPosition()
    food = gameState.getFood()
    walls = gameState.getWalls()
    problem = AnyFoodSearchProblem(gameState)

    return search.bfs(problem)
  
class AnyFoodSearchProblem(PositionSearchProblem):
  

  def __init__(self, gameState):
    
    self.food = gameState.getFood()

    self.walls = gameState.getWalls()
    self.startState = gameState.getPacmanPosition()
    self.costFn = lambda x: 1
    self._visited, self._visitedlist, self._expanded = {}, [], 0
    
  def isGoalState(self, state):
    
    x,y = state
    
    return self.food[x][y]

