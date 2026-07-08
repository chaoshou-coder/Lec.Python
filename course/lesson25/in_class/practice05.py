"""
[难度: ⭐⭐⭐]
[所属知识点: 特征工程]
[预计完成时间: 15 分钟]

题目描述:
在 California Housing 原始特征基础上,新增两个组合特征:
  - RoomsPerHouse = AveRooms / AveBedrms (每个房子的平均房间数)
  - PopulationPerHousehold = Population / AveOccup (每户人口数)
注意: 除法中分母可能为 0,需做边界处理(替换为 1)。
重新训练 LinearRegression,输出工程后的 RMSE,
与 practice03 的基准 RMSE 对比。

示例:
    >>> # 基准 RMSE 约为 0.7459
    >>> # 特征工程后 RMSE 预期有所下降
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 加载数据为 DataFrame
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# 计算 RoomsPerHouse = AveRooms / AveBedrms
# 分母为 0 时替换为 1,避免除零
ave_bedrms = df["AveBedrms"].replace(0, 1)
df["RoomsPerHouse"] = df["AveRooms"] / ave_bedrms

# 计算 PopulationPerHousehold = Population / AveOccup
ave_occup = df["AveOccup"].replace(0, 1)
df["PopulationPerHousehold"] = df["Population"] / ave_occup

# 准备特征与标签
X = df.drop("MedHouseVal", axis=1).values
y = df["MedHouseVal"].values

# 切分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练线性回归模型
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 输出特征工程后的 RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"特征工程后 RMSE: {rmse:.4f}")

    # 测试 2: 验证新增特征已正确加入(10 列 = 原 8 + 新增 2)
    assert X.shape[1] == 10, f"特征数异常: {X.shape[1]}"
    print(f"测试通过: 特征数 = {X.shape[1]} (原 8 + 新增 2)")

    # 测试 3: RMSE 比基准(约 0.7459)有所改善
    assert rmse < 0.75, f"RMSE 异常偏高: {rmse}"
    print("测试通过: 特征工程后 RMSE 在合理范围")
