"""
[难度: ⭐⭐⭐]
[所属知识点: LinearRegression + 真实数据]
[预计完成时间: 15 分钟]

题目描述:
从 sklearn.datasets.fetch_california_housing 加载数据集,
取 "AveRooms"(平均房间数)作为唯一特征,
目标为 MedHouseVal(房价中位数)。
用 train_test_split 切分(test_size=0.2),
训练线性回归模型,输出测试集的 MSE 和 R²。

提示: from sklearn.datasets import fetch_california_housing

示例:
    >>> # 输出测试集 MSE 和 R²(数值因随机性略有不同)
    >>> # 使用 random_state=42 可复现
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def california_single_feature():
    """使用 AveRooms 单特征预测 California 房价"""
    # 加载数据
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    # 使用 AveRooms 作为唯一特征
    X = df[['AveRooms']]
    y = df['MedHouseVal']
    # 切分数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # 训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    # 预测与评估
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"测试集 MSE: {mse:.4f}")
    print(f"测试集 R²:  {r2:.4f}")
    print(f"系数: {model.coef_[0]:.4f}")
    print(f"截距: {model.intercept_:.4f}")
    return model, mse, r2


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 运行单特征模型
    print("测试1: AveRooms 单特征预测")
    model, mse, r2 = california_single_feature()

    # 测试 2: 验证模型参数
    print("\n测试2: 查看模型信息")
    print(f"R² > 0: {r2 > 0}")
    print(f"MSE > 0: {mse > 0}")

    # 测试 3: 预测新数据
    print("\n测试3: 预测 AveRooms=5 的房价")
    pred = model.predict(np.array([[5]]))
    print(f"预测房价中位数: {pred[0]:.4f}")
