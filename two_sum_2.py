class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        x=0
        y=len(numbers)-1

        for i in range(y):
            current_sum= numbers[x] + numbers[y]
            if  current_sum == target:
                return x+1,y+1
            if  current_sum < target:
                x += 1
            else:
                y -=1