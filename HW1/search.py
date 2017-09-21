# In collaboration with Ingrid Hermanrud
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
    sequence of moves will be incorrect, so only use this for tinyMaze...
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    visited = []  # Nodes visited
    stack = util.Stack() #Using a stack so that when a node is popped it is the last node that was pushed to the stack.
    stack.push((problem.getStartState(), []))  # Pushing coordinate and how to get there to the stack.
                                               # For the root node is "how to get there" an empty list.

    while not stack.isEmpty():
        node, directions = stack.pop()

        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node): # Checking if the current node is the goal state, if so return the directions
                return directions

            # Looping through the successors of the current node, pushing the coordinates of the successor with
            # the required action to reach the successor

            for successor in problem.getSuccessors(node):
                coordinate = successor[0]
                direction = successor[1]
                newDirections = directions + [direction]
                stack.push((coordinate, newDirections))


def breadthFirstSearch(problem):
    visited = []  # List of coordinates visisted
    queue = util.Queue() # Using a stack so that when a node is popped it is the first node that was pushed to the queue.
    queue.push((problem.getStartState(), []))  # Pushing coordinate and how to get there to the queue.
                                               # For the root node is "how to get there" an empty list.

    while not queue.isEmpty():
        node, directions = queue.pop()

        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node): # Checking if the current node is the goal state, if so return the directions
                return directions

            # Looping through the successors of the current node, pushing the coordinates of the successor with
            # the required action to reach the successor
            for successor in problem.getSuccessors(node):
                coordinate = successor[0]
                direction = successor[1]
                newDirections = directions + [direction]
                queue.push((coordinate, newDirections))


def uniformCostSearch(problem):
    "Search the node of least total cost first. "

    # Running UCS is the same as running A* Search with a null heuristic,
    # so simplify the calls by just using aStarSearch.
    return aStarSearch(problem)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    visited = []  # Visited nodes
    pqueue = util.PriorityQueue() # Using a priorityqueue to be able to pop the node with the lowest estimated path cost.
    # priorirty queue = item,p priority. here, the g(n) = 0, so only add h(n)
    pqueue.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))

    while pqueue:
        node, directions = pqueue.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node): # Checking if the current node is the goal state, if so return the directions
                return directions

            # Looping through the successors of the current node, pushing the coordinates of the successor with
            # the required actions to reach the successor and the path cost.
            for successor in problem.getSuccessors(node):
                coordinate = successor[0]
                direction = successor[1]
                # appending the action from current node to successor to
                #  the list of all actions required from root node to current node
                newDirections = directions + [direction]
                # f(n) = g(n) + h(n)
                newCost = problem.getCostOfActions(newDirections) + heuristic(coordinate, problem)
                pqueue.push((coordinate, newDirections), newCost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch