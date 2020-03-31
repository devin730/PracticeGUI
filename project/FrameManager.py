#coding=utf-8
import LoginFrame
import ContentFrame
from ParentQFrame import ParentQFrame
import FinalPage


class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI
        self.frameDict = {}  # 用来装载已经创建的Frame对象
        self.RecordList = ['0' for i in range(10)]
        self.RecordName = ""

    def GetFrame(self, type):
        frame = self.frameDict.get(type)
        if frame is None:
            frame = self.CreateFrame(type)
            self.frameDict[type] = frame
        return frame

    def CreateFrame(self, type):
        print("Name: " + self.RecordName)
        print(self.RecordList)
        if type == 0:
            return LoginFrame.LoginFrame(parent=None, id=type, UpdateUI=self.UpdateUI,
                                         UpName=self.UpdateName, UpRecord=self.UpdateRecord)
        elif type == 1:
            return self.Question_1(id=type)

        elif type == 2:
            return self.Question_2(id=type)

        elif type == 3:
            return self.FinalFrame()

    def UpdateName(self, usname):
        self.RecordName = usname

    def UpdateRecord(self, type, ustr):
        self.RecordList[type] = ustr

    def Question_1(self, id):
        text_question = '我的生日'
        AnswerA = '1989/07/30'
        AnswerB = '1989/07/31'
        AnswerC = '1988/07/30'
        AnswerD = '1988/07/31'
        return ParentQFrame(question=text_question, label1=AnswerA,
                            label2=AnswerB, label3=AnswerC, label4=AnswerD,
                            UpdateUI=self.UpdateUI, PageID=id, UpdateRecord=self.UpdateRecord)

    def Question_2(self, id):
        text_question = '我的故乡'
        AnswerA = '长沙'
        AnswerB = '株洲'
        AnswerC = '哈尔滨'
        AnswerD = '许昌'
        return ParentQFrame(question=text_question, label1=AnswerA,
                            label2=AnswerB, label3=AnswerC, label4=AnswerD,
                            UpdateUI=self.UpdateUI, PageID=id, UpdateRecord=self.UpdateRecord)
    
    def FinalFrame(self):
        print('final page 姓名', self.RecordName)
        print('final page 最终记录 ', self.RecordList)
        return FinalPage.FinalPage(Record=self.RecordList, Standard_Ans=['C', 'B'])
