class Solution:
    def maximumMeetings(self,start,end):

        meetings = [(i, j) for i, j in zip(start, end)]
        
        #the meeting that is ending the quickest will come first 
        meetings.sort(key = lambda x: (x[1], x[0])) 
        # print(meetings)
        attend = 0
        free = -1
        for meet in range(len(meetings)):
            if meetings[meet][0] > free:
                attend +=1
                free = meetings[meet][1]
            
        return attend
        