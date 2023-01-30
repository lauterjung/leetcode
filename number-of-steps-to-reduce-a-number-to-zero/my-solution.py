class Solution:
    def numberOfSteps(self, number: int) -> int:
        counter = 0

        while number > 0:
            number_is_even: bool = (number % 2) == 0
            if number_is_even:
                number /= 2
            else:
                number -= 1
            counter +=1
        
        return counter