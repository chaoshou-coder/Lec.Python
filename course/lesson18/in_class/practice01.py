"""
[难度: ⭐]
[所属知识点: train_test_split 原理]
[预计完成时间: 5 分钟]

手写一个简单版的 `my_train_test_split` —— 接收 X(列表的列表)、
y(列表)、test_ratio(浮点数),返回 X_train, X_test, y_train, y_test。
使用 sklearn.datasets 的 load_iris 函数导入数据,取前 30 条作为输入,
测试比例设为 0.2。使用 int(比例×总数) 切分测试集,其余为训练集。

提示: 可使用 numpy.random.permutation 打乱索引。

示例:
    >>> X = [[1,2],[3,4],[5,6],[7,8]]
    >>> y = [0,1,0,1]
    >>> X_train,X_test,y_train,y_test = my_train_test_split(X,y,0.5)
    >>> len(X_test)
    2
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 导入所需模块
    # from sklearn.datasets import load_iris
    # import numpy as np
    #
    # 载入 iris 数据并取前 30 条
    # iris = load_iris()
    # X = iris.data[:30].tolist()
    # y = iris.target[:30].tolist()
    #
    # 调用学员实现的函数
    # X_train, X_test, y_train, y_test = my_train_test_split(
    #     X, y, 0.2
    # )
    #
    # 验证测试集长度为 6(int(30 * 0.2) = 6)
    # print("测试集 y 长度:", len(y_test))  # 应输出 6
    # print("训练集 y 长度:", len(y_train))  # 应输出 24
    # print("总长度:", len(y_test) + len(y_train))  # 应输出 30
    #
    # 断言检查(全部通过说明实现正确)
    # assert len(y_test) == 6
    # assert len(y_train) == 24
    # assert len(y_test) + len(y_train) == 30
    pass
