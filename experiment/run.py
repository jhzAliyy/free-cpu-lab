import argparse, json, os, time
import multiprocessing as mp
import random

def estimate_pi(n):
    """蒙特卡洛法估算圆周率: 投 n 个随机点, 纯 CPU 密集演示"""
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1.0:
            inside += 1
    return inside

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--task', type=int, default=1, help='任务编号')
    p.add_argument('--samples', type=int, default=100, help='每进程采样数(百万)')
    a = p.parse_args()

    n = a.samples * 1_000_000
    t0 = time.time()
    with mp.Pool(2) as pool:                      # 免费 runner 是 2 核
        results = pool.map(estimate_pi, [n, n])
    total = 2 * n
    pi = 4 * sum(results) / total
    dt = time.time() - t0

    os.makedirs('results', exist_ok=True)
    info = {
        'task': a.task,
        'total_samples': total,
        'pi_estimate': pi,
        'error': abs(pi - 3.141592653589793),
        'seconds': round(dt, 1),
        'cpu_cores': os.cpu_count(),
    }
    with open(f'results/task{a.task}.json', 'w') as f:
        json.dump(info, f, indent=2)
    print(json.dumps(info, indent=2))

if __name__ == '__main__':
    main()
