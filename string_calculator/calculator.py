def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = "\n"
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    
    clean = numbers.replace(delimiter, ",")
    negative_numbers = [n for n in clean.split(",") if int(n) < 0]
    
    if negative_numbers:
        raise Exception(f"negative numbers not allowed {','.join(negative_numbers)}")
    return sum(int(n) for n in clean.split(","))
