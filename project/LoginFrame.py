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
import LoginDialog


class LoginFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None,
                 title='登录页面', UpName=None, UpRecord=None):
        wx.Frame.__init__(self, parent, id, title)
        self.UpdateUI = UpdateUI
        self.InitUI()
        self.Centre()
        self.UpdateName = UpName
        self.UpdateRecord = UpRecord

    def InitUI(self):
        self.SetSize((750, 350))  # 设置窗口尺寸
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
        self.fontChinese = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False,
                                   'Microsoft yahei')
        self.fontChinese.SetPointSize(10)
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
        self.tc = wx.TextCtrl(panel)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='输入学号:')
        st2.SetFont(self.fontChinese)
        hbox2.Add(st2, flag=wx.RIGHT, border=10)
        self.tc2 = wx.TextCtrl(panel)
        hbox2.Add(self.tc2, proportion=1)
        vbox.Add(hbox2,
                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)

        vbox.Add((-1, 10))

        #! 增加两个按钮OK和Cancel
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='确定', size=(70, 30))
        btn2 = wx.Button(panel, label='取消', size=(70, 30))
        btn1.Bind(wx.EVT_BUTTON, self.Next)
        btn2.Bind(wx.EVT_BUTTON, self.Close)
        hbox3.Add(btn1)
        hbox3.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox3, flag=wx.RIGHT | wx.ALIGN_RIGHT, border=10)
        panel.SetSizer(vbox)

    def Next(self, e):
        # 到下一个页面
        #! 绑定文本框的输入
        self.userName = self.tc.GetValue()
        self.userID = self.tc2.GetValue()
        comfirm_dialogs = logindialog(func_cb=self.UpdateUI, uname=self.userName,
                                      uuid=self.userID, callback_name=self.UpdateName, callback_str=self.UpdateRecord)
        comfirm_dialogs.Show()

    def Close(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()

    def OnAboutBox(self, e):
        description = "Hala Madrid"
        licence = "测试代码：授权说明"
        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon('../images/rm.jpg', wx.BITMAP_TYPE_ANY))
        info.SetName('测试程序')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2020 - Forever, Devin')
        info.SetWebSite('http://www.dzm.me')
        info.SetLicence(licence)
        info.AddDeveloper('Deng Zengming')
        info.AddDocWriter('Deng Zengming')
        info.AddArtist('Deng Zengming')
        info.AddTranslator('Deng Zengming')
        wx.adv.AboutBox(info)

class logindialog(LoginDialog.DialogMSG):
    def __init__(self, func_cb, uname, uuid, callback_name, callback_str):
        LoginDialog.DialogMSG.__init__(self, parent=None, func_callback=func_cb,
                                       user_name=uname, uid=uuid,
                                       name_callback=callback_name,
                                       str_callback=callback_str)

if __name__ == '__main__':
    app = wx.App()
    ex = LoginFrame(None, title='test programme')
    ex.Show()
    app.MainLoop()
