def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


def three_item_not_freq(powerset, tree_items_set):
    out = []
    for l in powerset:
        if len(l) == 3 and l not in tree_items_set:
            out.append(l)
    return out

def not_freq_4_items_set(powerset, nfis):
    out = []
    for p in powerset:
        if len(p) == 4:
            flag = True
            for n in nfis:
                if set_in_set(n, p):
                    flag = False
            if flag:
                out.append(p)
    return out


def set_in_set(s1, s2):
    for s in s1:
        if s not in s2:
            return False
    return True


def from_3_item_set(power, freq_list):
    four_list = [p for p in power if len(p) == 4]
    out = []
    for p in four_list:
        i = 0
        for f in freq_list:
            if set_in_set(f, p):
                i += 1
        if i >= 2:
            out.append(p)
    return out



# find the subsets of below vector.
array = ['a', 'b', 'c', 'd', 'e', 'f']


freq_sets = [['a', 'b', 'c'], ['a', 'b', 'd'],
              ['a', 'b', 'e'], ['a', 'c', 'd'], ['a', 'c', 'e'],
              ['a', 'c', 'f'],['a', 'd', 'f'], ['b', 'c', 'd'], ['b', 'c', 'e'],
              ['b', 'd', 'f'], ['c', 'd', 'e'], ['c', 'd', 'f']]

r = [x for x in powerset(array)]

#print(r)

not_freq = three_item_not_freq(r, freq_sets)

print(not_freq)
not_freq_4_itm = not_freq_4_items_set(r, not_freq)
print(not_freq_4_itm)
print(len(not_freq_4_itm))
print(len([p for p in r if len(p) == 4]))
print(['d', 'e', 'f'] in ['d', 'e', 'f'])
print(from_3_item_set(r, freq_sets))



