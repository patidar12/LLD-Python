class Solution:
    def is_matched(self, open, closed):
        if open == "(" and closed != ")":
            return False
        if open == "{" and closed != "}":
            return False
        if open == "[" and closed != "]":
            return False
        return True
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop(-1)
                if not self.is_matched(top, char):
                    return False
        if stack:
            return False
        return True

print(Solution().isValid("(]"))