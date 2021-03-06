import queue

myMap = {
    "Arad": {
        "Zerind": { "cost": 75 },
        "Timisoara": { "cost": 118 },
        "Sibiu": { "cost": 140 }
    },
    "Zerind": {
        "Oradea": { "cost": 71 },
        "Arad": { "cost": 75 }
    },
    "Timisoara": {
        "Lugoj": { "cost": 111 },
        "Arad": { "cost": 118 }
    },
    "Sibiu": {
        "Fagaras": { "cost": 99 },
        "Rimnicu Vilcea": { "cost": 80 },
        "Oradea": { "cost": 151 },
        "Arad": { "cost": 140 }
    },
    "Oradea": {
        "Sibiu": { "cost": 151 },
        "Zerind": { "cost": 71 }
    },
    "Lugoj": {
        "Mehadia": { "cost": 70 },
        "Timisoara": { "cost": 111 }
    },
    "Fagaras": {
        "Bucharest": { "cost": 211 },
        "Sibiu": { "cost": 99 }
    },
    "Rimnicu Vilcea": {
        "Pitesti": { "cost": 97 },
        "Craiova": { "cost": 146 },
        "Sibiu": { "cost": 99 }
    },
    "Mehadia": {
        "Drobeta": { "cost": 75 },
        "Lugoj": { "cost": 70 }
    },
    "Pitesti": {
        "Bucharest": { "cost": 101 },
        "Rimnicu Vilcea": { "cost": 97 },
        "Craiova": { "cost": 138 }
    },
    "Craiova": {
        "Pitesti": { "cost": 138 },
        "Rimnicu Vilcea": { "cost": 146 },
        "Drobeta": { "cost": 120 }
    },
    "Drobeta": {
        "Craiova": { "cost": 120 },
        "Mehadia": { "cost": 75 }
    },
    "Bucharest": {
        "Fagaras": { "cost": 211 },
        "Pitesti": { "cost": 101 },
        "Giurgiu": { "cost": 90 },
        "Urziceni": { "cost": 85 }
    },
    "Giurgiu": {
        "Bucharest": { "cost": 90 }
    },
    "Urziceni": {
        "Bucharest": { "cost": 85 },
        "Hirsova": { "cost": 98 },
        "Vaslui": { "cost": 142 }
    },
    "Hirsova": {
        "Eforie": { "cost": 70 },
        "Urziceni": { "cost": 98 }
    },
    "Vaslui": {
        "Iasi": { "cost": 92 },
        "Urziceni": { "cost": 142 }
    },
    "Iasi": {
        "Neamt": { "cost": 87 },
        "Vaslui": { "cost": 92 }
    },
    "Neamt": {
        "Iasi": { "cost": 87 }
    }
}

heuristic = {
    "Arad": 366,
    "Zerind": 374,
    "Timisoara": 329,
    "Sibiu": 253,
    "Oradea": 380,
    "Lugoj": 244,
    "Fagaras": 176,
    "Rimnicu Vilcea": 193,
    "Mehadia": 241,
    "Pitesti": 100,
    "Craiova": 160,
    "Drobeta": 242,
    "Bucharest": 20,
    "Giurgiu": 77,
    "Urziceni": 10,
    "Hirsova": 0,
    "Eforie": 161,
    "Vaslui": 199,
    "Iasi": 226,
    "Neamt": 234
}

def showResult(previous, start, goal):
    curCity = goal # Truy v???t t??? ??i???m ????ch v??? ??i???m b???t ?????u
    print('Result:', curCity, end=' ')
    while curCity != start:
        curCity = previous[curCity]
        print('->', curCity, end=' ')

def showResultWithAttr(previous, start, goal, attr='total_cost'):
    curCity = goal # Truy v???t t??? ??i???m ????ch v??? ??i???m b???t ?????u
    print('Result:', (curCity, previous[curCity][attr]), end=' ')
    while curCity != start:
        curCity = previous[curCity]['from']
        print('->', (curCity, previous[curCity][attr]), end=' ')

def showStep(counter, q, previous, attr='total_cost'):
    print('%d. {' % counter, end=' ')
    i = 0
    lenQ = len(q)
    for v in q:
        i += 1
        if (i < lenQ):
            print((v, previous[v][attr], previous[v]['from']), end=', ')
        else:
            print((v, previous[v][attr], previous[v]['from']), end=' ') 
    print('}')

