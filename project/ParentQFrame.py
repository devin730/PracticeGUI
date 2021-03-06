#!/usr/bin/python
# coding: utf-8
#
# @module ParentQFrame
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-20 15:06:50
# -------------------------------

import wx

class ParentQFrame(wx.Frame):
    def __init__(self, question='问题问题', label1='选项A', label2='选项B', label3='选项C', label4='选项D', UpdateUI=None, PageID=0, UpdateRecord=None):
        super(ParentQFrame, self).__init__(None)
        self.strlabel1 = label1
        self.strlabel2 = label2
        self.strlabel3 = label3
        self.strlabel4 = label4
        self.QuestionText = question
        self.UpdateUI = UpdateUI
        self.PageID = PageID
        self.UpdateStr = UpdateRecord  # (type=0, ustr=self.user_id)
        self.InitUI()

    # def EditRadioButtonLabel(self, id, input):
    #     if id == 1:
    #         self.strlabel1 = input
    #     elif id == 2:
    #         self.strlabel2 = input
    #     elif id == 3:
    #         self.strlabel3 = input
    #     elif id == 4:
    #         self.strlabel4 = input
    #     else:
    #         print("id is wrong.")
    
    # def InputQuestion(self, st):
    #     self.QuestionText = st

    def InitUI(self):
        pnl = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)
        
        static_text = wx.StaticText(pnl, label=str(self.QuestionText))
        sizer.Add(static_text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.rb1 = wx.RadioButton(pnl, label=str(self.strlabel1), pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, label=str(self.strlabel2), pos=(10, 30))
        self.rb3 = wx.RadioButton(pnl, label=str(self.strlabel3), pos=(10, 50))
        self.rb4 = wx.RadioButton(pnl, label=str(self.strlabel4), pos=(10, 70))
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb4.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

        sizer.Add(self.rb1, pos=(1, 1), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        sizer.Add(self.rb2, pos=(2, 1), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        sizer.Add(self.rb3, pos=(3, 1), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        sizer.Add(self.rb4, pos=(4, 1), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(pnl, label='上一步', size=(70, 30))
        btn2 = wx.Button(pnl, label='下一步', size=(70, 30))
        btn1.Bind(wx.EVT_BUTTON, self.Previous)
        btn2.Bind(wx.EVT_BUTTON, self.Next)
        hbox3.Add(btn1)
        hbox3.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(hbox3, pos=(5, 2), flag=wx.RIGHT | wx.BOTTOM, border=10)

        pnl.SetSizer(sizer)

        self.SetSize((300, 210))
        title_text = '第' + str(self.PageID) + '道题'
        self.SetTitle(title_text)
        self.Centre()
        # self.Show(True)

    def SetVal(self, e):
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())
        state4 = str(self.rb4.GetValue())
        if state1 == 'True':
            self.Choice = 'A'
        elif state2 == 'True':
            self.Choice = 'B'
        elif state3 == 'True':
            self.Choice = 'C'
        else:
            self.Choice = 'D'
        print(state1, state2, state3, state4)
        print('you choose', self.Choice)
        
    def Next(self, e):
        # 到下一个页面
        print('前往下一页, 第', self.PageID, '页的结果是', self.Choice)
        self.UpdateStr(type=self.PageID, ustr=self.Choice)
        self.UpdateUI(self.PageID+1)
        self.Destroy()

    def Previous(self, e):
        dial = wx.MessageDialog(None, '返回上一级修改?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            print('返回上一页')
            self.UpdateUI(self.PageID-1)
            self.Destroy()
        else:
            e.Veto()

if __name__ == '__main__':
    ex = wx.App()
    f = ParentQFrame()
    f.Show()
    ex.MainLoop()
