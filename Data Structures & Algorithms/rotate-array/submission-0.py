from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        q=deque(nums)
        for _ in range(k):
            q.appendleft(q.pop())
        nums[:]=list(q)
        