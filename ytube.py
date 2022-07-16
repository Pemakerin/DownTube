import wx
import os
import pytube
import wx.lib.agw.genericmessagedialog as GMD

class StartFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None,title='Download YouTube',style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
        panel = wx.Panel(self)
        
        self.text1 = wx.StaticText(panel, label='Link', pos=(3,10))
        self.text2 = wx.StaticText(panel, label='Selecione Qualidade', pos=(3,50))
        self.text3 = wx.StaticText(panel, label='Salve Vídeo', pos=(3, 159))
        self.text4 = wx.StaticText(panel, label='Inciar', pos=(3,299))
        self.f = 0 
        self.my_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.tc = wx.TextCtrl(panel, wx.ID_ANY, "Adicioner o Link", pos=(38,5), size=(350,30))
        self.ListOpcao = wx.CheckListBox(panel, id=wx.ID_ANY, pos=(-1,79), size=(389,96), choices=['360p', '720p', '1080p', 'MP3 Player'], style=0)

        self.my_sizer.Add(self.ListOpcao, 0, wx.ALL | wx.EXPAND, 5)
        self.my_sizer.Add(self.tc, 0, wx.ALL | wx.EXPAND, 5)

        self.tc_ = wx.TextCtrl(panel, pos=(-1,189), size=(395,30))
        self.tc_.AppendText(os.getcwd())

        self.btn = wx.Button(panel, label='Arquivo', pos=(150,229))
        self.btn.Bind(wx.EVT_BUTTON, self.dirlog)

        self.my_sizer.Add(self.tc_, 0, wx.ALL | wx.EXPAND, 5)
        self.my_sizer.Add(self.btn, 0, wx.ALL | wx.EXPAND, 5)

        self.text = wx.StaticText(panel, label='Fazer Download', pos=(1, 399))
        self.btn_ = wx.Button(panel, label='Download', pos=(49, 289))

        self.btn_.Bind(wx.EVT_BUTTON, self.Upload)

        self.my_sizer.Add(self.btn_, 0, wx.ALL | wx.EXPAND, 5)

        self.menubar = wx.MenuBar()
        self.finame = wx.Menu()

        self.finame.Append(wx.ID_ABOUT, '&Sair', 'Sair do progrma')
        self.menubar.Append(self.finame, '&File')
        
        self.menubar.Bind(wx.EVT_MENU, self.Menu_Exit)

        self.SetMenuBar(self.menubar)
        
        self.ico = wx.Icon('/opt/downtube/img_1.png', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.ico)



        self.Centre()
        self.Show()

    def Menu_Exit(self, event):
        exit_ = wx.MessageDialog(None, 'Você desejar sair ?', 'Pergunta', wx.YES_NO)
        if exit_.ShowModal() == wx.ID_YES:
            self.Close(True)
        exit_.Destroy()

    def dirlog(self,event):           
        self.dlg_ = wx.DirDialog(self,message='Choose a folder')
        if self.dlg_.ShowModal() == wx.ID_OK:
            self.dirname = self.dlg_.GetPath()
            
            self.tc_.Clear()
            self.tc_.AppendText(self.dirname)
            
        self.dlg_.Destroy()

    def Upload(self, event):
        self.lists_ = str(self.ListOpcao.GetCheckedItems())
        if isinstance(self.lists_, str):
            self.s = self.lists_.replace(',', '').replace('(','')
            self.f = self.s.replace(')', '').split()
            lItems = self.f
            _url = self.tc.Value
            
            def ShowMessage():
                
                wx.MessageBox('Download feito com sucesso', 'Info', wx.OK | wx.ICON_INFORMATION)
            
            if str(_url[:-11]) != "https://www.youtube.com/watch?v=":
                error_link = 'Desculpe esse Link não existe no YouTube !'
                dlg = GMD.GenericMessageDialog(None, error_link, 'Error link', agwStyle=wx.ICON_INFORMATION | wx.OK)
                
                dlg.ShowModal()
                dlg.Destroy()
                
            elif len(lItems) == 0:
                main_message = 'Voce não escolher nenhum QUALIDADE !'
                dlg = GMD.GenericMessageDialog(None, main_message, 'Escolha de Qualidade', agwStyle=wx.ICON_INFORMATION | wx.OK)
                
                dlg.ShowModal()
                dlg.Destroy()
            else:
                
                if len(lItems) == int(1):
                    if lItems[0] == str('0'):
                        
                        url = _url
                        
                        video = pytube.YouTube(url)
                        video.streams.get_by_itag(18).download(self.tc_.Value)

                        print('Download Completed')
                        ShowMessage()
                    elif lItems[0] == str('1'):
                        url = _url
                        video = pytube.YouTube(url)
                        try:
                            video.streams.get_by_itag(22).download(self.tc_.Value)
                            print('Download Completed')
                            ShowMessage()
                        except AttributeError:
                            video = None
                            video = pytube.YouTube(url)
                            video.streams.get_highest_resolution().download(self.tc_.Value)
                            print('Downlaod Completed')
                            ShowMessage()
                            
                    elif lItems[0] == str('2'):
                        url = _url
                        video = pytube.YouTube(url)
                        try:
                            video.streams.get_by_itag(137).download(self.tc_.Value)
                            print('Download Completed')
                            ShowMessage()
                        except AttributeError:
                            video = None
                            video = pytube.YouTube(url)
                            video.streams.get_highest_resolution().download(self.tc_.Value)
                            print('Downlaod Completed')
                            ShowMessage()
                    
                    elif lItems[0] == str('3'):
                        yt = pytube.YouTube(_url)
                        vd = yt.streams.filter(only_audio=True).first()
                        out_file = vd.download(self.tc_.Value)
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)
                        print('Download Completed')
                        ShowMessage()
                else:
                    if len(lItems) == 2 or len(lItems) == 3:
                        main_message = 'Por favor, escolhar apernas uma QUALIDADE !!!'
                        dlg = GMD.GenericMessageDialog(None, main_message, 'A Nice Message Box', agwStyle=wx.ICON_INFORMATION | wx.OK)

                        dlg.ShowModal()
                        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    StartFrame()
    app.MainLoop()
