class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes*6
        h = (hour%12)*30 + (minutes/60)*30
        return min(abs(h-m), abs((360-max(m,h)) + min(m,h)))