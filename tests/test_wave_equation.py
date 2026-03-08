"""测试波动方程求解器"""

import sys
sys.path.insert(0, '..')

from src.core.wave_equation import WaveEquationSolver


def test_wave_speed():
    """测试波速计算"""
    solver = WaveEquationSolver(pile_length=20, pile_area=0.1)
    
    # 钢桩波速应约为 5120 m/s
    expected = 5120
    actual = solver.c
    
    assert abs(actual - expected) < 100, f"波速计算错误: 期望 {expected}, 实际 {actual}"
    print(f"✓ 波速测试通过: {actual:.2f} m/s")


if __name__ == "__main__":
    test_wave_speed()