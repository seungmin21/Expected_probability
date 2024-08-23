import random
import json
import argparse

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config['items'], config['probabilities'], config['simulations']

def simulate_draws(items, probabilities, num_simulations):
    results = {item: 0 for item in items}
    
    for _ in range(num_simulations):
        drawn_item = random.choices(items, probabilities)[0]
        results[drawn_item] += 1
    
    return results

def print_results(results):
    for item, count in results.items():
        print(f"{item}는 {count}번 뽑혔습니다.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="뽑기 시뮬레이션")
    parser.add_argument('--config', type=str, required=True, help="사용할 뽑기의 설정 파일 경로")
    args = parser.parse_args()

    items, probabilities, num_simulations = load_config(args.config)
    results = simulate_draws(items, probabilities, num_simulations)
    
    print_results(results)
