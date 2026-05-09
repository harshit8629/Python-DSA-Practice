class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for event in events:
            # Stop if counter becomes 10
            if counter == 10:
                break

            if event == "W":
                counter += 1

            elif event == "WD" or event == "NB":
                score += 1

            else:
                score += int(event)

        return [score, counter]
solution = Solution()
print(solution.scoreValidator(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "WD", "NB"]))