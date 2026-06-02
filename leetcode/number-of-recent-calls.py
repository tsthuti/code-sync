from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.reqs = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.reqs.append(t) # add right 

        while self.reqs[0] < t - 3000:
            self.reqs.popleft()

        return len(self.reqs)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(1)