def aweSomeSort(array, previous, sortBy='total_cost'): # QuickSort (python version)
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = previous[array[0]][sortBy]
        for city in array:
            cost = previous[city][sortBy]
            if cost < pivot:
                less.append(city)
            if cost == pivot:
                equal.append(city)
            if cost > pivot:
                greater.append(city)
        return aweSomeSort(less, previous, sortBy) + equal + aweSomeSort(greater, previous, sortBy) # to??n t??? n???i m???ng
    else:  
        return array

def GBFS(start, goal):
    q = queue.deque()
    q.append(start)

    previous = [] # kh???i t???o previous ki???u dictionary
    for city in myMap.keys():
        previous.append((city, {'from': None, 'heuristic': heuristic[city]}))
    previous = dict(previous)

    counter = 0
    while 1:
        counter += 1
        showStep(counter, q, previous, 'heuristic') # Show c??c b?????c th???c hi???n thu???t to??n

        curCity = q.popleft() # dequeue
    
        if curCity == goal:
            print('Success!')
            showResultWithAttr(previous, start, goal, 'heuristic')
            return True # T??m th???y goal
    
        for city in myMap[curCity].keys(): # C??c th??nh ph??? c?? th??? ??i ?????n ???????c t??? th??nh ph??? hi???n t???i
            if previous[city]['from'] == None: # N???u ch??a ??i qua th??nh ph??? n??y
                q.append(city) # Th??m v??o h??ng ?????i
                previous[city]['from'] = curCity # L??u l???i d???u v???t
        

        if len(q) == 0:
            print('Fail!')
            return False # Kh??ng th??? ??i ?????n goal t??? start
        q = queue.deque(aweSomeSort(q, previous, 'heuristic'))

def AStar(start, goal):
    q = queue.deque() # kh???i t???o queue
    q.append(start)  # enqueue

    previous = [] # kh???i t???o previous ki???u dictionary
    for city in myMap.keys():
        previous.append((city, {'from': None, 'total_cost': heuristic[city]}))
    previous = dict(previous)

    counter = 0
    while 1:
        counter += 1
        showStep(counter, q, previous) # Show c??c b?????c th???c hi???n thu???t to??n
        curCity = q.popleft() # enqueue (????y c??ng l?? ph???n t??? nh??? nh???t v?? ???? s???p x???p queue t??ng d???n)

        if curCity == goal:
            print('Success!')
            showResultWithAttr(previous, start, goal)
            return True # T??m th???y goal
    
        curCityTotalCost = previous[curCity]['total_cost'] - heuristic[curCity] # Chi ph?? ????? ??i t??? start ?????n curCity
    
        if curCity != goal:
            for city in myMap[curCity].keys(): # C??c th??nh ph??? c?? th??? ??i ?????n ???????c t??? curCity
                cityTotalCost = previous[city]['total_cost'] # Chi ph?? ???????c t??nh ??? b?????c tr?????c ????
                totalCost = myMap[curCity][city]['cost'] + curCityTotalCost + heuristic[city] # Chi ph?? ????? ??i t??? start -> curCity -> city 
        
                # N???u ch??a ??i qua th??nh ph??? n??y ho???c chi phi ??i t??? start -> curCity -> city t???t h??n chi ph?? tr?????c ????
                if previous[city]['from'] == None or totalCost < cityTotalCost :
                    if q.count(city) != 0: # N???u ???? c?? city n??y trong h??ng ?????i th?? x??a n?? ??i
                        q.remove(city)
                    q.append(city) # Th??m v??o h??ng ?????i
                    previous[city]['from'] =  curCity # L??u l???i d???u v???t
                    previous[city]['total_cost'] = totalCost # C???p nh???t l???i chi ph?? m???i

        if len(q) == 0:
            print('Fail!')
            return False # Kh??ng th??? ??i ?????n goal t??? start
        q = queue.deque(aweSomeSort(q, previous)) # S???p x???p l???i h??ng ?????i t??ng d???n theo total_cost

start = "Arad"
goal = "Hirsova"
print('Greedy Best First Search Arap-> Hirsova')
GBFS(start,goal)
print('A* Search Arap->Hirsova')
AStar(start,goal)
