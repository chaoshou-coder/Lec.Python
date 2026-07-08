# Day23 · 聚类 + 降维

> 本节时长: 6 小时(约 6 节 × 45 分钟)
> 前置: Day22 已掌握分类模型选型、SVM 核技巧直觉;Day18 已建立监督/无监督直觉
> 关键问题: 没标签,怎么让数据"自己说话"?100 维数据没法画图,怎么"看见"
  它的结构?

---

## 0. 引入(5 分钟)

- **抽问上节**(2 分钟): 让学员口答 —— SVM 的"核"到底做了什么(直觉)?随机森
  林的特征重要性怎么算?目的: 唤醒上节记忆,自然切换到今天主题。
- **赏玩 demo**(3 分钟): 投影一幅"500 × 100 维"数据 PCA 降到 2D 的散点点
  云(每点一簇颜色,即使没有标签也看得出来有几"坨")。说:"虽然没有 y,人类
  一眼就能看出分 3 类 —— 这就是**无监督**。"

---

## 1. 第一讲(15 分钟) —— K-Means:最经典的聚类算法

### 知识点 1.1 K-Means 流程(动画式)

1. 随机选 K 个"质心"(centroid)。
2. 每个点归入最近的质心 → 形成 K 个簇。
3. 每个簇重新算质心(本簇的点取平均)。
4. 重复 2-3,直到质心不再动(收敛)。

类比:选 K 个班委,每个同学跟最近的班委;班委换位置到追随者中心;反复几次
班委原地不动 —— 收敛结束。

### 知识点 1.2 sklearn 5 行跑通 K-Means

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

X, y = load_iris(return_X_y=True)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

print("质心 shape:", model_centers_.shape)  # (3, 4)
print("每条簇标签:", model.labels_[:10])
# 注意:模型给的标签(0,1,2)和原 y 的标签**不一定对应**,只代表"第几簇"
```

> 🔴 教学红线: 学员常拿 KMeans 预测的 `labels_` 与 `y` 比较"准确率"。注意:
> **KMeans 不知道真实标签**,它只做"把相似点凑一起",无法评价对错(真实应用
> 中也没标签可评价)。评价要用**轮廓系数**(见下)而不是准确率。

### 知识点 1.3 肘部法则:怎么选 K?

```python
inertias = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertias.append(model.inertia_)  # 簇内平方和

import matplotlib.pyplot as plt
plt.plot(range(1, 11), inertias, marker="o")
plt.xlabel("K")
plt.ylabel("Inertia(簇内平方和)")
plt.title("肘部法则")
plt.show()
# 拐点处(一般 K=3)是"最佳 K" —— 再多分簇,收益微小
```

> 肘部图看起来像一个手臂,"肘部"对应的 K 是最经济选择。

### 知识点 1.4 轮廓系数:聚类质量评分

轮廓系数 s(i) ∈ [-1, 1]:
- 接近 1:点离自己簇近、离别人远(好)
- 接近 0:在两簇边界(犹豫)
- 接近 -1:分错簇(差)

```python
from sklearn.metrics import silhouette_score

for k in range(2, 6):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    score = silhouette_score(X, labels)
    print(f"K={k} 轮廓系数: {score:.4f}")
# K=2 轮廓系数: 0.68...
# K=3 轮廓系数: 0.55...
# K=4 轮廓系数: 0.49...
# K=5 轮廓系数: 0.47...
```

## 2. 当堂练 1(20 分钟)

- 练习 1: `in_class/practice01.py` —— iris 数据集 KMeans(n_clusters=3),与真实
  y 做交叉表(`pd.crosstab`),看哪些类分得好、哪些类易混淆(⭐⭐,10 分钟)
- 练习 2: `in_class/practice02.py` —— 画 elbow 图 + 轮廓系数图,双指标联合确
  定最适 K(⭐⭐⭐,15 分钟)

> 巡场重点: 学员常直接在 clustering 后算 accuracy —— 提示:**没有标签就没有
  准确率**,用轮廓系数。

---

## 3. 第二讲(15 分钟) —— 层次聚类 + DBSCAN 直觉

### 知识点 3.1 层次聚类(Agglomerative Clustering)

从"每个点单独一类"开始,每次**合**最近的两个簇,最终形成一棵**树状图**(den
drogram)。

```python
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X)
```

> 优点:**不需要预先指定 K**,可以从树状图上任选切一刀定 K。
> 缺点:大数据集慢(O(n²))。

### 知识点 3.2 DBSCAN:基于密度 —— 不需要人为选 K

直觉:把"点密的地方"归为一簇,"孤立的稀疏点"当成**噪声**。

```python
from sklearn.cluster import DBSCAN

