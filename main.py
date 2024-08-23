import random

def simulate_draw():
    items = ['A', 'B', 'C', 'D', 'E']
    probabilities = [0.06, 0.10, 0.20, 0.32, 0.32]  # 각 아이템의 확률
    count = 0
    
    while True:
        count += 1
        drawn_item = random.choices(items, probabilities)[0]
        if drawn_item == 'A':
            break
    
    return count

# A를 뽑기 위해 몇 번 뽑기를 해야 하는지 10번 시뮬레이션
results = [simulate_draw() for _ in range(10)]
print(results)
