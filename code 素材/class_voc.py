import random


class Vocabulary:
    '''
    class單字們
    包含英文單字、中文意思、詞性、開頭結尾
    '''

    # 隨機讀入voc的第n個csv，並將裡面的單字做成一個word_list
    def read_in():
        n = random.randint(1, 15) # 從1~15隨機產生一個數字
        fn = 'C:\\Users\\ASUS\\Desktop\\third\\program\\vocab\\voc' + str(n) + '.csv'  # 這是我電腦裡csv的路徑，不知道怎麼改成github上可共用的QQ
        fh = open(fn, 'r', encoding="utf-8")
        line = fh.readline()
        line = line.encode('utf-8').decode('utf-8-sig')
        line = line.strip('\n')
        word_list = []
        while line:
            line = line.split(',')
            cin = Vocabulary()
            cin.english = line[0]  # english屬性:英文單字
            cin.property = line[1]  # property屬性:詞性
            cin.chinese = line[2]  # chinese屬性:中文解釋
            cin.letter = line[3]  # letter屬性:第一個和最後一個字母
            # Vocabulary.print_list(cin)
            word_list.append(cin)
            line = fh.readline()
            line = line.strip('\n')
        return word_list
            
    def print_list(self):
        print(self.__dict__)


word_list = Vocabulary.read_in(n)

