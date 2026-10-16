class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count how many copies of each character are required.
        need = Counter(t)
        required = len(need)
        window = {}
        formed = 0
        left = 0

        # Store the best window as its length and boundaries.
        best_length = float("inf")
        best_left = 0
        best_right = 0

        # Expand the window using the right pointer.
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink while every required character is present.
            while formed == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right + 1

                removed = s[left]
                window[removed] -= 1

                if removed in need and window[removed] < need[removed]:
                    formed -= 1

                left += 1

        return s[best_left:best_right]
        