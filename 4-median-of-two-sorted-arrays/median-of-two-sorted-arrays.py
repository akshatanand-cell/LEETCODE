class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            p1 = (left + right) // 2
            p2 = (m + n + 1) // 2 - p1

            maxLeft1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            minRight1 = float('inf') if p1 == m else nums1[p1]

            maxLeft2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            minRight2 = float('inf') if p2 == n else nums2[p2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) +
                            min(minRight1, minRight2)) / 2.0

                return float(max(maxLeft1, maxLeft2))

            elif maxLeft1 > minRight2:
                right = p1 - 1
            else:
                left = p1 + 1