from electorate import Electorate


def find_district(electorate, voter, found, count):
    count += 1
    if count == electorate.district_size():
        return [voter]
    found[voter] = True
    for neighbor in electorate.graph.neighbors(voter):
        if not found[neighbor]:
            result = find_district(electorate, neighbor, found, count)
            if result:
                return result + [voter]
    return None


e = Electorate(3)
print(find_district(e, 0, [False] * 9, 0))
