import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

# 二次元正規分布の確率密度を返す関数
def gaussian(x, sigma, mu):
    # 分散共分散行列の行列式
    det = np.linalg.det(sigma)
    # 分散共分散行列の逆行列
    inv = np.linalg.inv(sigma)
    n = x.ndim
    return np.exp(-np.diag((x - mu)@inv@(x - mu).T)/2.0) / (np.sqrt((2 * np.pi) ** n * det))

def main():
    # 関数に投入するデータを作成
    x = y = np.arange(-3, 3, 0.1)
    mash_x, mash_y = np.meshgrid(x, y)

    z = np.c_[mash_x.ravel(), mash_y.ravel()]

    # 変数x, yの平均値を指定
    mu = np.array([0, 0])
    # 変数x, yの分散共分散行列を指定
    sigma = np.array([[1, 0], [0, 1]])
    
    # ガウシアン分布を計算
    g = gaussian(z, sigma, mu)
    # 二次元にreshape
    g = g.reshape(mash_x.shape)

    # 二次元正規分布をplot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # 描画
    ax.plot_surface(mash_x, mash_y, g, rstride=1, cstride=1, cmap=cm.coolwarm)
    plt.savefig('../../output/metadata/2_gaussian.png')

if __name__ == '__main__':
    main()

