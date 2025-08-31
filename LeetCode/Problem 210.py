from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        ind = [0 for _ in range(numCourses)]
        for v, u in prerequisites:
            adj_list[v].append(u) 
            ind[u] += 1

        q = deque()
        res = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        while q:
            curr_course = q.popleft()
            res.append(curr_course)
            for adjCourse in adj_list[curr_course]:
                ind[adjCourse] -=1
                if ind[adjCourse] == 0:
                    q.append(adjCourse)
        if len(res) == numCourses:
            return res[::-1]
        else:
            return []

        