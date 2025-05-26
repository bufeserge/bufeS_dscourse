# L02T04 : Python Packages for Data Science


# INSTRUCTIONS : Create a file named numpy_task.py
#               Answer the following questions using comments and code:
#                   Q1: why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)) create a 2D array?
#                       - fix the syntax and show the correct way to create a 3x3 identity matrix with float values
#                Q2: what is the difference between:
#                       a = np.array([0, 0, 0]) and a = np.array([[0, 0, 0]])?
#                       - explain how the dimensions differ and how they behave differently in operations

#                Q3: given: arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
#                       - use indexing/slicing to obtain the following:
#                            a. the value 20.0
#                            b. the row [9. 10. 11. 12.]
#                            c. the last 2D matrix: [[33. 34. 35. 36.], [37. 38. 39. 40.], [41. 42. 43. 44.], [45. 46. 47. 48.]]
#                            d. selected pairs: [[5. 6.], [21. 22.], [37. 38.]]
#                            e. mirrored row-wise block: [[36. 35.], [40. 39.], [44. 43.], [48. 47.]]
#                            f. reversed rows and columns block: [[13. 9. 5. 1.], [29. 25. 21. 17.], [45. 41. 37. 33.]]
#                            g. edge values: [[1. 4.], [45. 48.]]
#                            h. center block: [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]

# i will write code in a script called numpy_task.py and add comments to explain my answers.
# the task will involve understanding how numpy handles dimensions, shapes, and memory layout.
# i plan to experiment with the numpy methods interactively before writing the final answers in the script.
# i’ll use examples from the cheat sheet and documentation to guide my slicing operations.
# once completed, i will ensure the code is clean, well-commented, and correctly demonstrates each concept.


import numpy as np

# Q1: Why doesn’t this create a 2D array?
# np.array((1, 0, 0), (0, 1, 0), (0, 0, 1), dtype=float)  # Incorrect syntax
# Explanation: The function call is missing an extra pair of parentheses to group the rows.
# Correct version:
identity_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
print("Q1 Result:\n", identity_matrix)

# Q2: What is the difference between:
a1 = np.array([0, 0, 0])  # 1D array with shape (3,)
a2 = np.array([[0, 0, 0]])  # 2D array with shape (1, 3)
print("\nQ2 Result:")
print("a1 shape:", a1.shape)  # Outputs: (3,)
print("a2 shape:", a2.shape)  # Outputs: (1, 3)

# Q3: Create the 3x4x4 array
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print("\nQ3 Full Array:\n", arr)

# a. Get the value 20.0
value_20 = arr[1, 1, 3]
print("\na. Value 20.0:", value_20)

# b. Get the row [9. 10. 11. 12.]
row_9_to_12 = arr[0, 2, :]
print("\nb. Row [9. 10. 11. 12.]:", row_9_to_12)

# c. Get the full matrix: [[33. 34. 35. 36.] ... [45. 46. 47. 48.]]
last_matrix = arr[2, :, :]
print("\nc. Last matrix:\n", last_matrix)

# d. Get selected pairs: [[5. 6.], [21. 22.], [37. 38.]]
selected_pairs = arr[:, 1, 0:2]
print("\nd. Selected pairs:\n", selected_pairs)

# e. Get mirrored row-wise block: [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
mirrored_block = arr[2, :, -1:-3:-1]
print("\ne. Mirrored block:\n", mirrored_block)

# f. Reversed rows and columns block: [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
rev_block = arr[:, :, ::-4]
rev_block_result = np.array([arr[0, 3, ::-1], arr[1, 3, ::-1], arr[2, 3, ::-1]])
print("\nf. Reversed block:\n", rev_block_result)

# g. Edge values: [[1. 4.] [45. 48.]]
edge_values = np.array([[arr[0, 0, 0], arr[0, 0, 3]], [arr[2, 3, 0], arr[2, 3, 3]]])
print("\ng. Edge values:\n", edge_values)

# h. Center block: [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
center_block = arr[1, :, :]
print("\nh. Center block:\n", center_block)
