class Solution:
    def maxArea(self, heights: List[int]) -> int:        
        max_area=0
        n = len(heights)
        l =0
        r= n-1

        while l <r:
            width = r-l
            height = min(heights[l] , heights[r])
            area = width * height 

            max_area = max(area , max_area)

            if heights[l]<heights[r]:
                l=l+1
            elif heights[r] < heights[l]:
                r=r-1
            else:
                r=r-1

        return max_area
        