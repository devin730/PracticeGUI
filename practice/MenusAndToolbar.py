#!/usr/bin/python
# coding: utf-8
#
# @module MenusAndToolbar
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-04 14:30:07
# -------------------------------

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fileItem2 = fileMenu.Append(wx.ID_FIND, 'Find', 'Find something')
        menubar.Append(fileMenu, '&文件')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem2)
        self.SetSize((500, 500))
        self.SetTitle('一个简单的小程序')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
