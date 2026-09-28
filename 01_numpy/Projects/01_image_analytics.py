import numpy as np

# Base Data: 8x8 Grayscale Image Matrix (0-255 brightness)
image = np.array([
    [ 10,  15,  20,  25,  30,  35,  40,  45],
    [ 50,  55, 200, 210, 220,  60,  65,  70],
    [ 75,  80, 230, 240, 250,  85,  90,  95],
    [100, 105, 215, 225, 235, 110, 115, 120],
    [125, 130, 135, 140, 145, 150, 155, 160],
    [165, 170, 175, 180, 185, 190, 195, 200],
    [205, 210, 215, 220, 225, 230, 235, 240],
    [245, 250, 255,   0,   5,  10,  15,  20]
])
print("TASK 1: Crop High-Brightness Region (Rows 1-3, Cols 2-4) ")
# Rows 1 to 3 (stop at index 4) and Columns 2 to 4 (stop at index 5)
bright_region = image[1:4, 2:5]
print(bright_region)
print("\nTASK 2: Invert Image (Vectorized Math) ")
# C-speed vectorized subtraction across the entire array
inverted_image = 255 - image
print(inverted_image)
print("\n TASK 3: Threshold Masking (Boolean Masking) ")
# Always copy to keep original array intact
thresholded_image = image.copy()
# Create boolean masks to apply conditions
overexposed_mask = thresholded_image >= 200
underexposed_mask = thresholded_image < 200
thresholded_image[overexposed_mask] = 255
thresholded_image[underexposed_mask] = 0
print(thresholded_image)

print("\nTASK 4: Analytics (Axis Aggregation & Peak Location)")
# Calculate average brightness per column (axis=0 moves vertically down rows)
col_avg = np.mean(image, axis=0)
print("Column Averages:", col_avg)
# Locate maximum value and its row/col coordinates
max_val = np.max(image)
max_pos = np.where(image == max_val)
# Convert coordinates into a clean tuple format (row, col)
row_idx, col_idx = max_pos[0][0], max_pos[1][0]
print(f"Max Value: {max_val} at position: (Row {row_idx}, Col {col_idx})")

print("\nTASK 5: Normalize Image (Broadcasting)")
# Broadcasting: float division across every integer element
normalized_image = image / 255.0
print(normalized_image)