model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X)
print(set(labels))  # 可能包含 -1 = 噪声点
```

| 参数 | 含义 |
|---|---|
| `eps` | 邻域半径 |
| `min_samples` | 成为核心点的最少邻居数 |

> DBSCAN 天然能处理"任意形状的簇"和"噪声",这是 K-Means 做不到的。但 `eps` 和
> `min_samples` 需要调,**调参即调世界观**。

## 4. 当堂练 2(25 分钟)

- 练习 3: `in_class/practice03.py` —— 用 `make_moons` 造两个半月形数据,对
  比 KMeans(n_clusters=2) 和 DBSCAN(eps=0.2) 的聚类结果**可视化**(⭐⭐⭐⭐,
  15 分钟)

> 巡场重点:KMeans 在半月形上表现灾难(因为它假设簇是"凸的/圆球状的"),这是
> K-Means 的**致命局限**。

---

## 5. 第三讲(15 分钟) —— PCA 与 t-SNE:降维可视化

### 知识点 5.1 PCA:方差最大化直觉

🔴 **严格边界 —— 不讲特征值推导,只讲直觉**: PCA 把原始数据投影到一个新坐标系,
让**投影后数据方差(信息)最大的轴作为第一主成分**,次大的作为第二,依次。

类比:拍集体照 —— 找到"拍出来每个人脸最清晰"的角度,那个角度就是"信息最大的
方向"。

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)   # 降到 2 维
X_2d = pca.fit_transform(X)
print("解释方差比:", pca.explained_variance_ratio_)
# [0.92, 0.05]  ← PC1 保住 92% 信息,PC2 保住 5%,合计 97%
```

> 解释方差比之和 ≈ 97% 表示:"把 4 维压到 2 维,只丢了 3% 信息"。

### 知识点 5.2 什么时候用 PCA?

- 特征过多(>50),怀疑共线性 → PCA 降维 + 送模型(如逻辑回归/SVM)。
- 可视化(强制降到 2D 或 3D 画图)。
- **不要**在有强业务意义的特征上 PCA —— 降维后**解释性变差**,业务部门看不懂。

### 知识点 5.3 t-SNE:高维数据可视化的利器

t-SNE 也是降到 2D/3D,**但专门为可视化设计**,不做逆变换。

```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
X_2d = tsne.fit_transform(X)
# 画散点图:同类应该聚在一起
```

| | PCA | t-SNE |
|---|---|---|
| 目标 | 保留全局结构 | 保留局部结构(让近邻保持近邻) |
| 可逆? | ✅ | ❌(仅可视化) |
| 速度 | 快 | 慢 |
| 用途 | 预处理/降维 | **可视化** |

## 6. 当堂练 3(25 分钟)

- 练习 4: `in_class/practice04.py` —— iris 数据集:
  (a) 用 PCA 降到 2D,画散点图;解释方差比多少?
  (b) 用 t-SNE 降到 2D,画散点图;
  (c) **对比**:哪个让三类"分得更开"?为什么?(⭐⭐⭐⭐,20 分钟)

> 巡场重点: 学员易认为"t-SNE 比 PCA 好"—— 错。它们解决不同问题,t-SNE 只是
> 让可视化好看,不能做预处理(不能逆变换)。

---

## 7. 小项目(若本日有,45 分钟)

**无监督探索报告**:

给一组无标签客户购买数据(含 age / income / 购买金额 / 频次),要求:

1. KMeans 聚类(K 用 elbow + 轮廓双指标定)。
2. 每个簇做业务画像("年轻高消费"、"中年低频次"...)。
3. PCA/t-SNE 降到 2D 画图,标出各簇。
4. 给业务部门写 100 字"你的客户分几类"报告。

---

## 8. 总结(5 分钟)

- **本日错 3 件事**:
  1. KMeans 直接和真实 y 比"准确率"(无监督没正确答案)
  2. PCA 降维到 2D 直接送进模型(丢掉信息可能影响预测)
  3. t-SNE 当作"降维预处理"用(它不能逆变换,不可用于送模型)
- **作业说明**: 课后 `homework/task01.py`(KMeans + 轮廓系数 + elbow 三件套 on
  加利福尼亚房价 feats)、`homework/task02.py`(t-SNE vs PCA 可视化对比 + 100
  字洞察)。

---

## 易错点

1. **KMeans 假设簇是凸形**:对环形/半月形数据彻底失败,改用 DBSCAN/谱聚类。
2. **`n_init` 不设置**: KMeans 跑一次(n_init=1)可能收敛到局部最优,设
   `n_init=10` 跑多次选最好结果。
3. **PCA 降维后送树模型**: 树模型需要原始特征排序共线性信息,PCA 后维度失
   去物理意义反而可能掉分。
4. **t-SNE `perplexity` 调参**: 默认 30 一般 OK,数据集极小(<50)要调低。
5. **评价聚类用 accuracy**: 无监督场景用轮廓系数 + 业务解读,不要硬凑 label。

## 延伸题

- **KMeans 初始化 K-Means++(⭐⭐)**: sklearn 默认就是 `init="k-means++"`,了
  解它让初始质心尽可能远离 —— 避免"两质心挤一簇"的情况。
- **DBSCAN 参数选择实验(⭐⭐⭐)**: 用 `NearestNeighbors` 画 K-distance 图,
  选"拐点"作为 `eps`。
- **UMAP(⭐⭐⭐⭐)**: t-SNE 替代,保留全局结构更强,大数据更快 — 扩展了解。
