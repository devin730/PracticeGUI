#coding=utf-8

import wx
import FrameManager

class MainAPP(wx.App):
    def OnInit(self):
        self.manager = FrameManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(0)
        self.frame.Show()
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type)
        self.frame.Show(True)


if __name__ == '__main__':
    app = MainAPP()
    app.MainLoop()
