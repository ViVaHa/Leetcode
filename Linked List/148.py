# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self,list1,list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head=None
        
        if list1.val<list2.val:
            head=list1
            list1=list1.next
        else:
            head=list2
            list2=list2.next
        cur=head
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                cur.next=list1
                cur=cur.next
                list1=list1.next
            else:
                cur.next=list2
                cur=cur.next
                list2=list2.next
        if list1:
            while list1 is not None:
                cur.next=list1
                list1=list1.next
                cur=cur.next
        if list2:
            while list2 is not None:
                cur.next=list2
                list2=list2.next
                cur=cur.next
        return head
                
            
    def mergeSort(self,head):
        if head is None:
            return None
        if head.next is None:
            return head
        slow=head
        fast=head
        while fast.next is not None:
            fast=fast.next.next
            prev=slow
            slow=slow.next
            if fast is None:
                break
        middle=slow
        prev.next=None
        leftHalf=self.mergeSort(head)
        rightHalf=self.mergeSort(middle)
        merged=None
        if leftHalf and rightHalf:
            merged=self.merge(leftHalf,rightHalf)
        return merged
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        newHead=self.mergeSort(head)
        return newHead
