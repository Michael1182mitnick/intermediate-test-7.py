# Given a list of intervals, merge all overlapping intervals into one.

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            merged_intervals[-1] = [last_merged[0],
                                    max(last_merged[1], current[1])]
        else:
            merged_intervals.append(current)

    return merged_intervals


# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print(f"Merged intervals: {result}")
