# p7 : Alphabet Rangoli

# link : https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# code :

def print_rangoli(size):
    # your code goes here
    lines = []
    width = 4 * size - 3
    
    # Generate the top half and the middle line
    for i in range(size):
        # Generate the letters for the current row
        letters = [chr(97 + size - 1 - j) for j in range(i + 1)]
        letters.extend([chr(97 + size - 1 - j) for j in range(i - 1, -1, -1)])
        
        # Combine, format with hyphens, and center
        row_string = "-".join(letters)
        lines.append(row_string.center(width, '-'))
        
    # Print the top half, middle, and the mirrored bottom half
    print('\n'.join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
