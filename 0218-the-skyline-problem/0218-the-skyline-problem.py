from collections import defaultdict, deque
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        cumulated_buildings = defaultdict(list)
        heapa, heapb = [], []
        heapq.heapify(heapa)
        heapq.heapify(heapb)
        for building in buildings:
            src, dst, height = building
            cumulated_buildings[src].append(height)
            cumulated_buildings[dst].append(-height)
        keys = list(cumulated_buildings.keys())
        keys.sort()
        output= []
        cur_height = 0
        for key in keys:
            #FIXME2, in the case of same boxes.
            cumulated_buildings[key].sort(key= lambda x: abs(x))
            for value in cumulated_buildings[key]:
                if value > 0:
                    heapq.heappush(heapa, -value)
                else:
                    if value == -cur_height:
                        heapq.heappop(heapa)
                        while heapb and heapb[0]== heapa[0]:
                            heapq.heappop(heapa)
                            heapq.heappop(heapb)
                        cur_height = 0
                    else:
                        heapq.heappush(heapb, value)
            if heapa and cur_height < -heapa[0]:
                output.append([key, -heapa[0]])
                cur_height = -heapa[0]
            elif not heapa:
                output.append([key, 0])
                cur_height = 0

        #FIXME!!!
        new_output = [] 
        tmp = -1
        for i in range(len(output)):
            if i == 0:
                new_output.append(output[i])
                tmp = output[i][1]
            if output[i][1] != tmp:
                new_output.append(output[i])
                tmp =output[i][1]

        if new_output[-1][1]!=0:
            new_output.append([key, 0])
        return new_output