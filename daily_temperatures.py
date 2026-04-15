#Intel - Return list of days until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stak = []
    
    for i in range(0, len(temperatures)):
        
        while len(stak) != 0 and temperatures[i] > temperatures[stak[-1]]:
            answer[stak[-1]] = i - stak[-1]
            stak.pop(-1)
        
        
        stak.append(i)
    
    
    return answer