#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class Exam(wx.Frame):
    def __init__(self, parent, title):
        super(Exam, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        self.SetSize((300, 200))
        self.CreatMenu()

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 2, 9, 20)
        title = wx.StaticText(panel,  label="学号：")
        author = wx.StaticText(panel, label="姓名：")
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author), (tc2, 1, wx.EXPAND)])
        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def CreatMenu(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Exam(None, "考试")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
