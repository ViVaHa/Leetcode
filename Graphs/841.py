class Solution:
    def dfs(self,d,roomNo,visited):
        if visited[roomNo]:
            return
        visited[roomNo]=True
        for neighbour in d[roomNo]:
            self.dfs(d,neighbour,visited)
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms)==0:
            return True
        numOfRooms=len(rooms)
        visited=[False for i in range(len(rooms))]
        d={}
        for i in range(len(rooms)):
            d[i]=rooms[i]
        self.dfs(d,0,visited)
        for i in range(numOfRooms):
            if not(visited[i]):
                return False
        return True
            
        
