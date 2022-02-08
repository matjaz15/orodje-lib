from itertools import combinations


def subsetsum(nums, target, steps, tolerance=0, return_only_indexees=False, include_rest=False) -> tuple:
    """
    Finds number combinations, whose sum is equal (or close) to desired value. 

    :param list nums: List of integers and floats.
    :param float target: Target sum-combination.
    :param int steps: Amount of combinations returned.
    :param float tolerance: Threshold of allowed candidates. Smaller values give more accurate results.
    :param bool return_only_indexees: Returns tupple of indexees instead of values.
    :param bool include_rest: On zero findings, returns the CLOESET sum-combination to (target). Ignores tolerance.
    :return: Tupple with (steps) amount of values whose sum falls in the (tolerance) +- field.
    :rtype: tuple
    """

    closest = []
    rest = []
    limitmax = target + tolerance
    limitmin = target - tolerance    
    indexrange = [i for i, j in enumerate(nums)] if return_only_indexees else nums
    for i in combinations(indexrange, steps):        
        tup = (nums[l] for l in i) if return_only_indexees else i
        tup_sum = sum(tup)
        if tup_sum == target:
            return i

        var = (abs(tup_sum - target), i)
        if include_rest:
            rest.append(var)
            continue
        if limitmin <= tup_sum <= limitmax:
            closest.append(var)
    return min(closest)[1] if closest else min(rest)[1] if include_rest else ()
    
def chunks(lst, n): 
    """
    Explode list into smaller chunks.

    :param list lst: List to explode.
    :param int n: Max amount of elements in a sub-object.
    :return: Sliced generator object.
    """
    
    for i in range(0, len(lst), n):
        yield lst[i:i + n]