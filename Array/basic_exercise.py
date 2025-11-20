# =====================
# Copying an Array
# =====================
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
copy_array = []

# Copy each element from the original array
for a in array:
    copy_array.append(a)

print(f"Original Array: {array}")
print(f"Copied Array:   {copy_array}")
print()

# =====================
# Swapping Elements in an Array
# =====================

# Method 1: Swap neighboring pairs
n = len(array)

for i in range(0, n, 2):
    for j in range(i+1, i+2):
        if j < n:
            array[i], array[j] = array[j], array[i]

print("Swapping array - Method 1:")
print(*array)

# Method 2: Swap back to original positions
for i in range(0, n, 2):
    if i+1 < n:
        array[i], array[i+1] = array[i+1], array[i]

print("Swapping array - Method 2 (original):")
print(*array)
print()

# ==========================
# Shifting Elements: Left and Right
# ==========================

# Left Shift
# Move each element one position to the left.
# The last position is filled with 0.
left_shift = array[:-1]  # copy all elements except the last
for i in range(1, len(left_shift)):
    left_shift[i-1] = left_shift[i]

left_shift[-1] = 0  # fill the last spot with 0
print("Array after left shift:")
print(left_shift)

# Right Shift
# Move each element one position to the right.
# The first position is filled with 0.
right_shift = array[:-1]  # copy all elements except the last
for i in range(len(right_shift)-2, -1, -1):
    right_shift[i+1] = right_shift[i]

right_shift[0] = 0  # fill the first spot with 0
print("Array after right shift:")
print(right_shift)
