"""
Refer to the following Python method, What does the function return for each of the following inputs?


"""


class solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {")": "(", "}": "{", "]": "["}
        stack_list = []
        for char in s:
            if char in pair_dict:
                if len(stack_list) == 0:
                    return False
                top = stack_list[-1]
                if top != pair_dict[char]:
                    return False
                stack_list.pop()
            else:
                stack_list.append(char)
        return True


"""

"([)]"
False
 
"[(}]"
False
 
"[()]"
True 

"""
