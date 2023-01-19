#Minumum Waiting Time
#Time Complexity: O(nlogn) || Space Complexity: O(1)
def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        leftQueries = len(queries) - (idx + 1)
        totalWaitingTime += duration * leftQueries
    return totalWaitingTime