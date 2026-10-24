class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        d=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def dateToMonth(date_str:str)->int:
            M=int(date_str[:2])
            D=int(date_str[3:])
            return sum(d[:M-1])+D
        alice_start = dateToMonth(arriveAlice)
        alice_end = dateToMonth(leaveAlice)
        bob_start = dateToMonth(arriveBob)
        bob_end = dateToMonth(leaveBob)
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        return max(0,overlap_end-overlap_start+1)
