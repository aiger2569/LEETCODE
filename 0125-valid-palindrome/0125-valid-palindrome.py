class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        c=""
        for i in s:
            if i.isalnum():
                c+=i
        if c==c[::-1]:
            return True
        return False