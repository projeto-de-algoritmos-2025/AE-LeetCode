from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        
        dp = [0] * n
        dp[0] = jobs[0][2]  

    
        end_times = [job[1] for job in jobs]

        for i in range(1, n):
            incl_prof = jobs[i][2]
    
            index = bisect_right(end_times, jobs[i][0]) - 1
            if index != -1:
                incl_prof += dp[index]
            dp[i] = max(dp[i - 1], incl_prof)

        return dp[-1]
