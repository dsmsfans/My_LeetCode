# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final = []
        def to_int(L):
            if L:
                return L.val + 10 * to_int(L.next)
            else :
                return 0
            
        def to_list(val):
            for i in range(len(str(val))):
                a = val % 10
                final.append(a)
                val = val / 10
            
            return final
        
        return to_list(to_int(l1) + to_int(l2))
            