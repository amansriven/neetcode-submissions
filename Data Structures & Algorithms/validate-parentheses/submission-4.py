class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != "(":
                    return False
            elif c == ']':
                if not stack or stack.pop() != "[":
                    return False
            elif c == '}' and stack.pop() != '{':
                if not stack or stack.pop() != "{":
                    return False
        return True