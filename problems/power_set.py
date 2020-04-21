# Ex: {1,2,3}

#                {}
#             /      \
# 1:        {}          {1}
#          /   \         /   \
# 2:    {}      {2}     {1}    {1,2}
#      /  \     / \      / \       /   \
# 3: {}   {3} {2} {2,3} {1} {1,3} {1,2} {1,2,3}
 
def power_set(s):
    ps = []
    def helper(sub, i):
        if i == len(s):
            ps.append(sub)
            return
        helper(sub.copy(), i+1)
        sub.append(s[i])
        helper(sub.copy(), i+1)
    
    helper([], 0)
    return ps

print(power_set([1,2,3]))

# Time: O(n*2^n)
# Space: O(n*2^n)
