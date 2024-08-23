import random

def simulate_draws(num_simulations):
    items = ['A', 'B', 'C', 'D', 'E']
    probabilities = [0.06, 0.10, 0.20, 0.32, 0.32]  # 각 아이템의 확률
    results = {item: 0 for item in items}  # 각 아이템의 뽑힌 횟수를 기록하는 딕셔너리
    
    for _ in range(num_simulations):
        drawn_item = random.choices(items, probabilities)[0]
        results[drawn_item] += 1  # 뽑힌 아이템의 횟수를 증가시킴
    
    return results

# 10번 시뮬레이션
num_simulations = 10
results = simulate_draws(num_simulations)

# 결과 출력
for item, count in results.items():
    print(f"{item}: {count}번 뽑혔습니다.")
