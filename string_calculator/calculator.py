def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = "\n"
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    
    clean = numbers.replace(delimiter, ",")
    numbers = [int(n) for n in clean.split(",")]
    negative_numbers = [str(n) for n in numbers if n < 0]
    print(negative_numbers, numbers)

    if negative_numbers:
        raise Exception(f"negative numbers not allowed {','.join(negative_numbers)}")

    filtered = [n for n in numbers if n <= 1000]
    return sum(filtered)
