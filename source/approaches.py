from typing import List

class Merge_By_Expansion:
    """
    🔍 Merge by Expansion

    💡 Idea:
        • Sort all intervals by their starting point.
        • Treat each interval as the beginning of a potential merged range.
        • Continuously expand the current interval while the following intervals overlap.
        • Once no more overlaps exist, store the merged interval and repeat.

    ⏱️ Time Complexity: O(n log n)
        • Sorting takes O(n log n).
        • The traversal visits each interval at most once.

    💾 Space Complexity: O(n)
        • Stores the merged intervals in the result list.
    """

    def __init__(self, intervals: List[List[int]]) -> None:
        # 📥 Store and sort the intervals by their starting values
        self.__intervals: List[List[int]] = intervals
        self.__intervals.sort()

        # 📦 Stores the final merged intervals
        self.merged_intervals: List[List[int]] = []

    def merge(self) -> List[List[int]]:
        total_intervals: int = len(self.__intervals)
        interval_index: int = 0

        # 🔍 Process each interval one by one
        while interval_index < total_intervals:
            # 🎯 Start a new merged interval
            current_start: int = self.__intervals[interval_index][0]
            current_end: int = self.__intervals[interval_index][1]

            # ➡️ Look ahead for overlapping intervals
            next_interval_index: int = interval_index + 1

            while (
                next_interval_index < total_intervals and
                current_end >= self.__intervals[next_interval_index][0]
            ):
                # 🔗 Expand the current interval to include the overlap
                current_end = max(
                    current_end,
                    self.__intervals[next_interval_index][1]
                )

                next_interval_index += 1

            # ✅ Save the completely merged interval
            self.merged_intervals.append([current_start, current_end])

            # 🚀 Continue from the first unprocessed interval
            interval_index = next_interval_index

        return self.merged_intervals


class Single_Pass_Merge:
    """
    ⚡ Single-Pass Merge

    💡 Idea:
        • Sort the intervals by their starting point.
        • Keep track of the current merged interval.
        • If the next interval overlaps, extend the current interval.
        • Otherwise, save the completed interval and begin a new one.
        • Finish by adding the final merged interval.

    ⏱️ Time Complexity: O(n log n)
        • Sorting takes O(n log n).
        • The remaining traversal is a single O(n) pass.

    💾 Space Complexity: O(n)
        • Stores the merged intervals in the result list.
    """

    def __init__(self, intervals: List[List[int]]) -> None:
        # 📥 Store and sort the intervals by their starting values
        self.__intervals: List[List[int]] = intervals
        self.__intervals.sort()

        # 📦 Stores the final merged intervals
        self.merged_intervals: List[List[int]] = []

    def merge(self) -> List[List[int]]:
        # 🎯 Initialize the merged interval with the first interval
        current_start: int = self.__intervals[0][0]
        current_end: int = self.__intervals[0][1]

        # 🔍 Traverse the remaining intervals
        for next_start, next_end in self.__intervals[1:]:
            # 🔗 Extend the current interval if an overlap exists
            if current_end >= next_start:
                current_end = max(current_end, next_end)

            else:
                # ✅ Save the completed merged interval
                self.merged_intervals.append([current_start, current_end])

                # 🚀 Begin tracking a new interval
                current_start, current_end = next_start, next_end

        # 📌 Add the final merged interval
        self.merged_intervals.append([current_start, current_end])

        return self.merged_intervals
