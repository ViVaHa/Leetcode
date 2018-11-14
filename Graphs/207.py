class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        outdegree=[0 for j in range(numCourses)]
        indegree=[[] for j in range(numCourses)]
        for prerequisite in prerequisites:
            outdegree[prerequisite[0]]+=1 
            indegree[prerequisite[1]].append(prerequisite[0])
        from collections import deque
        q=deque()
        for i in range(numCourses):
            if outdegree[i]==0:
                q.append(i)
        vertices=0
        while len(q)>0:
            vertex=q.pop()
            vertices+=1
            for neighbour in indegree[vertex]:
                outdegree[neighbour]-=1
                if outdegree[neighbour]==0:
                    q.append(neighbour)
        return vertices==numCourses
            
            
            
