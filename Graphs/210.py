class Solution:
    hasCycle=False
    def topoSort(self,graph,vertex,visited,stack,recStack):
        visited[vertex]=True
        recStack[vertex]=True
        if vertex in graph:
            for neighbour in graph[vertex]:
                if not(visited[neighbour]):
                    self.topoSort(graph,neighbour,visited,stack,recStack)
                elif recStack[neighbour]:
                    self.hasCycle=True
        recStack[vertex]=False
        stack.append(vertex)
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph={}
        self.hasCycle=False
        for prerequisite in prerequisites:
            if prerequisite[0] in graph:
                graph[prerequisite[0]].append(prerequisite[1])
            else:
                graph[prerequisite[0]]=[]
                graph[prerequisite[0]].append(prerequisite[1])
        visited=[False for j in range(numCourses)]
        stack=[]
        recStack=[False for j in range(numCourses)]
        for i in range(numCourses):
            if not visited[i]:
                self.topoSort(graph,i,visited,stack,recStack)
        if self.hasCycle:
            return []
        return stack
        
