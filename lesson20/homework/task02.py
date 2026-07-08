"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 学习曲线 / 训练集大小影响]
[预计完成时间: 20 分钟]

题目描述:
从 California Housing 数据集取前 500 条记录,
训练集比例从 0.1 到 0.9、步长 0.1。
对每个比例用 train_test_split 切分后训练
LinearRegression,记录训练集和测试集 R²。
返回各比例对应的两个 R² 列表。
用 random_state=42 保证可复现。

提示: 可用列表收集结果。

示例:
    >>> ratios, train_scores, test_scores = learning_curve()
    >>> # ratios = [0.1, 0.2, ..., 0.9]
    >>> # train_scores 为各比例对应的训练集 R²
    >>> # test_scores 为各比例对应的测试集 R²
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def learning_curve():
    """绘制学习曲线数据"""
    # 加载数据并取前 500 条
    data = fetch_california_housing(as_frame=True)
    df = data.frame.iloc[:500]
    X = df.drop(columns=['MedHouseVal'])
    y = df['MedHouseVal']
    ratios = [0.1, 0.2, 0.3, 0.4, 0.5,
              0.6, 0.7, 0.8, 0.9]
    train_scores = []
    test_scores = []
    for ratio in ratios:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=1 - ratio, random_state=42
        )
        model = LinearRegression()
        model.fit(X_train, y_train)
        # 训练集 R²
        train_pred = model.predict(X_train)
        train_r2 = r2_score(y_train, train_pred)
        # 测试集 R²
        test_pred = model.predict(X_test)
        test_r2 = r2_score(y_test, test_pred)
        train_scores.append(train_r2)
        test_scores.append(test_r2)
        print(f"比例 {ratio:.1f}: "
              f"训练 R²={train_r2:.4f}, "
              f"测试 R²={test_r2:.4f}")
    return ratios, train_scores, test_scores


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 运行学习曲线
    print("测试1: 学习曲线数据")
    ratios, train_scores, test_scores = learning_curve()

    # 测试 2: 验证返回列表长度
    print("\n测试2: 验证列表长度")
    print(f"ratios 长度: {len(ratios)}")
    print(f"train_scores 长度: {len(train_scores)}")
    print(f"test_scores 长度: {len(test_scores)}")

    # 测试 3: 验证训练 R² 通常高于测试 R²
    print("\n测试3: R² 关系")
    for i in range(len(ratios)):
        print(f"比例 {ratios[i]:.1f}: "
              f"train={train_scores[i]:.4f} >= "
              f"test={test_scores[i]:.4f} ? "
              f"{train_scores[i] >= test_scores[i]}")
