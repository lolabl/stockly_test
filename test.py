def recursive_use_shortcut(a, temp_result, i):
    if i >= destination:
        return temp_result + abs(i - destination)
    return min(recursive_use_shortcut(a, temp_result + 1, max(a[i-1], i+1)), temp_result + abs(i - destination))

def second_recursion()
n = int(input())
a = list(map(int,input().split(' ')))
result = [i-1 for i in range(1,n+1)]
for destination in range(1, n+1):
    for intersection in range(1, destination):
        temporary_result = intersection - 1
        result[destination - 1] = min(result[destination - 1], recursive_use_shortcut(a, temporary_result, intersection))
print(' '.join(map(str, result)))
        