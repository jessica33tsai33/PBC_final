# 108-1 商管程式設計期末專案 - 英語詞彙打字遊戲

[![hackmd-github-sync-badge](https://hackmd.io/4n9r7zceSIuWaCke7gShmA/badge)](https://hackmd.io/4n9r7zceSIuWaCke7gShmA)


## 遊戲主題
對於台灣學生來說，每當要準備多益、托福、雅思時勢必得花費許多心力加強單字能力，但是「背單字」這件事本身對許多人而言，是一件非常枯燥乏味，且令人沒有動力持續下去的事，因此我們組別設計了一款可以幫助使用者背單字的小遊戲將單字和遊戲做結合以期達到增進學生背單字的效果。

## 開發方法
運用Python的pygame套件，做出一個英文詞彙打字練習的小遊戲

## 系統設計
1. 遊戲開始前先產生 10 個單字(包含英文單字、中文意思、詞性)，顯示給玩家，等玩家備好單字後，按「space」，才進入遊戲
2. 按照順序產生剛剛在單字表裡的單字的中文，玩家需將正確的英文打出來
3. 當十個單字都考過時結束遊戲
4. 當錯誤的單字超過含 5 個時，提早結束遊戲
5. 顯示最後得分

## 程式架構與重要pseudocode
```python
Class Vocabulary
  設定單字表路徑，並把單字列表上的單字 append 到 voclist 中
Class vocaUnit
  把單字個體拆成英文、中文
def show_vocabulary
  設定背景與顯示單字表（一張單字表上有 10 個單字）
def createMap
  單字會一直在畫面中動，動的方向是如果碰到畫面的邊界就會反彈
  畫面顯示分數(score)、錯誤數(wrong)
def get_result
  設定遊戲結束（錯 5 個單字時遊戲就會提早結束）時背景與顯示成績
```
1. 初始化：字體與大小、視窗大小、時鐘
2. 變數宣告：分數(score)、單字序號(i)、錯誤次數(wrong)、移動速度(speed)、第幾個畫面(condition)、輸入的單字(text)
3. 路徑：單字表、單字列表(csv)檔、宣告 class
4. 遊戲開始：一進入遊戲就顯示單字表 (if condition=1 ，跳到show_vocabulary)，使用者背完單字後按下 space 就進入遊戲畫面(if condition=2，跳到 createMap)，一開始時單字序號 i = 0，答了一個單字後 i+=1 ，答對 (text=vocalist.english)score+=1 答錯 wrong+=1 ，直到 i=10 或 wrong=5 時遊戲就會結束，(if condition=3 ，跳到 get_result)
5. 主程式
```
  初始化、變數宣告、讀入路徑檔案
  隨機從 1~15 挑一個數字
  顯示單字表
  If 按離開鍵：
    就結束遊戲
  If 按 space：
    進入遊戲畫面
  If 按 enter：
    If 錯誤小於 4：
      If 已出現單字數 <10 個：
        If 打對：
          分數加一、單字換到下一個、文字清空
        If 打錯：
          錯誤分加一、單字換到下一個、文字清空
      If 已出現單字數是第 10 個：
        If 打對：
          分數加一、遊戲結束
        If 打錯：
          遊戲結束
    If 錯誤 = 4：
      If 已出現單字數 <10 個：
        If 打對：
          分數加一、遊戲結束
        If 打錯：
          遊戲結束
  If按 backspace：
    將文字最後一字刪除
  If按其他鍵：
    將輸入的字加到文字裡
```

last update：108/12

###### tags: `PBC` `GitHub` `Python` `pygame`