class Solution:
    def romanToInt(self, s: str) -> int:
        romanStore={
            'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"CM":900,"CD":400,"XL":40,"XC":90,
            "IV":4,"IX":9
        }
        integer=0
        i=0
        while i<len(s):
            if s[i:i+2] in romanStore :
                integer+=romanStore[s[i:i+2]]
                i+=2
                if i >=len(s):
                    i=len(s)
            else:
                integer+=romanStore[s[i]]
                i+=1
        return integer
        