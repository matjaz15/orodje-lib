import itertools


def subsetsum(nums, target, steps, tolerance=0, return_only_indexees=False, include_rest=False):
    """Returns tupple with (steps) amount of values from list (nums), 
    whose sum is closest to (target) and falls in the (tolerance) +- field.
    (return_only_indexees) = returns tupple of indexees instead of values.
    (include_rest) = on zero findings, returns tupple of combination, 
    whose sum is closest to (target)."""
    
    closest = rest = []  
    indexrange = [i for i, j in enumerate(nums)]
    indexlist = list(itertools.combinations(indexrange, steps))
    permlist = itertools.combinations(nums, steps)
    limitmax = target + tolerance
    limitmin = target - tolerance
    
    if return_only_indexees:
        for i in indexlist:
            tup = ()
            for l in i:
                tup = tup + (nums[l],)
                
            tup_sum = sum(tup)
            if tup_sum == target:
                return i

            var = (abs(tup_sum - target), i)
            if include_rest:
                rest.append(var)
            if limitmin <= tup_sum <= limitmax:
                closest.append(var)
    else:
        for i in permlist:
            tup_sum = sum(i)
            if tup_sum == target:
                return i

            var = (abs(tup_sum - target), i)
            if include_rest:
                rest.append(var)
            if limitmin <= tup_sum <= limitmax:
                closest.append(var)

    return min(closest)[1] if closest else min(rest)[1] if include_rest else ()
    
    
def chunks(lst, n):
    """Explode list (lst) into smaller sub-lists where (n) is the max
    amount of elements in a sub-list."""
    
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        

        
nums = [5,10,5,6,3,7,12,32,16,74] 
test = subsetsum(nums,9,1,0, True, True)
print(test)
