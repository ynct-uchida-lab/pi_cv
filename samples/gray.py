# ライブラリのインポート
import cv2

# mainメイン関数
def main():

    # 画像の読み込み
    img = cv2.imread('../data/lena.png')

    # グレースケールに変換
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 画像の要素数を確認
    print(img.shape)
    # グレースケール画像の要素数を確認
    print(gray_img.shape)

    # 画像を保存
    cv2.imwrite('../output/gray_lena.png', gray_img)

if __name__ == '__main__':
    main()

