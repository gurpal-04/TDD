def add(numbers: str) -> int:
    if numbers == "":
        return 0
    clean = numbers.replace("\n", ",")
    return sum(int(n) for n in clean.split(","))
