1st solution
def reverse_string(s):
    return s[::-1]

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()

2nd solution
def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18:
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
3rd solution
def read_and_write_file(filename):
    try:
        # Issue 1: Reading and writing to the same file without preserving original content
        # Solution 1: Read the content, close the file, and then write to a new file or use a temporary variable.
        with open(filename, 'r') as file:
            content = file.read()

        # Issue 2: Overwriting the original file content before processing
        # Solution 2: Store the modified content in a new variable before writing it back to the file.
        modified_content = content.upper()

        # Write modified content back to the same file
        with open(filename, 'w') as file:
            file.write(modified_content)

        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        # Issue 3: Generic exception handling without specifying the type of exception
        # Solution 3: Handle specific exceptions like FileNotFoundError, PermissionError, etc., for better error reporting.
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()
    4th solution
    def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the subarrays
    left = merge_sort(left)
    right = merge_sort(right)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(f"The sorted array is: {arr}")
