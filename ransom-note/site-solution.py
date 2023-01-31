class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for charr in set(ransomNote):
            if ransomNote.count(charr)>magazine.count(charr):return False
        return True