class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        half_string: str = ""
        count: int = 0
        slow = fast = head
        
        while slow:
            if (fast and fast.next):
                half_string += str(slow.val)
                fast = fast.next.next
                print("a")
                print(half_string)
            else:
                print("b")
                print(half_string[-1])
                print(slow.val)
                if half_string[-1] != slow.val:
                    return False
                # half_string.pop()
            
            print("c")
            print(slow.val)
            slow = slow.next
        return True