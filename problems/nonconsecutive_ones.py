# Given an integer n, return all binary strings of length n that do not contain consecutive ones.

# Input: n
# Output: ['0000', '0001', '0010', '0100', '0101', '1000', '1001', '1010']

def nonconsecutive_ones(n):
    result = []
    def helper(binstr):
        if len(binstr) == n:
            result.append(''.join(binstr))
            return
        binstr.append('0')
        helper(binstr)
        binstr.pop()
        if not binstr or binstr[-1] != '1':
            binstr.append('1')
            helper(binstr)
            binstr.pop()

    helper([])
    return result

print(nonconsecutive_ones(4))
