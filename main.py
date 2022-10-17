import numpy as np
#global variables
BOARD_ROWS = 5
BOARD_COLS = 5
ACTION_N = 5
P_E = 0.5

stateT = np.array([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]])
stateValues = np.zeros([BOARD_ROWS, BOARD_COLS])
action = [[0, 1], [0, -1], [-1, 0], [1, 0], [0, 0]]
tranProb = {
    (tuple(stateT[0]), tuple(stateT[0]), tuple(action[0])): 0
}

def isObsticle(a):
    if np.all(a == [1, 1]) or np.all(a == [2, 1]) or np.all(a == [1, 3]) or np.all(a == [2, 3]):
        return 1
    else:
        return 0

def isNeighbour(s, s_p):

    x = s + np.array([0, 1])
    y = s + np.array([0, -1])
    z = s + np.array([1, 0])
    w = s + np.array([-1, 0])

    if np.all(s_p == x) or np.all(s_p == y) or np.all(s_p == z) or np.all(s_p == w):
        if isObsticle(s_p) == 1:
            return 0
        else:
            return 1
    else:
        return 0

#funtion to calculate transition probabilities
def calculate_TP(state):

    for i in state:
        for a in action:
            for j in state:
                if a == [0, 0]:
                    if np.all(i == j):
                        tranProb[(tuple(i), tuple(j), tuple(a))] = 1
                    else:
                        tranProb[(tuple(i), tuple(j), tuple(a))] = 0
                else:
                    if isNeighbour(i, j) == 1:
                        ai = i+a
                        if np.array_equal(j, ai):
                            tranProb[(tuple(i), tuple(j), tuple(a))] = 1 - P_E
                        else:
                            tranProb[(tuple(i), tuple(j), tuple(a))] = P_E/4
                    else:
                        tranProb[(tuple(i), tuple(j), tuple(a))] = 0

    for s in state:
        for a in action:
            if a != [0, 0]:
                summ = 0
                for n in state:
                    summ = summ + tranProb[(tuple(s), tuple(n), tuple(a))]
                tranProb[(tuple(s), tuple(s), tuple(a))] = 1 - summ

if __name__ == "__main__":
    calculate_TP(stateT)
    print(tranProb)




