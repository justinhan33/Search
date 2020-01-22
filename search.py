# Attribution Information: The Pacman AI projects were developed at UC Berkeley.

"""
In search.py, implemented generic search algorithms will be called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchNode:

    def __init__(self, value, action, parent):
        self.value = value
        self.action = action
        self.parent = parent
        self.actions = []
        self.cost = 0

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
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

    Return a list of actions that reaches the goal.
    """

    fringe = util.Stack()
    visited = []
    solution = []
    startNode = SearchNode(problem.getStartState(), None, None)
    fringe.push(startNode)
    while not fringe.isEmpty():

        curr = fringe.pop()
        if problem.isGoalState(curr.value):
            solution.append(curr.action)
            while curr.parent != startNode:
                solution.append(curr.parent.action)
                curr = curr.parent
            solution.reverse()
            return solution

        elif curr.value not in visited:
            visited.append(curr.value)
            for x in problem.getSuccessors(curr.value):
                fringe.push(SearchNode(x[0], x[1], curr))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    visited = []
    solution = []
    startNode = SearchNode(problem.getStartState(), None, None)
    fringe.push(startNode)
    while not fringe.isEmpty():
        curr = fringe.pop()
        if problem.isGoalState(curr.value):
            solution.append(curr.action)
            if curr.parent == startNode and problem.isGoalState(curr.value):
                return solution
            while curr.parent != None:
                solution.append(curr.parent.action)
                curr = curr.parent
            solution.reverse()
            return solution[1:]
        elif curr.value not in visited:
            visited.append(curr.value)
            for x in problem.getSuccessors(curr.value):
                fringe.push(SearchNode(x[0], x[1], curr))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    visited = []
    solution = []
    startNode = SearchNode(problem.getStartState(), None, None)
    fringe.push(startNode, 0)
    while not fringe.isEmpty():
        curr = fringe.pop()
        if problem.isGoalState(curr.value):
            solution.append(curr.action)
            if curr.parent == startNode and problem.isGoalState(curr.value):
                return solution
            while curr.parent != None:
                solution.append(curr.parent.action)
                curr = curr.parent
            solution.reverse()
            return solution[1:]
        elif curr.value not in visited:
            visited.append(curr.value)
            for neighbor in problem.getSuccessors(curr.value):
                next = SearchNode(neighbor[0], neighbor[1], curr)
                next.actions = curr.actions.copy()
                next.actions.append(next.action)
                if next.actions != None and len(next.actions) != 0:
                    next.cost = problem.getCostOfActions(next.actions)
                else:
                    next.cost = curr.cost
                fringe.push(next, next.cost)
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    visited = []
    solution = []
    startNode = SearchNode(problem.getStartState(), None, None)
    fringe.push(startNode, 0)
    while not fringe.isEmpty():
        curr = fringe.pop()
        if problem.isGoalState(curr.value):
            solution.append(curr.action)
            if curr.parent == startNode and problem.isGoalState(curr.value):
                return solution
            while curr.parent != None:
                solution.append(curr.parent.action)
                curr = curr.parent
            solution.reverse()
            return solution[1:]
        elif curr.value not in visited:
            visited.append(curr.value)
            for neighbor in problem.getSuccessors(curr.value):
                next = SearchNode(neighbor[0], neighbor[1], curr)
                next.actions = curr.actions.copy()
                next.actions.append(next.action)
                if next.actions != None and len(next.actions) != 0:
                    next.cost = problem.getCostOfActions(next.actions) + heuristic(next.value, problem = problem)
                else:
                    next.cost = curr.cost
                fringe.push(next, next.cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
