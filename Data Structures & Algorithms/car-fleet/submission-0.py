class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n =len(position)

        time =[0] *n

        for i in range(n):
            time[i] = (target-position[i]) / speed[i]
        
        cars = sorted(zip(position , time) , reverse=True)

        fleets =0
        fleet_time =0

        for i in range(n):
            current_time =cars[i][1]

            if current_time>fleet_time:
                fleets+=1
                fleet_time = current_time
        
        return fleets

            

        
        