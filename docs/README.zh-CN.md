# OMR 中文说明

**Outcome-Matched Retrieval（OMR）** 利用同一条轨迹中“观测端点”和“从更早时刻预测到同一端点”的多视角关系，学习面向目标的动作检索度量。检索头只负责选择动作先验；世界模型的原目标代价仍然负责轨迹优化和最终选择。

## 快速开始

```bash
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
uv pip install -r requirements.txt
uv pip install -e . --no-deps
python scripts/check_runtime.py
python scripts/verify_release.py
```

复现主实验需要外部 HDF5 数据和 SHA 完全一致的四个冻结世界模型 checkpoint；见 `docs/REPRODUCIBILITY.md`。仓库已包含检索库、九个学习头、离线特征、128 个确认 root 和完整逐回合结果。

## 主要结果

| 环境 | 成功率 (%) | 95% CI |
|:--|--:|:--|
| TwoRoom | 97.40 | [94.66, 99.48] |
| PushT | 91.02 | [86.98, 94.53] |
| Cube | 86.46 | [81.51, 91.02] |
| Reacher | 85.55 | [81.12, 89.71] |
| 平均 | 90.10 | [88.09, 91.99] |

完整矩阵为 24,576 回合，包含匹配 CEM、纯检索、几何/偏好/时间引导及结构消融。结果没有按分数筛选。
