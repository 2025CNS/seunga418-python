scores = []
for _ in range(5):
    score = int(input())
    if score < 40:
        scores.append(40)
    else:
        scores.append(score)
total_score = sum(scores)
average_score = total_score // 5
print(average_score)