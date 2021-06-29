"""
Using Recursion and 2 Pointers to swap 
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recur_twopointer(left,right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                recur_twopointer(left+1, right-1)

        recur_twopointer(0, len(s)-1)
        
