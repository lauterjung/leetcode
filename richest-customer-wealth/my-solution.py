class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        number_of_rows = len(accounts)

        result = -1
        for i in range(number_of_rows):
            current = sum(accounts[i])
            if current > result:
                result = current

        return result