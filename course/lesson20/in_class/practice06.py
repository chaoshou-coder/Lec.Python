"""
[难度: ⭐⭐⭐]
[所属知识点: 误差分析 / MAE]
[预计完成时间: 15 分钟]

题目描述:
在 practice05 的基础上,计算测试集的平均绝对误差(MAE),
并找出预测误差最大的前 5 个样本,
输出它们的真实值和预测值。

提示: 可使用 numpy.argsort 或 pandas。

示例:
    >>> # 输出 MAE 的值
    >>> # 输出误差最大的 5 个样本及其真实值/预测值
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np


def error_analysis():
    """对房价预测模型进行误差分析"""
    # 加载数据
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    X = df[['AveRooms']]
    y = df['MedHouseVal']
    # 切分数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # 训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # 计算 MAE
    mae = mean_absolute_error(y_test, y_pred)
    print(f"测试集 MAE: {mae:.4f}")
    # 找出误差最大的前 5 个样本
    errors = np.abs(y_test.values - y_pred)
    top5_idx = np.argsort(errors)[-5:][::-1]
    print("\n误差最大的 5 个样本:")
    print(f"{'真实值':>8} {'预测值':>8} {'误差':>8}")
    print("-" * 28)
    for idx in top5_idx:
        true_val = y_test.values[idx]
        pred_val = y_pred[idx]
        err = errors[idx]
        print(f"{true_val:>8.4f} {pred_val:>8.4f} {err:>8.4f}")
    return mae, top5_idx


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 运行误差分析
    print("测试1: 误差分析")
    mae, top5 = error_analysis()

    # 测试 2: 验证 MAE > 0
    print("\n测试2: 验证 MAE 为正数")
    print(f"MAE = {mae:.4f}")
    print(f"MAE > 0: {mae > 0}")

    # 测试 3: 误差最大样本数量
    print("\n测试3: 验证返回 5 个样本")
    print(f"返回样本数: {len(top5)}")
