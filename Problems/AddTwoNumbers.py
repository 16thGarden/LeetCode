# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        currNode = self
        output = []
        while(currNode is not None):
            output.append(currNode.val)
            currNode = currNode.next
        print(output)

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = l1.val + l2.val + carry
        carry = sum // 10
        sum %= 10
        
        l3 = ListNode(sum)

        currl1Node = l1.next
        currl2Node = l2.next
        currl3Node = l3

        while(currl1Node is not None and currl2Node is not None):
            sum = currl1Node.val + currl2Node.val + carry
            carry = sum // 10
            sum %= 10

            currl3Node.next = ListNode(sum)
            currl1Node = currl1Node.next
            currl2Node = currl2Node.next
            currl3Node = currl3Node.next
        
        remaining = None
        if (currl1Node is None):
            remaining = currl2Node
        elif (currl2Node is None):
            remaining = currl1Node

        while (remaining is not None):
            sum = remaining.val + carry
            carry = sum // 10
            sum %= 10

            currl3Node.next = ListNode(sum)
            currl3Node = currl3Node.next
            remaining = remaining.next

        if (carry > 0):
            currl3Node.next = ListNode(carry)

        return l3