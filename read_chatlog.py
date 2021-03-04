import re
file_path = 'file.txt'
pureTxt = []
def judge_start_line(message):

        """
        判断某行是不是起始行
        条件1:YYYY-MM-DD HH-MM-SS开头(长度大于19)
        条件2::(XXXXXXXXX)或者<xxx@xxx.xxx>结尾
        :return: False or (time,ID)
        """
        if len(message) > 19 and (self.time_pattern.match(message)) and (self.ID_pattern.search(message)):
            return self.time_pattern.search(message).group(), self.ID_pattern.search(message).group()
        return False

def removeAt(ss):
    temp = ss.split(' ')
    temp2 = []
    str = " "
    for i in (temp):
        if '@' not in i:
            temp2.append(i)

    for i in temp2:
        str = str + i
        str = str + ' '

    return str


def work(file_path):
    """
    腾讯导出的聊天记录是UTF-8+bom的 手动改成-bom
    进行数据清洗,将原始数据划分成块保存进mongodb中
    ..note::例子
        time:YYYY-MM-DD HH-MM-SS
        ID:(XXXXXXXXX)或者<xxx@xxx.xxx>
        name:username
        text:['sentence1','sentence2',...]
        """
    print('----------正在进行数据清洗-------------')

    with open(file_path, 'r', encoding='utf-8') as chatlog_file:
        chatlog_list = [line.strip() for line in chatlog_file if line.strip() != ""]

    for i,n in enumerate(chatlog_list):
        if(not n[0].isnumeric()):
            pureTxt.append(n)

    temp = []

    for i in pureTxt:
        temp.append(removeAt(i))


    f = open('chatlog.txt', 'w', encoding='utf-8')
    for i in temp:
        f.writelines("\n")
        f.writelines(i)
