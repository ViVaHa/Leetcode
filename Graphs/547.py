class Solution:
    def dfs(self,graph,visited,vertex):
        if visited[vertex]:
            return 
        visited[vertex]=True
        for neighbour in graph[vertex]:
            if not(visited[neighbour]):
                self.dfs(graph,visited,neighbour)
        
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        graph={}
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]==1:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i]=[]
                        graph[i].append(j)
        visited=[False for j in range(len(M))]
        components=0
        for i in range(len(M)):
            if not(visited[i]):
                self.dfs(graph,visited,i)
                components+=1
        return components
                        
