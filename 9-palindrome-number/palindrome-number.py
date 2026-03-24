class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
           
        v=str(x)[::-1]
        if x<0:
            return False  
        
       
        elif int(v) == x:
            return True
        
        else:
            return False
            
            