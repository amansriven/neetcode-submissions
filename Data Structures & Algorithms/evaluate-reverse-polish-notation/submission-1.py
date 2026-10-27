class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for elem in tokens:
            if elem.isdigit() or len(elem) == 2:
                if len(elem) == 2:
                    num = -(int(elem[1]))
                    stack.append(num)
                else:
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
                    stack.append(math.trunc(num1/num2))

        if stack:
            return stack.pop()
        return 0
