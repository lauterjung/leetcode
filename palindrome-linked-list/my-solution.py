class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        half_string: str = ""
        is_even: bool = False
        is_odd: bool = True
        count = 0
        slow = fast = head
        
        while slow:
            if (fast and fast.next):
                half_string += str(slow.val)
                fast = fast.next
                count += 1

                if fast.next: #fast.next.next
                    fast = fast.next
                    count += 1

                else:
                    half_string = half_string[:-1]
                    is_even = True

            else:
                # print("full: " + str(half_string))
                # print("compared: " + str(half_string[-1]))
                # print("actual: "+ str(slow.val))
                if str(half_string[-1]) != str(slow.val):
                    return False
                half_string = half_string[:-1]

            slow = slow.next
        return True