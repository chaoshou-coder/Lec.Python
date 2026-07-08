"""
[难度: ⭐⭐]
[所属知识点: 张量基本运算（加减乘除、广播）]
[预计完成时间: 10 分钟]

神经网络前向传播里常做张量四则运算。请完成以下练习，熟悉
逐元素运算、矩阵乘法与广播机制。

任务:
  1) 创建 a=torch.tensor([[1.0,2.0],[3.0,4.0]]),
           b=torch.tensor([[5.0,6.0],[7.0,8.0]]);
  2) 计算 a+b, a*b（逐元素乘）, a @ b（矩阵乘）, a/2；
  3) 广播：c=torch.tensor([1.0,2.0])，计算 a+c；
  4) 逐行打印结果。

示例:
    >>> python3 practice02.py
    a+b:
     tensor([[ 6.,  8.],
             [10., 12.]])
    ...
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
# 学员请在此处实现
import torch

# 1) 创建两个 2x2 的浮点张量
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# 2) 四则运算与矩阵乘
add_res = a + b        # 逐元素加
mul_res = a * b        # 逐元素乘
mat_res = a @ b        # 矩阵乘法
div_res = a / 2        # 逐元素除以标量

# 3) 广播：行向量加到每一行
c = torch.tensor([1.0, 2.0])
broadcast_res = a + c

# 4) 逐行打印结果
print("a+b:\n", add_res)
print("a*b (逐元素):\n", mul_res)
print("a@b (矩阵乘):\n", mat_res)
print("a/2:\n", div_res)
print("a+c (广播):\n", broadcast_res)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: 验证逐元素加法
    expected_add = torch.tensor([[6., 8.], [10., 12.]])
    assert torch.allclose(add_res, expected_add)

    # 测试 2: 验证矩阵乘法结果
    expected_mat = torch.tensor([[19., 22.], [43., 50.]])
    assert torch.allclose(mat_res, expected_mat)

    # 测试 3: 广播后第一行应为 [2., 4.]
    expected_broadcast_row0 = torch.tensor([2., 4.])
    assert torch.allclose(broadcast_res[0], expected_broadcast_row0)
    print("所有测试通过!")
