# 캐시

def solution(cachesize, cities):
    cache = []
    result = 0
    if cachesize == 0:
        return len(cities) * 5

    for i in range(len(cities)):
        cities[i] = cities[i].upper()
        if cities[i] in cache:
            result += 1
            cache.remove(cities[i])
            cache.insert(0,cities[i])
            if len(cache) == cachesize:
                cache.pop(0)
                cache.append(cities[i])
            elif len(cache) < cachesize:
                cache.append(cities[i])
        else:
            result += 5
            if len(cache) == cachesize:
                cache.pop(0)
                cache.append(cities[i])
            elif len(cache) < cachesize:
                cache.append(cities[i])
    return result




solution(2,	["a", "a", "a", "b", "b", "b", "c", "c", "c"] )