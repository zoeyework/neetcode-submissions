class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        area =[]
        max_area=0
        while i <j:
            length = abs(j-i)
            height = min(heights[i],heights[j])
            current_area=length*height
            max_area=max(max_area, current_area)
            if heights[i] < heights[j]:
                i=i+1
            else:
                j=j-1 
        return max_area
