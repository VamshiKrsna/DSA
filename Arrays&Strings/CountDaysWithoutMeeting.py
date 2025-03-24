class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_days = 0
        last_end = 0
        for i,j in meetings:
            if i > last_end + 1:
                free_days += i-last_end-1
            last_end = max(last_end,j)
        if last_end < days:
            free_days += days - last_end
        return free_days
        
