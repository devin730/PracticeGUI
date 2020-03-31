#!/usr/bin/python
# coding: utf-8
#
# @module FinalPage
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-23 11:40:27
# -------------------------------

import wx

class FinalPage(wx.Frame):

    def __init__(self, Record=['', 'A', 'B'], Standard_Ans=['A', 'B']):
        super(FinalPage, self).__init__(None)
        print('1')
        self.GenerateResult(rec=Record, ans=Standard_Ans)
        print('2')
        self.InitUI()
        print('3')
    
    def GenerateResult(self, rec, ans):
        num = len(ans)
        cnt = 0
        for i in range(num):
            if rec[i+1] == ans[i]:
                cnt = cnt + 1
        score = int(cnt/num) * 100
        self.Result_Text = '你得到了'+str(score)+'分'

    def InitUI(self):
        pnl = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)
        static_text = wx.StaticText(pnl, label=str(self.Result_Text))
        sizer.Add(static_text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        btn = wx.Button(pnl, label='确定', size=(70, 30))
        btn.Bind(wx.EVT_BUTTON, self.Close)
        sizer.Add(btn, pos=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        pnl.SetSizer(sizer)
        self.SetSize((300, 200))
        self.SetTitle('测试结果')
        self.Centre()
    
    def Close(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()

if __name__ == '__main__':
    app = wx.App()
    f = FinalPage(Record=['', 'B', 'C'], Standard_Ans=['B', 'C'])
    f.Show()
    app.MainLoop()
