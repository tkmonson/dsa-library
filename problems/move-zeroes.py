'''
Move Zeroes (#283)

Given an integer array nums, move all 0s to the end of it while maintaining the
relative order of the nonzero elements. Do this in-place, without making a
copy of the array.
'''


def move_zeroes(nums: list[int]) -> None:
    count = nums.count(0)
    nums[:] = [n for n in nums if n != 0]
    nums += count * [0]


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12, 0, 0, 0, 7, 8]
    move_zeroes(nums)
    print(nums)


'''
I made this problem a lot harder than it needed to be because I thought that
in-place meant that I couldn't use a second array at all. Given this
constraint, I knew that removing zeros from the middle of the array would be
inefficient because it would require shifting all of the following elements
forward by one index, so I settled on a two-pointer swap solution where a zero
pointer finds the leftmost zero and a nonzero pointer finds the first nonzero
element to the right of that.

Because all of the zeroes need to be at the end, it's much easier to replace all
elements of the array with only the nonzero elements and then append as many
zeroes as needed.
'''


def move_zeroes_slow(nums: list[int]) -> None:
    n = len(nums)
    zi = -1
    for i in range(n):
        if nums[i] == 0:
            zi = i
            break

    if zi == -1 or zi == n - 1:
        return

    nzi = -1
    for i in range(zi + 1, n):
        if nums[i] != 0:
            nzi = i
            break

    if nzi == -1:
        return

    while nzi < n:
        nums[nzi], nums[zi] = nums[zi], nums[nzi]
        while nzi < n and nums[nzi] == 0:
            nzi += 1
        while zi < nzi and nums[zi] != 0:
            zi += 1

