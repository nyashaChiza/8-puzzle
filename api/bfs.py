from collections import deque
import sys
import time
import random

"""

Nyasha Chizampeni
Reg Number: H170209v
Title: AI Lab 1 8 Puzzle

|States|:
	It describes the location of each numbered tiles and the blank tile.

|Initial State|: 
	We can start from any state as the initial state.
|Actions|:
	Here, actions of the blank space is dened, i.e., either left, right, up or down
|Transition Model|:
	It returns the resulting state as per the given state and actions.
|Goal test|:
	It identies whether we have reached the correct goal-state.
	 goal_state = [
        0, 1, 2,
		3, 4, 5,
		6, 7, 8,
         ]
|Path cost|:
	The path cost is the number of steps in the path where the cost of each step is 1
"""


class Solver(object):
    def __init__(self, initNode):
        self.initNode = initNode
        self.searchType = 'bfs'
        self.frontier = deque([initNode])
        self.expandedSet = set([initNode.state])
        self.goal = '0,1,2,3,4,5,6,7,8'
        self.path_to_goal = []
        self.goalFound = False
        self.nodes_expanded = 0
        self.max_search_depth = 0
        self.start_time = 0
        self.end_time = 0
        self.max_ram_usage = 0


    def exchange(self, board, n_bi, new_bi):
        new_board = board[:]
        new_board[n_bi] = board[new_bi]
        new_board[new_bi] = '0'
        return new_board


    def heuristic(self, node):
        for i in range(len(node.board)):
            X = abs(i // 3 - node.board.index(str(i))// 3)
            Y = abs(i % 3 - node.board.index(str(i))% 3)
            d = X + Y
            node.h = d + node.h
        node.h = node.h + node.depth
        return node


    def run(self):
        self.start_time = time.time()
        while len(self.frontier) > 0:
            node = self.frontier.popleft()
            self.goal_test(node)
            if self.goalFound:
                return

        return print('no solution')

    def goal_test(self, node):
        if node.state == self.goal:
            self.goalFound = True
            self.end_time = time.time()
            return self.success(node)
        else:
            self.nodes_expanded += 1
            return self.exNodes(node)


    def exNodes(self, node):
        n_b = node.board
        n_bi = node.board.index('0')

        if n_bi - 3 >= 0:
            self.addNode(Node(self.exchange(n_b, n_bi, n_bi - 3), node, 'Up'))
        if n_bi + 3 <= 8:
            self.addNode(Node(self.exchange(n_b, n_bi, n_bi + 3), node, 'Down'))
        if n_bi % 3 - 1 >= 0:
            self.addNode(Node(self.exchange(n_b, n_bi, n_bi - 1), node, 'Left'))
        if n_bi % 3 + 1 < 3:
            self.addNode(Node(self.exchange(n_b, n_bi, n_bi + 1), node, 'Right'))

        
    def addNode(self, newNode):
        if newNode.state not in self.expandedSet:
            self.expandedSet.add(newNode.state)
            self.frontier.append(newNode)
            self.max_search_depth = max(newNode.depth, self.max_search_depth)
            
    def success(self, node):
        global successfulPath 
        successfulPath = self.getPath(node)
        print('computational time:', self.end_time - self.start_time)
       

    def getPath(self, node):
        while node.parent:
            self.path_to_goal.append(node.action)
            node = node.parent
        self.path_to_goal.reverse()
        return self.path_to_goal




class Node(object):
    def __init__(self, board, parentNode, action):
        self.state = ','.join(board)
        self.board = board
        self.h = 0

        if parentNode == False:
            self.parent = False
            self.depth = 0
            self.action = ''
        else:
            self.parent = parentNode
            self.depth = parentNode.depth + 1
            self.action = action

    def __str__(self):
        return self.state

def play_game(state):
    board = []
    for num in state:
        board.append(str(num))
    print('initial board: ', board)
    initNode = Node(board, False, '') 
    mySolver = Solver(initNode) 
    mySolver.run()
    print(successfulPath)

