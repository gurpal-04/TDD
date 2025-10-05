def add(numbers: str) -> int:
    if numbers == "":
        return 0

    if "," in numbers:
        n,m = numbers.split(",")
        return int(n) + int(m)
    return int(numbers)
