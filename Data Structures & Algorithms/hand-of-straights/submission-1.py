class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        

        count = defaultdict(int)

        for h in hand:
            count[h] += 1

        for h in sorted(count.keys()):
            while count[h] > 0:
                for i in range(groupSize):
                    g = h+i
                    if count[g] <= 0:
                        return False
                    count[g] -= 1
        
        return True