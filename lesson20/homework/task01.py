"""
[难度: ⭐⭐⭐]
[所属知识点: 特征数量对线性回归的影响]
[预计完成时间: 15 分钟]

题目描述:
使用 fetch_california_housing 的全部 8 个特征训练
LinearRegression 模型。对比只用 AveRooms 的单特征模型,
输出两个模型的 R² 哪个更高,并解释原因。

提示: 多特征模型的 R² 通常更高,因为更多信息帮助预测。

示例:
    >>> # 输出单特征 R² 和多特征 R²
    >>> # 多特征的 R² 应更高
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def compare_models():
    """对比单特征与多特征线性回归"""
    # 加载数据
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    y = df['MedHouseVal']
    # 单特征模型
    X_single = df[['AveRooms']]
    # 多特征模型
    X_multi = df.drop(columns=['MedHouseVal'])
    # 切分数据
    X_s_train, X_s_test, y_train, y_test = train_test_split(
        X_single, y, test_size=0.2, random_state=42
    )
    X_m_train, X_m_test, _, _ = train_test_split(
        X_multi, y, test_size=0.2, random_state=42
    )
    # 训练单特征模型
    model_single = LinearRegression()
    model_single.fit(X_s_train, y_train)
    y_pred_single = model_single.predict(X_s_test)
    r2_single = r2_score(y_test, y_pred_single)
    # 训练多特征模型
    model_multi = LinearRegression()
    model_multi.fit(X_m_train, y_train)
    y_pred_multi = model_multi.predict(X_m_test)
    r2_multi = r2_score(y_test, y_pred_multi)
    # 输出结果
    print(f"单特征 R² (AveRooms): {r2_single:.4f}")
    print(f"多特征 R² (全部8个): {r2_multi:.4f}")
    print(f"多特征 R² 更高: {r2_multi > r2_single}")
    return r2_single, r2_multi


# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 运行对比
    print("测试1: 单特征 vs 多特征")
    r2_single, r2_multi = compare_models()

    # 测试 2: 验证多特征 R² 更高
    print("\n测试2: 验证多特征效果更好")
    assert r2_multi >= r2_single, \
        "多特征 R² 应 >= 单特征 R²"
    print("验证通过!")

    # 测试 3: R² 值范围检查
    print("\n测试3: R² 范围检查")
    print(f"单特征 R² <= 1: {r2_single <= 1}")
    print(f"多特征 R² <= 1: {r2_multi <= 1}")
