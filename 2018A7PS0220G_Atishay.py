import random

mutateProb_8q = 0.5
mutateProb_tsp = 0.5

def findFitness_tsp(state , initial):

    fitness = 0
    for i in range(13):
        g1 = state[i]
        g2 = state[i + 1]
        fitness = fitness + initial[g1][g2]
    fitness = fitness + initial[state[13]][state[0]]


    return fitness

def mutate_tsp(state):
    i = random.randint(0,13)
    v = random.randint(0,13)
    
    temp = state[i]
    state[i] = state[v]
    state[v] = temp
    



def randomPick_tsp(fitness):
    
    sumFitness = sum(fitness)
    while True:
        for i in range(20):
            if random.random() < fitness[i] / sumFitness:
                return i
    

def largest_tsp(fitness): 
  
  
    m = 0

    for i in range(1, 20): 
        if fitness[i] < fitness[m]: 
            m = i 
    return m
def reproduce_tsp(states, fitness, x, y):
    
  
    l = random.randint(0, 14)
    
    m = random.randint(0 , 14)
    
    if l > m :
        temp = l
        l = m
        m = temp
    aa = [-1]*14
    aa1 = []
    res = []
    for i in range(14):
        if i >= l and i <= m:
            aa1.append(states[x][i])
            aa[i] = states[x][i]
    
    for i in range(14):
        b=1
        for j in range(len(aa1)):
            if states[y][i]==aa1[j]:
                b = 0

        if b == 1 :
            res.append(states[y][i])


    k=0

    for i in range(l):
        aa[i]=res[k]
        k = k + 1
    i = m + 1
    while i<14:
        aa[i]=res[k]
        i = i + 1
        k = k + 1
    




    return aa

def nextGen_tsp(states, fitness , initial):

    children = []
    
    while len(children) < 20:

        first = largest_tsp(fitness)
        second = first
        while first == second:
            second = randomPick_tsp(fitness)
        children.append(reproduce_tsp(states, fitness, first, second))

        ff = findFitness_tsp(children[-1] , initial)

        if ff > 100 and random.random() < mutateProb_tsp:
            mutate_tsp(children[-1])

    return children
        


def main_tsp():
    
    initial = [[100 for _ in range(14)] for _ in range(14)]
    
    initial[0][0] = 0
    initial[1][1] = 0
    initial[2][2] = 0
    initial[3][3] = 0
    initial[4][4] = 0
    initial[5][5] = 0
    initial[6][6] = 0
    initial[7][7] = 0
    initial[8][8] = 0
    initial[9][9] = 0
    initial[10][10] = 0
    initial[11][11] = 0
    initial[12][12] = 0
    initial[13][13] = 0
    initial[1][13] = .13
    initial[13][1] = .13
    initial[5][13] = .9
    initial[13][5] = .9
    initial[7][13] = .17
    initial[13][7] = .17
    initial[8][13] = .6
    initial[13][8] = .6
    initial[9][13] = .5
    initial[13][9] = .5
    initial[5][12] = .26
    initial[12][5] = .26
    initial[10][12] = .24
    initial[12][10] = .24
    initial[11][12] = .4
    initial[12][11] = .4
    initial[0][11] = .12
    initial[11][0] = .12
    initial[5][11] = .6
    initial[11][5] = .6
    initial[6][11] = .18
    initial[11][6] = .18
    initial[9][11] = .16
    initial[11][9] = .16
    initial[3][10] = .3
    initial[10][3] = .3
    initial[5][10] = .37
    initial[10][5] = .37
    initial[6][10] = .55
    initial[10][6] = .55
    initial[0][9] = .2
    initial[9][0] = .2
    initial[7][9] = .56
    initial[9][7] = .56
    initial[1][8] = .4
    initial[8][1] = .4
    initial[2][8] = .2
    initial[8][2] = .2
    initial[4][8] = .18
    initial[8][4] = .18
    initial[1][7] = .19
    initial[7][1] = .19
    initial[0][6] = .15
    initial[6][0] = .15
    initial[2][5] = .4
    initial[5][2] = .4
    initial[3][5] = .21
    initial[5][3] = .21
    initial[2][4] = .22
    initial[4][2] = .22
    initial[2][3] = .6
    initial[3][2] = .6
    fitness = [1 for _ in range(20)]
   
    states = [[i for i in range(14)] for _ in range(20)]
    cost = 0
    for j in range(13):
        cost = cost + initial[j][j+1]
    cost = cost + initial[13][0]
    fitness = [cost for _ in range(20)]
    #print(findFitness_tsp([10, 12, 11, 6, 0, 9, 13, 7, 1, 8, 4, 2, 5, 3],initial))
    generation = 0
    
    while min(fitness) > 3.74 and generation < 10000: 
        states = nextGen_tsp(states, fitness , initial)
        generation += 1
        fitness = [findFitness_tsp(i , initial) for i in states]
        print("\nGENERATION :: {}\n".format(generation))
        print('TSP Best Fitness Value in generation : ' , "\t" , min(fitness)) 
        for tt in range(20):
            if(findFitness_tsp(states[tt] , initial) == min(fitness)):
                pol.append(states[tt])
        for rr in pol:
            if(findFitness_tsp(rr , initial) == min(fitness)):
                print("TSP Best Solution till now:" , rr)
                break;        
    return generation
    

