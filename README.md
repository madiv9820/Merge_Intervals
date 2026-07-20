# [🧩 Interval Fusion: Merge the Overlapping Time Blocks ⏳✨](https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150)
Imagine you are managing a busy calendar 📅, where every event is represented by a time range **`[startᵢ, endᵢ]`**. Some events may overlap with each other, causing duplicate bookings or connected time slots 🔗.

Your task is to ***combine all overlapping intervals 🤝*** and create a simplified schedule 📝 containing only ***non-overlapping intervals*** that together cover every time range from the original list 🌍.

The final schedule should be clean, organized, and represent the complete coverage of all given intervals 🚀.

### 📌 Examples
- #### 🌟 Example 1: Combining Overlapping Events
    ```
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    ```
    **Explanation:** <br>
    The intervals **`[1,3]`** and **`[2,6]`** overlap because they share common time points ⏰. <br>
    By combining these connected ranges, they form a larger interval **`[1,6]`**.

    The remaining intervals **`[8,10]`** and **`[15,18]`** do not overlap, so they remain unchanged ✅.

- #### 🌟 Example 2: Touching Boundaries Count as Overlapping
    ```
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    ```
    **Explanation:** <br>
    The intervals **`[1,4]`** and **`[4,5]`** meet at the boundary point **`4`** 🔗.

    Since the ending point of the first interval connects with the starting point of the second interval, they are considered overlapping and merge into one continuous interval **`[1,5]`** 📌.

- #### 🌟 Example 3: Merging Intervals in Any Order
    ```
    Input: [[4,7],[1,4]]
    Output: [[1,7]]
    ```
    **Explanation:** <br>
    Although the intervals appear in reverse order 🔄, they still represent connected ranges.

    The intervals **`[1,4]`** and **`[4,7]`** touch at point **`4`**, allowing them to be merged into a single continuous interval **`[1,7]`** ✨.

### 📏 Constraints
- 📌 **`1 <= intervals.length <= 10⁴`**, The number of intervals can be large, so the solution should handle many ranges efficiently ⚡.
- 📌 **`intervals[i].length == 2`**, Each interval contains exactly two values:
    - 🟢 **`startᵢ`** → beginning of the range
    - 🔴 **`endᵢ`** → ending of the range
- 📌 **`0 <= startᵢ <= endᵢ <= 10⁴`**, Interval boundaries are valid and stay within the given range 📊.

### 🎯 Goal 
*Transform a messy collection of overlapping ranges into a clean, organized set of intervals that represents the complete coverage without duplication. 🧩✨*

---