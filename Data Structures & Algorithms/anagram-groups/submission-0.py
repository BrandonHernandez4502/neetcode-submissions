class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = []
        solution = []
        visited = []

        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            sortedStrs.append(s)

        for j in range(len(sortedStrs)):
            if sortedStrs[j] in visited:
                    continue
            currAna = [strs[j]]
            for k in range(j + 1, len(sortedStrs)):
                if sortedStrs[k] == sortedStrs[j]:
                    currAna.append(strs[k])
                    visited.append(sortedStrs[j])
            solution.append(currAna)

        return solution