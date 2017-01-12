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

class Node:
    """
    This class is the node data structure for a search problem. It holds the
    current state, its parent and the cost of the action done from the
    last state.
    """
    def __init__(self, state, partialPath):
        self.state = state
        self.partialPath = partialPath


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
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Your DFS implementation goes here

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    frontier = util.Stack()
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []
    frontier.push(Node(startState, []))
    explored = set()
    frontierSet = set()
    frontierSet.add(startState)

    while not frontier.isEmpty():
        # print "FRONTIER IS", frontier
        curNode = frontier.pop()
        frontierSet.remove(curNode.state)
        explored.add(curNode)
        # print "successors are ", problem.getSuccessors(curNode.state)
        for s in problem.getSuccessors(curNode.state):
            successor, action, cost = s
            if (successor not in explored) and (successor not in frontierSet):
                newpath = list(curNode.partialPath)
                newpath.append(action)
                if problem.isGoalState(successor):
                    return newpath
                else:
                    # print "added a new path", newpath
                    frontier.push(Node(successor, newpath))
                    frontierSet.add(successor)

    raise Exception("THERE IS NO RESULTS") #need to find something to return

    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Your BFS implementation goes here. Like for DFS, your 
    search algorithm needs to return a list of actions that 
    reaches the goal.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Your UCS implementation goes here. Like for DFS, your 
    search algorithm needs to return a list of actions that 
    reaches the goal.
    """
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Your A* implementation goes here. Like for DFS, your 
    search algorithm needs to return a list of actions that 
    reaches the goal. heueristic is a heuristic function - 
    you can see an example of the arguments and return type
    in "nullHeuristic", above.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
