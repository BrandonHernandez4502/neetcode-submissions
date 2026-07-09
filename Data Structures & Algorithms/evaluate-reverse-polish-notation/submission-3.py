class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        for token in tokens:
            if token in operations:
                b = numbers.pop()
                a = numbers.pop()
                res = operations[token](a,b)
                numbers.append(res)
            else:
                numbers.append(int(token))
        return numbers.pop()