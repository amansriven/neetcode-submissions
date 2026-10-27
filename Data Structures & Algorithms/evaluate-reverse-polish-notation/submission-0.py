class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        res = 0
        for elem in tokens:
            if elem.isdigit():
                stack.append(int(elem))
                continue
            elif stack:
                num2 = stack.pop()
                num1 = stack.pop()
                if elem == '+':
                    stack.append(num1+num2)
                if elem == '-':
                    stack.append(num1-num2)
                if elem == '*':
                    stack.append(num1*num2)
                if elem == '/':
                    stack.append(num1/num2)

        if stack:
            return stack.pop()
        return 0
