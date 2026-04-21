#Unit–3 Assignment: Sorting Algorithms

#------------------------------------------------------------------------------------------------------
# Course            : Data Structures
# Assignment Title  : Sorting Algorithms
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
# Submission Date   : 20 April 2026
#____________________________________________________________________________________________________

# ------------------------------------------------------------
#Imports
import time
import random
import sys
sys.setrecursionlimit(20000)


# ------------------------------------------------------------
# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# ------------------------------------------------------------
# Merge Sort
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# ------------------------------------------------------------
# Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ------------------------------------------------------------
# Correctness Test
def test_correctness():
    arr = [5, 2, 9, 1, 5, 6]
    a1 = arr.copy()
    insertion_sort(a1)
    a2 = merge_sort(arr.copy())
    a3 = arr.copy()
    quick_sort(a3, 0, len(a3) - 1)

    print("Correctness Check:")
    print("Original :", arr)
    print("Insertion:", a1)
    print("Merge    :", a2)
    print("Quick    :", a3)
    print("-" * 40)


# ------------------------------------------------------------
# Timing Function
def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()
    if sort_func.__name__ == "quick_sort":
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        result = sort_func(arr_copy)
        if result is not None:
            arr_copy = result

    end = time.time()
    return (end - start) * 1000


# ------------------------------------------------------------
# Dataset Generator
def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}
    for size in sizes:
        random_list = [random.randint(1, 100000) for _ in range(size)]
        sorted_list = sorted(random_list)
        reverse_list = sorted_list[::-1]

        datasets[(size, "random")] = random_list
        datasets[(size, "sorted")] = sorted_list
        datasets[(size, "reverse")] = reverse_list
    return datasets


# ------------------------------------------------------------
# Running Experiments
def run_experiments():
    datasets = generate_datasets()
    results = []
    for (size, dtype), data in datasets.items():
        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data)

        results.append((size, dtype, t1, t2, t3))
    return results


# ------------------------------------------------------------
# Saving Results
def save_results(results):
    with open("output.txt", "w") as f:
        header = f"{'Size':<10}{'Type':<10}{'Insertion':<15}{'Merge':<15}{'Quick':<15}\n"
        print(header)
        f.write(header)
        for r in results:
            line = f"{r[0]:<10}{r[1]:<10}{r[2]:<15.2f}{r[3]:<15.2f}{r[4]:<15.2f}\n"
            print(line)
            f.write(line)


# ------------------------------------------------------------
# Main
if __name__ == "__main__":
    test_correctness()
    print("Running experiments...\n")
    results = run_experiments()
    save_results(results)
    print("\nResults saved to output.txt")