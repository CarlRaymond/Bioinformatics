'''
Created on Jan 1, 2013

@author: Carl Raymond
'''

class PriorityQueue:
    """Priority queue optimized for PERM solution states. A list of dictionaries where each dictionary
    holds solution states of the same score. The dictionary key is the permutation, and the value
    is the reversal list.
    """
    
    def __init__(self, n):
        self.queue = [{} for i in xrange(n)]
        self.smallestScore = n
        self.n = n
        self.count = 0
    
    
    def insert(self, state):
        score, revlist, perm = state
        if score < 0 or score >= self.n:
            raise ValueError('Score out of range: {0}'.format(score))
        
        self.queue[score][perm] = revlist 
        self.count += 1
        self.smallestScore = min(self.smallestScore, score)
    
    
    def insertUnlessPresent(self, state):
        score, revlist, perm = state
        if score < 0 or score >= self.n:
            raise ValueError('Score out of range: {0}'.format(score))

        # Look for the perm
        for i in xrange(self.smallestScore, self.n):
            if perm in self.queue[i]:
                if i <= score:
                    # perm already present with a better (or same) score.
                    return
                else:
                    # perm present with a worse score. Delete that one.
                    del(self.queue[i][perm])
                    self.count -= 1
                    
            self.queue[score][perm] = revlist
            self.count += 1

        self.smallestScore = min(self.smallestScore, score)
        return
        
    def pop(self):
        for i in xrange(self.smallestScore, self.n):
            if (len(self.queue[i]) > 0): break
            self.smallestScore = i
        else:
            return None
        
        key, value = self.queue[i].popitem()
        self.count -= 1
        return (i, value, key)
    
    def __len__(self):
        return self.count
    
if __name__ == '__main__':
    q = PriorityQueue(5)
    print "Len: ", len(q)
    q.insert((3, [(1,2)], (5, 3, 4, 2, 1)))
    print "Len: ", len(q)
    q.insertUnlessPresent((3, [], (5, 3, 4, 2, 1)))
    print "Len: ", len(q)
    q.insert((3, [(3,4)], (1, 2, 3, 5, 4)))
    print "Len: ", len(q)
    q.insert((1, [], (5,4,3,2,1)))
    print "Len: ", len(q)
    print "Pop: ", q.pop()
    print "Len: ", len(q)
    print "Pop: ", q.pop()
    print "Len: ", len(q)
    print "Pop: ", q.pop()
    print "Len: ", len(q)
    