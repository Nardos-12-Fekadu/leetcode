class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):

        count = 0

        for num in arr1:
            far = True

            for x in arr2:
                if abs(num - x) <= d:
                    far = False
                    break

            if far:
                count += 1

        return count