class Solution:
    def romanToInt(self, roman_string: str) -> int:
        roman_dict: dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        string_length = len(roman_string)
        result: int = 0
        
        for i, char in enumerate(roman_string):
            is_end_of_string: bool = i == string_length-1
            current_value: int = roman_dict[char]

            if is_end_of_string:
                next_value: int = 0 
            else:
                next_value = roman_dict[roman_string[i+1]]
            
            if current_value >= next_value:
                result += current_value 
            else:
                result -= current_value
            
        return result

solution = Solution()
roman_string = "MCMXCIV"
solution.romanToInt(roman_string)
