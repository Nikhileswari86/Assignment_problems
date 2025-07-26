def is_more_than_half_overlap(pos1, pos2):
    
    l1, r1 = pos1
    l2, r2 = pos2
    len1 = r1 - l1
    len2 = r2 - l2

    
    overlap = max(0, min(r1, r2) - max(l1, l2))

    return (overlap > len1 / 2) or (overlap > len2 / 2)


def combine_lists(list1, list2):
    combined = []
    used = set()

    for i, elem1 in enumerate(list1):
        merged = False
        for j, elem2 in enumerate(list2):
            if j in used:
                continue
            if is_more_than_half_overlap(tuple(elem1['positions']), tuple(elem2['positions'])):
                merged_elem = {
                    'positions': elem1['positions'],
                    'values': elem1['values'] + elem2['values']
                }
                combined.append(merged_elem)
                used.add(j)
                merged = True
                break
        if not merged:
            combined.append(elem1)

    
    for j, elem2 in enumerate(list2):
        if j not in used:
            combined.append(elem2)

    
    combined.sort(key=lambda x: x['positions'][0])
    return combined


if __name__ == "__main__":
    import json

    print("Enter first list (JSON format):")
    list1 = json.loads(input())
    
    print("Enter second list (JSON format):")
    list2 = json.loads(input())

    result = combine_lists(list1, list2)

    print("\nCombined and sorted list:")
    print(json.dumps(result, indent=4))
