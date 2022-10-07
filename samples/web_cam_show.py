# ライブラリのインポート
import os
import cv2

# main関数
def main():
    # カメラを取得
    cap = cv2.VideoCapture(0)
    
    # 無限ループ
    while True:
        # フレームを取得
        ret, frame = cap.read()
        # フレームを取得できない場合
        if not ret:
            # ループを抜ける
            break

        # フレームを表示
        cv2.imshow("Frame", frame)

        # キー入力待ち(1ms)
        key = cv2.waitKey(1)
        # 入力が'q'の場合
        if key == ord('q'):
            # ループを抜ける
            break

    # メモリの開放
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

