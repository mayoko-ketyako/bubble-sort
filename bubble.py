# 配列Suにデータを記憶する（データ件数はn件）
Su = ["peach", "melon", "apple", "grape", "strawberry", "banana", "orange", "litchi", "kiwi", "pineapple"]
n = len(Su)
print(f"元の配列: {Su}")
print(f"データ件数：{n}件")

# バブルソートの実行
for g in range(n - 1, 0, -1):  # 外側のループは配列の長さ-1から1まで
    for j in range(0, g, 1):  # 内側のループは0からg-1まで
        if Su[j] < Su[j + 1]:  # 降順にするために「<」を使用
            Hozon = Su[j]
            Su[j] = Su[j + 1]  # 隣接要素を交換
            Su[j + 1] = Hozon

for k in range(n):  # 整列後の配列を出力
    print(f"Su({k}): {Su[k]}")