def findFitness_8q(state):

    fitness = 29
    rows = [0 for _ in range(8)]
    diagonal1 = [0 for _ in range(15)]
    diagonal2 = [0 for _ in range(15)]

    for i in range(8):
        cur = state[i]
        rows[cur] += 1
        diagonal1[cur + i] += 1
        diagonal2[7 + cur - i] += 1
    for rr in rows:
        fitness -= (rr * (rr - 1) // 2)
    for d1 in diagonal1:
        fitness -= (d1 * (d1 - 1) // 2)
    for d2 in diagonal2:
        fitness -= (d2 * (d2 - 1) // 2)

    return fitness


def mutate_8q(state):
    child = state
    inw = findFitness_8q(state)
    #print(inw)
    prs = []
    for i in range(8):
        for j in range(8):
            k = child[i]
            child[i] = j
            ue = findFitness_8q(child)
            prs.append(ue)
            child[i] = k 
    hh = max(prs)
    #print(prs)
    #print(hh)
    if(inw == hh):
        index = random.randint(0,7)
        value = random.randint(0,7)
        state[index] = value 
    else:
        for d in range(64):
            if(hh == prs[d]):
                break       
    #print(d)
        re = d // 8
    #print(re)
        state[re] = d % 8
    # print(state[re])
    # print(findFitness(state))

def randomPick_8q(fitness):
    
    sumF = sum(fitness)
    koke = True
    while koke:
        for i in range(20):
            if random.random() < fitness[i] / sumF:
                return i
    

def largest_8q(fitness): 
  
    
    m = 0
    for i in range(1, 20): 
        if fitness[i] > fitness[m]: 
            m = i 
    return m
def reproduce_8q(states, fitness, first, second):

    caa = random.randint(0, 7)

    p = states[first][0:caa] + states[second][caa:8]
    return p
def nextGen_8q(states, fitness):

    childs = []
    while len(childs) < 20:
        first = largest_8q(fitness)
        second = first
        while first == second:
            second = randomPick_8q(fitness)
        childs.append(reproduce_8q(states, fitness, first, second))

        fofchild = findFitness_8q(childs[-1])
        if fofchild < 29 and random.random() < mutateProb_8q:
            mutate_8q(childs[-1])

    return childs
        


def main_8q():
    
    states_8q = [[0 for _ in range(8)] for _ in range(20)]
    fitness_8q = [1 for _ in range(20)]
    #print(fitness)

    generation_8q = 0

    while max(fitness_8q) < 29:
        
        states_8q = nextGen_8q(states_8q, fitness_8q)
        generation_8q += 1
        fitness_8q = [findFitness_8q(i) for i in states_8q]
        print("\nGENERATION :: {}\n".format(generation_8q))
        print('8 QUEEN Best Fitness Value :' , "\t" , max(fitness_8q)) 
        for tt in range(20):
            if(findFitness_8q(states_8q[tt]) == max(fitness_8q)):
                pol.append(states_8q[tt])
        for rr in pol:
            if(findFitness_8q(rr) == max(fitness_8q)):
                print("8 QUEEN Best Solution till now:" , rr)
                break;
    return generation_8q


if __name__=="__main__":

    val = input("PRESS 1 FOR TSP OR ANYTHING FOR 8 QUEEN ")
    if(val == '1') :
        pol = []
        main_tsp()
    else:
        pol = []
        main_8q()
   

    