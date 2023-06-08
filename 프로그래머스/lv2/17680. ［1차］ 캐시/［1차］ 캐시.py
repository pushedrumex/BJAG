def solution(cacheSize, cities):
    HIT = 1
    MISS = 5
    
    cache = []
    answer = 0
    
    if cacheSize == 0: return len(cities) * MISS

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += HIT
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += MISS
            
    return answer