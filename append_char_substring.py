class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Initialize pointers for s and t
        i, j = 0, 0
        m, n = len(s), len(t)
        
        # Traverse both strings
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1  # Match found, move pointer on t
            i += 1  # Always move pointer on s
        
        # Characters of t not matched
        return n - j

# Example usage
solution = Solution()
s = "coaching"
t = "coding"
print(solution.appendCharacters(s, t))  # Output: 4
