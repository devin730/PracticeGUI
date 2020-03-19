#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        pnl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        pnl.Bind(wx.EVT_KEY_UP, self.PrintChar)
        pnl.SetFocus()

        self.SetSize((350, 250))
        self.SetTitle('Key event')
        self.Centre()

    def PrintChar(self, e):
        print('c')

    def OnKeyDown(self, e):
        key = e.GetKeyCode()
        print(key)
        if key == wx.WXK_ESCAPE:

            ret = wx.MessageBox('Are you sure to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT, self)

            if ret == wx.YES:
                self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()