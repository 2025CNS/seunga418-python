n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_scores = [(score / max_score) * 100 for score in scores]
average = sum(new_scores) / n
print(average)