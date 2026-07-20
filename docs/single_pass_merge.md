# ⚡ Approach 2: Single-Pass Merge
### 💡 Intuition
After sorting the intervals, overlapping intervals always appear next to one another.

Instead of repeatedly looking ahead, we maintain a ***single active merged interval***.

For every new interval:
- 🔗 If it overlaps with the active interval, simply extend its ending boundary.
- 📦 Otherwise, the active interval is complete, so store it and begin tracking the new interval.

This greedy strategy processes every interval exactly once after sorting.

### 🚀 Algorithm
1. 📊 Sort intervals by their starting values.
2. 🎯 Initialize the first interval as the active merged interval.
3. 🔍 Traverse the remaining intervals one by one.
4. 🔗 If the current interval overlaps:
    - Extend the active interval.
5. 📦 Otherwise:
    - Store the active interval.
    - Start a new active interval.
6. 📌 Add the final active interval to the answer.
7. ✅ Return all merged intervals.

### 📝 Pseudocode
```
sort intervals

result = empty list

current_start = intervals[0].start
current_end = intervals[0].end

for every remaining interval

    if current_end >= interval.start

        current_end = max(current_end, interval.end)

    else

        add [current_start, current_end] to result

        current_start = interval.start
        current_end = interval.end

add [current_start, current_end] to result

return result
```

### ⏱️ Time Complexity
- Sorting the intervals: **`O(n log n)`**
- Single traversal: **`O(n)`**
- **Overall Complexity:** **`O(n log n)`**

### 💾 Space Complexity
- Result list stores merged intervals.
- **Overall Complexity:** **`O(n)`**
---