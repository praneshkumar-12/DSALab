from dynamicarray import DynamicArray
from timeit import default_timer

if __name__ == "__main__":
    d1 = DynamicArray(30000)
    elts = [1, 5, 10, 100, 500, 1000, 5000, 10_000, 50_000, 1_00_000]
    for elt in elts:
        number_of_elements_to_append = elt
        start = default_timer()
        for _ in range(number_of_elements_to_append):
            d1.append(None)
        stop = default_timer()
        print(f"Size: {number_of_elements_to_append}; Time taken: {(stop - start) / number_of_elements_to_append}"
              f"Original time: {stop-start}")
