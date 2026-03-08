# CIPDA - 国产化打桩分析软件

**Chinese Pile Driving Analysis**

## 项目简介

CIPDA 是一款国产化打桩分析软件，旨在实现 GRLWEAP 等国际主流软件的核心功能复刻与自主创新。

## 核心功能

- **波动方程分析** (Wave Equation Analysis)
- **锤击能量计算** (Hammer Energy Calculation)
- **桩身应力分析** (Pile Stress Analysis)
- **承载力预测** (Bearing Capacity Prediction)
- **土阻力模型** (Soil Resistance Model)

## 技术栈

- Python 3.x
- NumPy / SciPy - 数值计算
- Matplotlib - 数据可视化
- PySide6 - GUI界面

## 项目结构

```
CIPDA/
├── src/           # 源代码
│   ├── core/      # 核心算法
│   ├── gui/       # 图形界面
│   └── utils/     # 工具函数
├── docs/          # 文档
├── tests/         # 测试
├── examples/      # 示例
└── data/          # 数据文件
```

## 版本管理

- **主分支**: main（保持稳定）
- **开发分支**: dev（日常开发）
- **版本发布**: 每三天自动推送版本

## 开发日志

见 [CHANGELOG.md](./CHANGELOG.md)

## 许可证

MIT License

---

*国产替代 · 自主可控*