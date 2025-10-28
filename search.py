import util 

class SearchProblem:

  
  def getStartState(self):
    
     util.raiseNotDefined()
    
  def isGoalState(self, state):
    
     util.raiseNotDefined()

  def getSuccessors(self, state):
    
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
    
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  
  fringe = util.Stack()
  visited = set()
  
  # Each item in the fringe is a tuple: (state, path_to_state)
  fringe.push((problem.getStartState(), []))
  
  while not fringe.isEmpty():
    currentState, actions = fringe.pop()
    
    if currentState in visited:
      continue
      
    visited.add(currentState)
    
    if problem.isGoalState(currentState):
      return actions
      
    for successor, action, stepCost in problem.getSuccessors(currentState):
      newActions = actions + [action]
      fringe.push((successor, newActions))
      
  return [] 

def breadthFirstSearch(problem):
  
  fringe = util.Queue()
  visited = set()

  fringe.push((problem.getStartState(), []))
  visited.add(problem.getStartState())

  while not fringe.isEmpty():
    currentState, actions = fringe.pop()

    if problem.isGoalState(currentState):
        return actions

    for successor, action, stepCost in problem.getSuccessors(currentState):
        if successor not in visited:
            visited.add(successor)
            newActions = actions + [action]
            fringe.push((successor, newActions))
            
  return [] 

def uniformCostSearch(problem):
  
  fringe = util.PriorityQueue()
  visited = set()

  
  fringe.push((problem.getStartState(), [], 0), 0)

  while not fringe.isEmpty():
      currentState, actions, currentCost = fringe.pop()

      if currentState in visited:
          continue

      visited.add(currentState)

      if problem.isGoalState(currentState):
          return actions

      for successor, action, stepCost in problem.getSuccessors(currentState):
          newActions = actions + [action]
          newCost = currentCost + stepCost
          fringe.push((successor, newActions, newCost), newCost)
          
  return [] 


def nullHeuristic(state, problem=None):
  
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  
  fringe = util.PriorityQueue()
  visited = set()
  startState = problem.getStartState()
  fringe.push((startState, [], 0), 0 + heuristic(startState, problem))
  
  while not fringe.isEmpty():
    currentState, actions, currentCost = fringe.pop()

    if currentState in visited:
        continue
    
    visited.add(currentState)

    if problem.isGoalState(currentState):
        return actions
    
    for successor, action, stepCost in problem.getSuccessors(currentState):
        newActions = actions + [action]
        newCost = currentCost + stepCost
        priority = newCost + heuristic(successor, problem)
        fringe.push((successor, newActions, newCost), priority)
        
  return [] 
    
