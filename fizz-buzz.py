class Solution(object):
    def fizzBuzz(self, n):
        answer = []

        for i in range(1, n+1):
            result = ""

            if (i % 3) != 0 and (i % 5) != 0:
                result = str(i)
                answer.append(result)
                continue
            if (i % 3) == 0:
                result = result + "Fizz"
            if (i % 5) == 0:
                result = result + "Buzz"
            
            answer.append(result)
            
        return answer