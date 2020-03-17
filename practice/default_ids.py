#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        exitButton = wx.Button(pnl, wx.ID_ANY, 'Exit', (10, 10))
        self.Bind(wx.EVT_BUTTON,  self.OnExit, id=exitButton.GetId())

        openButton = wx.Button(pnl, wx.ID_ANY, 'Open', (120, 10))
        self.Bind(wx.EVT_BUTTON,  self.Open, id=openButton.GetId())

        self.SetTitle("Automatic ids")
        self.Centre()

    def OnExit(self, event):
        self.Close()

    def Open(self, event):
        print("you are entering open button")


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()