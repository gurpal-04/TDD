def add(numbers: str) -> int:
    if numbers == "":
        return 0

    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
        
        return sum(int(n) for n in numbers.split(delimiter))

    clean = numbers.replace("\n", ",")
    return sum(int(n) for n in clean.split(","))
