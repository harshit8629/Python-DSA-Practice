def convertToTitle(columnNumber: int) -> str:
    result = []
    while columnNumber > 0:
        columnNumber -= 1  # Adjust for 0-indexed arithmetic (A=0, B=1, ..., Z=25)
        remainder = columnNumber % 26
        result.append(chr(ord('A') + remainder))
        columnNumber //= 26
    return "".join(reversed(result))

# Example Usage:
print(f"Input: 1, Output: {convertToTitle(1)}")
print(f"Input: 28, Output: {convertToTitle(28)}")
print(f"Input: 701, Output: {convertToTitle(701)}")