def print_numbers(num):
    print(num)
    num *= 5
    
    if num <= 130:
        print_numbers(num)

if __name__ == "__main__":
        print_numbers(5)