class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        hashmap ={"}":"{" , "]" : "[" , ")":"("}

        for ch in s:
            if ch not in hashmap:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    val = stack.pop()
                    if val != hashmap[ch]:
                        return False
        
        return not stack
        