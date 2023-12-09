def generate_rows(width):
    if width == 0:
        return [[]] 
    elif width == 1:
        return [] 

    rows = []
    if width - 2 >= 0:
        rows.extend([row + [2] for row in generate_rows(width - 2)])

    if width - 3 >= 0:
        rows.extend([row + [3] for row in generate_rows(width - 3)])
    return rows

def generate_prefix_sum(row):
    prefix_sum = set()
    prefix = 0
    for i in range(len(row) - 1):
        prefix += row[i]
        prefix_sum.add(prefix)
    return prefix_sum

def generate_conflict_list(prefix_sums):
    conflict_list = []
    for i in range(len(prefix_sums)):
        conflict_list.append([j for j in range(len(prefix_sums)) if prefix_sums[i].isdisjoint(prefix_sums[j])])
    return conflict_list


def calculate_total_ways(conflict_list, height):
    num_rows = len(conflict_list)
    dp = [1] * num_rows  # Base case: 1 way to build the floor with 1 row

    # Build the solution for each height from 2 to the given height
    for _ in range(1, height):
        new_dp = [0] * num_rows
        for i in range(num_rows):
            for j in conflict_list[i]:
                new_dp[j] += dp[i]
        dp = new_dp

    return sum(dp)  # Sum of all ways for the topmost row

def count_patterns(width, height):
    rows = generate_rows(width)
    prefix_sums = [generate_prefix_sum(row) for row in rows] 
    conflict_list = generate_conflict_list(prefix_sums)
    return calculate_total_ways(conflict_list, height)

print(count_patterns(32, 10))
