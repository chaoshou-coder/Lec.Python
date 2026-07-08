"""
[难度: ⭐⭐⭐⭐]
[所属知识点: 交叉熵损失 / Log-Softmax / 数值稳定]
[预计完成时间: 20 分钟]

手写数字识别(10 类)使用交叉熵损失。请按以下步骤实现:
1) log_softmax(x) = x - max(x) - log(sum(exp(x - max(x))))
2) cross_entropy(y_true, x) = -sum(y_true * log_softmax) / n
3) 梯度 dL/dx = (softmax(x) - y_true) / n
返回 (loss, grad)。使用 one-hot 格式的标签 y_true。

示例:
    >>> y = np.array([[1,0,0,0,0,0,0,0,0,0]])
    >>> logits = np.array([[2.0,1.0,0.1,0,0,0,0,0,0,0]])
    >>> loss, grad = cross_entropy(y, logits)
    >>> loss < 1
    True
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
pass

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 单样本 10 类
    # 测试 2: 批量 3 样本,验证梯度 shape
    pass
