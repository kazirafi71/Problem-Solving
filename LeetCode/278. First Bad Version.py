
class Solution:
    def firstBadVersion(self, n: int,start=0) -> int:
        if n==start :
            return n
        mid=(n+start)//2
        if isBadVersion(mid):
            return self.firstBadVersion(mid,start)
        else:
            return self.firstBadVersion(n,mid+1)