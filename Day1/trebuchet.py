file = 'Day1\input.txt'

try:
    with open(file, 'r') as f:
        lines = f.readlines()

        total = 0

        for line in lines:
            digits = [char for char in line if char.isdigit()]

            if digits:
                sum = int(digits[0] + digits[-1])
                total += sum
        print("total sum is ",total)
except FileNotFoundError:
    print('File not found!')
except Exception as e:
    print(f"an error occured:{e}")


