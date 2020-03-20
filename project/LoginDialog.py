#!/usr/bin/python
# coding: utf-8
#
# @module dia
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-18 11:02:41
# -------------------------------

import wx

class DialogMSG(wx.Frame):
    def __init__(self, parent=None, func_callback=None, user_name='default',
                 uid='0', name_callback=None, str_callback=None):
        super(DialogMSG, self).__init__(parent)
        self.SetNameID(user_name, uid)
        self.UpdateUI = func_callback
        self.InitUI()
        self.SetSize((500, 180))
        self.SetTitle('确认输入信息')
        self.Centre()
        self.UpdateName = name_callback
        self.UpdateStr = str_callback

    def SetNameID(self, username='default name', u_id='0'):
        self.user_name = username
        self.user_id = u_id

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        text_user_info_name = "您输入的姓名是 " + self.user_name
        text_user_info_id = "您输入的ID是 " + self.user_id
        text_guide = "如果正确请点击确定，如果错误请点击取消，可返回上一级修改。"
        stext_name = wx.StaticText(panel, label=text_user_info_name)
        stext_id = wx.StaticText(panel, label=text_user_info_id)
        stext_guide = wx.StaticText(panel, label=text_guide)
        vbox.Add(stext_name, flag=wx.RIGHT, border=10)
        vbox.Add((-1, 10))
        vbox.Add(stext_id, flag=wx.RIGHT, border=10)
        vbox.Add((-1, 10))
        vbox.Add(stext_guide, flag=wx.RIGHT, border=10)
        vbox.Add((-1, 10))
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
        self.UpdateName(usname=self.user_name)
        self.UpdateStr(type=0, ustr=self.user_id)
        self.UpdateUI(1)
        self.Destroy()
        return 100

    def Close(self, e):
        dial = wx.MessageDialog(None, '返回上一级修改?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()

if __name__ == '__main__':
    app = wx.App()
    ex = DialogMSG(None, user_name='Devin', uid='2026')
    ex.Show()
    app.MainLoop()
