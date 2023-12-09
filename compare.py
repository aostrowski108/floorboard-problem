import floor
import time

def runtime_func(width, height):
    return height * width**2 * (1.32**width) ** 2

def percent_change(old_value, new_value):
    if old_value == 0:
        return "Undefined"
    change = (new_value - old_value) / old_value
    return change * 100

def test_runtimes(runs):
    #testing constant heights
    average_runtime = 0
    for _ in range(runs):
        start = time.time()
        floor.count_patterns(35, 32)
        end = time.time()
        average_runtime += (end - start)
    average_runtime = average_runtime / runs

    increased_width_rt = 0
    for _ in range(runs):
        start = time.time()
        floor.count_patterns(36, 32)
        end = time.time()
        increased_width_rt += (end - start)
    increased_width_rt = increased_width_rt / runs

    increased_height_rt = 0
    for _ in range(runs):
        start = time.time()
        floor.count_patterns(35, 33)
        end = time.time()
        increased_height_rt += (end - start)
    increased_height_rt = increased_height_rt / runs

    emp_width_ratio = increased_width_rt / average_runtime
    emp_height_ratio = increased_height_rt / average_runtime
    actual_width_ratio = runtime_func(36, 32) / runtime_func(35, 32)
    actual_height_ratio = runtime_func(35, 33) / runtime_func(35, 32)
    print("ratio % change with small change in width", percent_change(actual_width_ratio, emp_width_ratio))
    print("ratio % change with small change in height", percent_change(actual_height_ratio, emp_height_ratio))

    
test_runtimes(10)









