def add(numbers: str) -> int:
    if numbers == "":
        return 0
        
    delimiter = "\n"
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    
    clean = numbers.replace(delimiter, ",")
    return sum(int(n) for n in clean.split(","))
