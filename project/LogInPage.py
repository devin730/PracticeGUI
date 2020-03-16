#!/usr/bin/python
# coding: utf-8
#
# @module LogPage
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-16 11:24:43
# -------------------------------

import wx


class LogInPage(wx.Frame):
    def __init__(self, parent, title):
        super(LogInPage, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)

        # 设置字体
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)  
        #! 一个垂直方向的vbox 起始点
        
        #*写一下登录界面的文本
        fontChinese = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)    
        fontChinese.SetPointSize(15)
        hboxAD = wx.BoxSizer(wx.HORIZONTAL)
        ADwords = wx.StaticText(panel, label='这是一个用于XXX的登录页面，请在下方方框内输入信息！')
        ADwords.SetFont(fontChinese)
        hboxAD.Add(ADwords, flag=wx.RIGHT, border=10)
        vbox.Add(hboxAD,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)
        vbox.Add((-1, 10))
        #*

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='输入姓名:')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=10)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='输入学号:')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.RIGHT, border=10)
        tc2 = wx.TextCtrl(panel)
        hbox2.Add(tc2, proportion=1)
        vbox.Add(hbox2, 
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 
                 border=10)

        vbox.Add((-1, 10))

        # hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # tc2 = wx.TextCtrl(panel, style=wx.TE_LEFT)
        # hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        # vbox.Add(hbox3,
        #          proportion=1,
        #          flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
        #          border=10)

        # vbox.Add((-1, 25))

        # hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        # cb1 = wx.CheckBox(panel, label='Case Sensitive')
        # cb1.SetFont(font)
        # hbox4.Add(cb1)
        # cb2 = wx.CheckBox(panel, label='Nested Classes')
        # cb2.SetFont(font)
        # hbox4.Add(cb2, flag=wx.LEFT, border=10)
        # cb3 = wx.CheckBox(panel, label='Non-Project classes')
        # cb3.SetFont(font)
        # hbox4.Add(cb3, flag=wx.LEFT, border=10)
        # vbox.Add(hbox4, flag=wx.LEFT, border=10)
        # vbox.Add((-1, 25))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox3.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox3.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox3, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        #! 一个垂直方向的vbox 终点

        panel.SetSizer(vbox)


if __name__ == '__main__':
    app = wx.App()
    ex = LogInPage(None, title='登录页面测试')
    ex.Show()
    app.MainLoop()
