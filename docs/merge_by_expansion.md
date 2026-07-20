# 🔍 Approach 1: Merge by Expansion
Once the intervals are ***sorted by their starting values***, any intervals that overlap will appear next to each other.

Instead of immediately deciding whether to merge the next interval, we treat the current interval as the ***starting point of a merged range***. We then continuously ***look ahead*** and expand the current interval as long as the next interval overlaps.

When no more overlaps are found, the fully expanded interval is added to the answer, and the process repeats from the next unprocessed interval.

### 🚀 Algorithm
1. 📊 Sort all intervals based on their starting values.
2. 📍 Start from the first interval.
3. 🎯 Treat it as the current merged interval.
4. 🔗 Keep checking the following intervals:
    - If they overlap, extend the ending boundary.
    - Otherwise, stop expanding.
5. ✅ Store the completed merged interval.
6. 🚀 Continue from the first interval that wasn't merged.
7. 🔄 Repeat until every interval has been processed.

### 📝 Pseudocode
```
sort intervals

result = empty list
index = 0

while index < total_intervals

    current_start = intervals[index].start
    current_end = intervals[index].end

    next = index + 1

    while next exists AND current_end >= intervals[next].start

        current_end = max(current_end, intervals[next].end)
        next += 1

    add [current_start, current_end] to result

    index = next

return result
```

### ⏱️ Time Complexity
- Sorting the intervals: **`O(n log n)`**
- Traversing and expanding intervals: **`O(n)`**
- **Overall Complexity:** **`O(n log n)`**

### 💾 Space Complexity
- Result list stores merged intervals.
- **Overall Complexity:** **`O(n)`**
---