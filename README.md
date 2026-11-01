# free-cpu-lab

用 GitHub Actions 的免费算力跑 CPU 算法实验。

- 公开仓库的 Actions **完全免费**，单任务 2 核 4G，最多 20 个任务同时并行(约 40 核)
- 单任务上限 6 小时，超时任务要自己存档续跑
- `experiment/run.py` 是演示用的蒙特卡洛算圆周率，替换成你自己的算法即可
- 触发方式: ① 改动 `experiment/` 下任何文件自动触发 ② 手动触发(可设采样数)
- 结果在每次运行的 Artifacts 里下载(网页 Actions 页 -> 点进运行 -> 底部 Artifacts)

## 文件结构
- `.github/workflows/run.yml` — 流水线定义(matrix 并行 4 任务,可加到 20)
- `experiment/run.py` — 实验代码(演示: Monte Carlo pi)
