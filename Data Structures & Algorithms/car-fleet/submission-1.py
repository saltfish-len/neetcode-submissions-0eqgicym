class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # can catch before destination
        # sort
        pos_spd = [(p,s) for p,s in zip(position,speed)]
        pos_spd.sort(key = lambda x:x[0], reverse =True)
        time = lambda ps:(target-ps[0])/ps[1]

        fleet_time = None
        count = 0
        for cur in pos_spd:
            cur_arrive = time(cur)
            if not fleet_time or cur_arrive > fleet_time:
                # first car or cannot catch
                fleet_time = cur_arrive
                count+=1
            else:
                # catch
                pass
            
        return count