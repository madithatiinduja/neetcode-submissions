class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       s =int("".join(map(str,digits)))+1
       return [int(char) for char in str(s)]