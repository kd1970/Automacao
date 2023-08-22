# ===================================================================================================
# ==      Tela Robo VTL                                                                            ==
# ===================================================================================================
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QSystemTrayIcon
from PySide6.QtGui import QIcon, QAction
from PySide6.QtUiTools import QUiLoader
from threading  import Thread
from PySide6.QtCore import QThread, Signal, QFile
from tqdm import tqdm
from playwright.sync_api import sync_playwright
import sys, os, logging, pathlib, time as t


logging.basicConfig(level=logging.INFO, filename="robo.log", format="Tipo : %(levelname)s - %(message)s" )

my_host = '127.0.0.1' # HostAdress FQDN is better
port = 8080

class BarThread(QThread):
    change_value = Signal(int)
    def run(self):
        cnt = 0
        while cnt < 100:
            cnt+=5
            t.sleep(0.8)
            self.change_value.emit(cnt)

class UiRobo(QMainWindow):

    def __init__(self):

        global recStatus
        recStatus = ''
        super(UiRobo, self).__init__()
        self.setWindowIcon(QIcon('pc.ico'))
        self.get_log()
        self.show()
        self.thread = {}
        
        #primeiro grupo de fitas - HSM Scratch
        self.BtnPrivt1.clicked.connect(lambda :self.automacao(self.BtnPrivt1.text()))
        self.BtnPrivt2.clicked.connect(lambda :self.automacao(self.BtnPrivt2.text()))
        self.BtnPrivt3.clicked.connect(lambda :self.automacao(self.BtnPrivt3.text()))
        self.BtnPrivt4.clicked.connect(lambda :self.automacao(self.BtnPrivt4.text()))
        self.BtnPrivt5.clicked.connect(lambda :self.automacao(self.BtnPrivt5.text()))
        self.BtnPrivt6.clicked.connect(lambda :self.automacao(self.BtnPrivt6.text()))
        self.BtnPrivt7.clicked.connect(lambda :self.automacao(self.BtnPrivt7.text()))
        self.BtnPrivt8.clicked.connect(lambda :self.automacao(self.BtnPrivt8.text()))
        self.BtnPrivt9.clicked.connect(lambda :self.automacao(self.BtnPrivt9.text()))

        #segundo grupo de fitas - MIGRATE
        self.BtnMig1.clicked.connect(lambda :self.automacao(self.BtnMig1.text()))
        self.BtnMig2.clicked.connect(lambda :self.automacao(self.BtnMig2.text()))
        self.BtnMig3.clicked.connect(lambda :self.automacao(self.BtnMig3.text()))
        self.BtnMig4.clicked.connect(lambda :self.automacao(self.BtnMig4.text()))
        self.BtnMig5.clicked.connect(lambda :self.automacao(self.BtnMig5.text()))
        self.BtnMig6.clicked.connect(lambda :self.automacao(self.BtnMig6.text()))
        self.BtnMig7.clicked.connect(lambda :self.automacao(self.BtnMig7.text()))
        self.BtnMig8.clicked.connect(lambda :self.automacao(self.BtnMig8.text()))
        self.BtnMig9.clicked.connect(lambda :self.automacao(self.BtnMig9.text()))

        #Treceiro grupo de fitas - PRIVAT - DASDS
        self.BtnDasd1.clicked.connect(lambda :self.automacao(self.BtnDasd1.text()))
        self.BtnDasd2.clicked.connect(lambda :self.automacao(self.BtnDasd2.text()))
        self.BtnDasd3.clicked.connect(lambda :self.automacao(self.BtnDasd3.text()))
        self.BtnDasd4.clicked.connect(lambda :self.automacao(self.BtnDasd4.text()))
        self.BtnDasd5.clicked.connect(lambda :self.automacao(self.BtnDasd5.text()))
        self.BtnDasd6.clicked.connect(lambda :self.automacao(self.BtnDasd6.text()))
        self.BtnDasd7.clicked.connect(lambda :self.automacao(self.BtnDasd7.text()))
        self.BtnDasd8.clicked.connect(lambda :self.automacao(self.BtnDasd8.text()))
        self.BtnDasd9.clicked.connect(lambda :self.automacao(self.BtnDasd9.text()))
    '''
    def load_ui(self):

        loader = QUiLoader()
        path = os.fspath(pathlib.Path(__file__).resolve().parent / "TS35.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
    '''
    def start(self, tape):
        logging.info(f'Iniciando a montagem da fita {tape}')
        self.get_log()
        try:
            with sync_playwright() as p:

                tape = tape
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(f'http://{my_host}:{port}/cgi-bin/tasks/syslog')
                t.sleep(1)
                #Herc command mount het tape file tape variable
                page.locator("body > form > input[type=text]:nth-child(1)").fill(
                    f'devinit 580 C:/Mainframe/Tape/HERCULES.{tape}.comp.het')
                t.sleep(1)
                page.locator('body > form > input[type=submit]:nth-child(2)').click()
                browser.close()
                self.get_log()

        except Exception as e:
                logging.error(f' na montagem da fita {tape}')
                self.get_log()
            

    def grava_log(self):
        with open('robo.log', 'r') as f:
            N = 13
            self.textBrowser.setText(f'{f.readlines()[-N:]}')
    
    def startProgressBar(self):
        self.thread = BarThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
    
    def automacao(self, tape):
        self.get_log()
        self.startProgressBar()
        self.clear_bar()
        self.TxtLCD.setText(f'Loading Tape : {tape}')
        self.tape = tape
        o = Thread(target = self.start(tape))
        o.start()
        
    def setProgressVal(self, val):
        self.progressBar.setValue(val)
        if self.progressBar.value() == 100:
            t.sleep(2)
            self.progressBar.setValue(0)

    def get_log(self):
        self.log = Thread(target = self.grava_log())
        self.log.start()

    def clear_bar(self):

        self.progressBar.setValue(0)


def LoadRobo():
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = UiRobo()
    window.show()

   # Create the icon
    icon = QIcon("pc.ico")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()
    action = QAction("Exibir")
    action.triggered.connect(lambda:window.showNormal())
    menu.addAction(action)

    # Add a Quit option to the menu.
    quit = QAction("Sair")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    app.exec()

LoadRobo()