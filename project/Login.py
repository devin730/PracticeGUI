#!/usr/bin/python
# coding: utf-8
#
# @module Login
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-17 17:38:11
# -------------------------------

import wx
import wx.adv


class programme(wx.Frame):
    def __init__(self, parent, title):
        super(programme, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.SetSize((750, 350))  # 设置窗口尺寸
        self.SetTitle('Welcome')
        self.InitMenubar()
        self.InitPanel()

    def InitMenubar(self):
        menubar = wx.MenuBar()
        help = wx.Menu()
        help.Append(wx.ID_ANY, '&About')
        help.Bind(wx.EVT_MENU, self.OnAboutBox)
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

    def InitPanel(self):
        panel = wx.Panel(self)
        # 设置字体
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        vbox = wx.BoxSizer(wx.VERTICAL)
        #! 一个垂直方向的vbox 起始点

        #*写一下登录界面的文本
        self.fontChinese = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft yahei')
        self.fontChinese.SetPointSize(15)
        hboxAD = wx.BoxSizer(wx.HORIZONTAL)
        ADwords = wx.StaticText(panel, label='这是一个用于XXX的登录页面，请在下方方框内输入信息！')
        ADwords.SetFont(self.fontChinese)
        hboxAD.Add(ADwords, flag=wx.RIGHT, border=10)
        vbox.Add(hboxAD,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)
        vbox.Add((-1, 10))
        #*

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='输入姓名:')
        st1.SetFont(self.fontChinese)
        hbox1.Add(st1, flag=wx.RIGHT, border=10)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='输入学号:')
        st2.SetFont(self.fontChinese)
        hbox2.Add(st2, flag=wx.RIGHT, border=10)
        tc2 = wx.TextCtrl(panel)
        hbox2.Add(tc2, proportion=1)
        vbox.Add(hbox2,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)

        vbox.Add((-1, 10))
        panel.SetSizer(vbox)

    def OnAboutBox(self, e):
        description = "Hala Madrid"
        licence = "测试代码：授权说明"
        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon('../images/rm.jpg', wx.BITMAP_TYPE_ANY))
        info.SetName('File Hunter')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2007 - 2018 Jan Bodnar')
        info.SetWebSite('http://www.zetcode.com')
        info.SetLicence(licence)
        info.AddDeveloper('Jan Bodnar')
        info.AddDocWriter('Jan Bodnar')
        info.AddArtist('The Tango crew')
        info.AddTranslator('Jan Bodnar')
        wx.adv.AboutBox(info)

if __name__ == '__main__':
    app = wx.App()
    ex = programme(None, title='test programme')
    ex.Show()
    app.MainLoop()
