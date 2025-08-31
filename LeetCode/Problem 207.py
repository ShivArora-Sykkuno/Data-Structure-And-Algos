from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list =  [[] for _ in range(numCourses)]
        ind = [0 for _ in range(numCourses)]
        for v,u in prerequisites:
            adj_list[v].append(u)
            ind[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        res = []
        while q:
            curr_course = q.popleft()
            res.append(curr_course)
            for adjCourse in adj_list[curr_course]:
                ind[adjCourse] -= 1
                if ind[adjCourse] ==0:
                    q.append(adjCourse)
        if len(res) == numCourses:
            return True
        else:
            return False
