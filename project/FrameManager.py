#coding=utf-8
import LoginFrame
import ContentFrame


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
            return ContentFrame.ContentFrame(parent=None, id=type, UpdateUI=self.UpdateUI)

    def UpdateName(self, usname):
        self.RecordName = usname

    def UpdateRecord(self, type, ustr):
        self.RecordList[type] = ustr
