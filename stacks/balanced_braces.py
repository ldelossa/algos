def isBalanced(s):
    stack = []

    for char in s:
        # append opening symbols on stack
        if char in "{[(":
            stack.append(char)
            continue

        if stack == []:
            return "NO"

        if char == "}":
            if stack.pop() != "{":
                return "NO"
        if char == "]":
            if stack.pop() != "[":
                return "NO"
        if char == ")":
            if stack.pop() != "(":
                return "NO"

    return "YES"

if __name__ == "__main__":

