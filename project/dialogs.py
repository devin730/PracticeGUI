#!/usr/bin/python
# coding: utf-8
#
# @module dialogs
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-17 14:02:00
# -------------------------------

import wx
import wx.adv


class IntroDialog(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(IntroDialog, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        help = wx.Menu()
        help.Append(wx.ID_ANY, '&About')
        help.Bind(wx.EVT_MENU, self.OnAboutBox)
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)
        self.SetSize((350, 250))
        self.SetTitle('About dialog box')
        self.Centre()

    def OnAboutBox(self, e):
        description = """"""

        licence = """"""

        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
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
    ex = IntroDialog(None)
    ex.Show()
    app.MainLoop()
