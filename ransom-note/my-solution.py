class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        if not set(ransom_note).issubset(set(magazine)):
            return False
        
        ransom_note_dict: dict = {i: ransom_note.count(i) for i in set(ransom_note)}
        magazine_dict: dict = {i: magazine.count(i) for i in set(magazine)}
        for key, value in ransom_note_dict.items():
            if value > magazine_dict[key]:
                return False

        return True