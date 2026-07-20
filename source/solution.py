from typing import List
from .approaches import Merge_By_Expansion, Single_Pass_Merge

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 🎯 Choose one of the available approaches
        # approach_01: Merge_By_Expansion = Merge_By_Expansion(intervals=intervals)
        approach_02: Single_Pass_Merge = Single_Pass_Merge(intervals=intervals)

        # ⚙️ Execute the selected approach
        # ans_01: List[List[int]] = approach_01.merge()
        ans_02: List[List[int]] = approach_02.merge()

        # 📦 Return the final merged intervals
        return ans_02