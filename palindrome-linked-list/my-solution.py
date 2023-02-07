class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        half_string: str = ""
        count: int = 1
        slow = fast = head

        while slow:
            if (fast and fast.next):
                half_string += str(slow.val)
                if fast.next.next:
                    count += 2
                else:
                    count += 1
                fast = fast.next.next

            else:
                if count == 1:
                    return True
                if count % 2:
                    slow = slow.next
                    count = 0
                if int(half_string[-1]) != (slow.val):
                    return False
                half_string = half_string[:-1]

            slow = slow.next
        return True