class Solution:
    def isPalindrome(self, s: str) -> bool:
        res =''
        s=s.lower()
        s=s.replace(" " ,"")
        for char in s:
            if char.isalnum():
                res = res+char
        reverse_s =res[::-1]

        if res ==reverse_s:
            return True
        else:
            return  False
        