class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def target(numbers, t, skip):
            # give 2sum = t
            l = 0
            r = len(numbers)-1
            rl,rr = [],[]
            while l < r:
                if l == skip:
                    l+=1
                    continue
                if r == skip:
                    r -=1
                    continue
                if numbers[l] + numbers[r] == t:
                    rl.append(l)
                    rr.append(r)
                    l+=1
                    r-=1
                if numbers[l] + numbers[r] < t:
                    l+=1
                if numbers[l] + numbers[r] > t:
                    r-=1
            return rl,rr

        nums.sort()
     
        res = set()
        for i in range(len(nums)):
            rl,rr = target(nums, -nums[i], i)
            if rl:
                for l,r in zip(rl,rr):
                    res.add(tuple(sorted([nums[i],nums[l],nums[r]])))

        return list(res)


                

        


