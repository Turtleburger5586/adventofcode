def take_distance(list1: list[int], list2: list[int]) -> int:
    distances: list[int] = []
    for i in range(0,len(list1)):
        distances.append(abs(sorted(list1)[i]-sorted(list2)[i]))

    return sum(distances)

def similarity_score(list1: list[int], list2: list[int]) -> int:
    similarity: list[int] = []
    for num in list1:
        multiplier: int = 0
        for num2 in list2:
            if num==num2:
                multiplier += 1
        similarity.append(num*multiplier)
    
    return sum(similarity)

list1: list[int] = []
list2:list[int] = []
puzzle_input = open('problem.txt', 'r')
for line in puzzle_input:
    data = line.split()
    list1.append(int(data[0]))
    list2.append(int(data[1]))

print(take_distance(list1,list2))
print(similarity_score(list1,list2))
    