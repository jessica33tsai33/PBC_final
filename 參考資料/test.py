"""
滿天星：
繪製100顆小星星：隨機產生的
1.小星星移動：  左上角到右下角移動  循環形式
2.隨機顏色 閃爍 修改一次
"""
import pygame,sys
# 導入隨機函數模塊
import random
# 窗體
screen = pygame.display.set_mode((800,600),0,0)
#座標值
xx = []
yy = []
# 加載圖片（如果需要替換成好看的背景圖片）
back = pygame.image.load("1.jpg")
"""
第六部分：初始化函數
"""
def init():
    # 循環迭代初始化
    for i in range(0,100):
        xx.append(random.randint(0,800))
        yy.append(random.randint(0,800))
"""
第四部分：業務邏輯處理區域
"""
def action():
    # 4.1 循環遍歷所有的事件監聽
    for event in pygame.event.get():
        # 4.2 判斷是否退出系統
        if event.type == pygame.QUIT:
            sys.exit()
    # 星星移動
    for i in range(len(xx)):
        # 1.更改座標值
        xx[i] += 1
        yy[i] += 1
        # 2.循環
        if xx[i] > 800:
            xx[i] = 0
        if yy[i] > 800:
            yy[i] = 0
"""
第五部分：圖形圖案繪製
"""
def paint():
    # 5.1 初始化字體
    pygame.font.init()
    # 5.2 設置字體樣式
    font = pygame.font.Font("OpenSans-Bold.ttf", 28)

    for i in range(len(xx)):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        # 5.3 設置字體內容以及顏色
        fontRead = font.render("*", True, (R, G, B))
        # 5.4 繪製小星星
        screen.blit(fontRead, (xx[i], yy[i]))

    # 月亮
    pygame.draw.circle(
        screen,  # 繪製在哪個窗體上
        (255, 255, 255),  # 圓的顏色
        (100, 100),  # 圓的圓心點座標
        50,  # 圓的半徑
        0)  # 圓的線寬 0默認是實心圓  >0 空心圓
    pygame.draw.circle(
        screen,  
        (0, 0, 0),  
        (80, 80),  
        50,  
        0)  

"""
第一部分 主函數(設置窗口信息)
"""
def menu():
    # 1.設置窗口標題
    pygame.display.set_caption("滿天星")
    # 2.死循環
    while True:
        # 3.填充背景顏色（R,G,B）
        screen.fill((0,0,0))
        # 繪製哪張圖，以及起始點位置
        screen.blit(back,(0,0))
        # 4.調用業務邏輯模塊
        action()
        # 5.調用圖形圖像繪製
        paint()
        # 控制刷新頻率，設置每隔10毫秒刷新一次屏幕
        pygame.time.delay(10)
        # 6.刷新屏幕
        pygame.display.update()

if __name__ == '__main__':
    init()
    menu()