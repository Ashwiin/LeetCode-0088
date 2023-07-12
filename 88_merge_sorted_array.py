class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merges two sorted arrays in-place.

        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None (Modifies nums1 in-place)
        """
        pointer1 = m - 1  # Pointer for nums1
        pointer2 = n - 1  # Pointer for nums2
        current = m + n - 1  # Pointer for merged array

        # Merge elements from both arrays in descending order
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[current] = nums1[pointer1]  # Place larger element from nums1
                pointer1 -= 1
            else:
                nums1[current] = nums2[pointer2]  # Place larger element from nums2
                pointer2 -= 1
            current -= 1

        # Copy any remaining elements from nums2 to nums1
        while pointer2 >= 0:
            nums1[current] = nums2[pointer2]
            pointer2 -= 1
            current -= 1
