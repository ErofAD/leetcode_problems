from typing import List, Optional


#https://leetcode.com/problemset/all/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 1. Two Sum
    @staticmethod
    def two_sum(number_list: List[int], target: int) -> List[int]:
        for j in range(len(number_list)):
            for i in range(len(number_list)):
                if j != i:
                    if number_list[i] + number_list[j] == target:
                        return [j, i]

    # 2. Add Two Numbers
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ''
        l2_str = ''
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next

        l1_int = int(l1_str[::-1])
        l2_int = int(l2_str[::-1])
        sum_str = str(l1_int + l2_int)[::-1]
        answer = ListNode()
        answer_node = answer
        len_str = 0
        for i in sum_str:
            len_str = len_str + 1
            answer_node.val = i
            if len_str < len(sum_str):
                answer_node.next = ListNode()
                answer_node = answer_node.next

        return answer

    # 5. Longest Palindromic Substring
    #TODO: Time Limit Exceeded Error. Need to fix.
    def find_polindromic(original_line: str) -> str:
        if original_line == original_line[::-1]:
            return original_line

        polinom = ''

        for i in range(len(original_line)):
            for j in range(0, len(original_line) - i):
                tmp_polinom = original_line[i:len(original_line) - j]
                if len(polinom) < len(tmp_polinom):
                    if tmp_polinom == tmp_polinom[::-1]:
                        polinom = tmp_polinom

        return polinom

    # 9. Palindrome Number
    @staticmethod
    def is_palindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]

    # 13. Roman to Integer
    @staticmethod
    def roman_to_int(s: str) -> int:
        symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        values = []
        position = len(s) - 1
        while position > 0:
            if symbol_value[s[position]] <= symbol_value[s[position - 1]]:
                values.append(symbol_value[s[position]])
            else:
                values.append(symbol_value[s[position]] - symbol_value[s[position - 1]])
                position -= 1
                if position - 1 < 0:
                    return sum(values)
            position -= 1
        values.append(symbol_value[s[0]])
        return sum(values)

    # 14. Longest Common Prefix
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        strs_sort_len = sorted(strs, key=lambda x: len(x))
        prefix = strs_sort_len[0]
        search = True
        while search:
            new_prefix = prefix
            for string in strs_sort_len:
                if prefix in string[0:len(prefix)]:
                    continue
                else:
                    if len(prefix) > 1:
                        new_prefix = prefix[0:-1]
                        break
                    else:
                        new_prefix = ''
                        search = False
            if new_prefix == prefix:
                search = False
            else:
                prefix = new_prefix

        return prefix




if __name__ == '__main__':
    print(Solution.longest_common_prefix(["reflower","flow","flight"]))




