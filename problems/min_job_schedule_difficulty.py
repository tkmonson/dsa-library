'''
Minimum Difficulty of a Job Schedule

Given a list of job difficulties and d days, find the minimum difficulty of a
job schedule. To work on the ith job, you must first finish all jobs j, where
0 <= j < i. You must finish at least one job per day. The difficulty of a job
schedule is the sum of the difficulties of all d days. The difficulty of a day
is the maximum difficulty of a job done on that day. If no valid schedule
exists, return -1.

-------------------------------------------------------------------------------

Base cases:
    1. Not enough jobs left for remaining days - FAIL
    2. No days left (or past final day) - FAIL
    3. No jobs left and no days left (or doing final job on final day) - PASS

Recursive cases:
    1. Do the next job today (difficulty may increase, day remains the same)
    2. Do the next job tomorrow (difficulty is that of next job, increment day)

Time complexity: T(j) = T(j - 1) + c, where T(1) = c
Auxiliary space complexity: S(j) = S(j - 1) + c, where S(1) = c
'''

from functools import cache

def min_schedule_difficulty(job_difficulty: list[int], num_days: int) -> int:
    @cache
    def helper(current_diff, current_day, job_index):
        jobs_left = len(job_difficulty) - job_index
        days_left = num_days - current_day
        if jobs_left < days_left or days_left == -1:
            return float('inf')
        if not jobs_left and not days_left:
            return current_diff
        next_diff = job_difficulty[job_index]
        min_diff_today = helper(
            max(current_diff, next_diff),
            current_day,
            job_index + 1
        )
        min_diff_tomorrow = current_diff + helper(
            next_diff,
            current_day + 1,
            job_index + 1
        )
        return min(min_diff_today, min_diff_tomorrow)
    min_diff = helper(job_difficulty[0], 1, 1)
    return -1 if min_diff == float('inf') else min_diff

if __name__ == '__main__':
    print(min_schedule_difficulty([6,5,4,3,2,1], 2))

'''
Also, study this 100% time, 100% space solution:

The idea is to to finish up till ith job in d - k days and finish rest of the jobs in k days.
f(i,k) = min(f(j,k) + max_job_difficulty_for_ith_day) for i <= j <= n - k + 1
    where max_job_difficulty_for_ith_day is nothing but max(jobDifficulty[i:j])

Base case: When we have 1 day left, we have to finish the rest of the unfinished jobs
    (value for that day is max(jobDifficulty[i:]))

def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    if d > len(jobDifficulty): return -1
    arr = jobDifficulty
     
    @lru_cache(None)
    def helper(st, k):           
		# only one day left so we have to finish rest of the unfinished jobs 
        if k == 1: 
            return max(arr[st:]) 
         
		# cur_max is max from ith to jth index, which is value on kth day
        cur_max, ret = 0, float('inf')
        for i in range(st,len(arr)-k+1):
            cur_max = max(cur_max, arr[i])
            ret = min(ret, cur_max + helper(i+1, k - 1))                
        return ret
     
    return helper(0, d)
'''

