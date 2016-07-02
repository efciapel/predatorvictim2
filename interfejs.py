#coding:utf8
import wx
from Environment import Environment
from Predator import Predator
from Victim import Victim
import matplotlib.pyplot as plt

class MyWindow(wx.Panel):
    E=Environment()
    Predators=[]
    def __init__(self, parent):
        self.panel=wx.Panel.__init__(self, parent)
        self.hg = wx.StaticText(self, label="Podaj wysokość środowiska: ", pos=(20, 30))
        self.wd = wx.StaticText(self, label="Podaj szerokość środowiska: ", pos=(20, 60))
        self.pr = wx.StaticText(self, label="Podaj liczbę drapieżników: ", pos=(20, 90))
        self.vc = wx.StaticText(self, label="Podaj liczbę ofiar: ", pos=(20, 120))
        self.tm = wx.StaticText(self, label="Podaj liczbę okresów: ", pos=(20, 150))

        self.ehg = wx.TextCtrl(self, value='', pos=(300, 30))
        self.ewd = wx.TextCtrl(self, value='', pos=(300, 60))
        self.epr = wx.TextCtrl(self, value='', pos=(300, 90))
        self.evc = wx.TextCtrl(self, value='', pos=(300, 120))
        self.etm = wx.TextCtrl(self, value='', pos=(300, 150))



        # A button
        self.button =wx.Button(self, label="OK", pos=(160, 225), style=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.values, self.button)


    def values(self, event):
        data_predator=[]
        data_victim=[]
        data_time=[]
        self.hight=int(self.ehg.GetValue())
        self.width=int(self.ewd.GetValue())
        self.predator=int(self.epr.GetValue())
        self.victim=int(self.evc.GetValue())
        self.time=int(self.etm.GetValue())

        self.E.set_size(self.width * 2, self.hight)

        if self.predator + self.victim > self.E.size:
            wx.MessageBox('Za dużo osobników, a za małe środowisko ', 'Info',
            wx.OK | wx.ICON_EXCLAMATION)

        else:
            self.E.envi_clear()
            for i in range(self.predator):
                Predator(self.E)

            for i in range(self.victim):
                Victim(self.E)

            self.E.observator()

            for i in range(self.time):

                data_time.append(i)
                data_victim.append(self.E.victims)
                data_predator.append(self.E.predators)
                for i in range(len(self.E.envi)):
                    # print "test1"
                    for j in range(len(self.E.envi[i])):
                        # print "test2"
                        if j % 2 == 0:
                            if self.E.envi[i][j]==2:
                                if self.E.envi[i][j+1] == 1:
                                    self.E.predators = self.E.predators + 1
                                    self.E.victims = self.E.victims - 1

                                elif self.E.envi[i][j+1] == 0:
                                    self.E.victims = self.E.victims + 1

                            elif self.E.envi[i][j]==1:
                                if self.E.envi[i][j+1] == 0:
                                    self.E.predators = self.E.predators - 1

                                elif self.E.envi[i][j+1]== 1:
                                    self.E.predators = self.E.predators - 2

                                elif self.E.envi[i][j+1] == 2:
                                    self.E.predators = self.E.predators + 1
                                    self.E.victims = self.E.victims - 1

                            elif self.E.envi[i][j]==0:
                                if self.E.envi[i][j+1] == 1:
                                    self.E.predators = self.E.predators - 1

                                elif self.E.envi[i][j+1] == 2:
                                    self.E.victims = self.E.victims + 1
                self.E.envi_clear()
                for i in range(self.E.predators):
                    Predator(self.E)
                for i in range(self.E.victims):
                    Victim(self.E)

            plt.plot(data_time, data_predator, data_time, data_victim)
            plt.xlabel('czas')
            plt.ylabel('liczba osobnikow')
            plt.title('Wykres')
            plt.legend()
            plt.show()


 #Rozpoczęcie nowej aplikacji
Prog = wx.App(0)

frame = wx.Frame(None, title=u'Drapieżnik - Ofiara', size=(400,300))
panel = MyWindow(frame)

frame.Show()
Prog.MainLoop()


