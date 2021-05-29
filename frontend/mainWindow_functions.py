from mainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys
sys.path.insert(1, '/home/janekkttme/Документы/FindIt/database')
import database_functions 
import urllib.request as ur



class MainWindow(QMainWindow):      
    '''
    def setMenu(self, sex, *args):
        for widget in range(self.ui.verticalLayout_2.count()):
            self.ui.verticalLayout_2.itemAt(widget).widget().deleteLater()
        if sex == 'women':
            # EDIT...............................................................
            categories = ['View All', 'Dress', 'T-shirts', 'Pants', 'Shorts', 'Shirts',
                          'Hoodies & Sweatshirts', 'Jeans', 'Jackets & Coats', 'Suits & Blazers',
                          'Shoes', 'Cardigans & Sweaters']
        elif sex == 'men':
            categories = ['View All', 'T-shirts', 'Pants', 'Shorts', 'Shirts',
                          'Hoodies & Sweatshirts', 'Jeans', 'Jackets & Coats', 'Suits & Blazers',
                          'Shoes', 'Cardigans & Sweaters']
        
        '''
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # MAIN WINDOW
        
        ## ITEM
        self.setView('', '')
        
        ## 'BACK' AND 'NEXT' BUTTONS
        self.ui.back.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()-1))
        
        self.ui.next.clicked.connect(lambda:
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()+1))
        
        
    def setView(self, sex, category, *args):
        items = []
        if sex == '':
            items = database_functions.Database.getAll()
        else:
            items = database_functions.Database.getBySexAndCategory(sex, category)
            
        for i in range(len(items)):
            self.ui.page = QtWidgets.QWidget()
            
            self.ui.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ui.page)
            self.ui.verticalLayout_2.setObjectName("verticalLayout_2")
            self.ui.scrollArea = QtWidgets.QScrollArea(self.ui.page)
            self.ui.scrollArea.setWidgetResizable(True)
            self.ui.scrollArea.setObjectName("scrollArea")
            self.ui.scrollArea.setVerticalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff)
            self.ui.scrollArea.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff)
            self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
            self.ui.scrollAreaWidgetContents = QtWidgets.QWidget()
            #self.ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 4420, 524))
            self.ui.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
            self.ui.item = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
            self.ui.item.setObjectName("item")
            
            url = items[i][2]    
            data = ur.urlopen(url).read()
            self.ui.pixmap = QPixmap()
            self.ui.pixmap.loadFromData(data)
            #self.ui.pixmap = self.ui.pixmap.scaledToWidth(310)
            #self.ui.pixmap = self.ui.pixmap.scaledToHeight(420)
            self.ui.image = QtWidgets.QLabel()
            self.ui.image.setObjectName(items[i][0])
            self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.image.setPixmap(self.ui.pixmap)
            self.ui.image.setFixedWidth(410)
            self.ui.image.setFixedHeight(460)
            self.ui.item.addWidget(self.ui.image)    
            
            self.ui.title = QtWidgets.QLabel()
            self.ui.title.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.title.setObjectName(str(items[i][0]))
            self.ui.title.setText(items[i][3])
            self.ui.title.setContentsMargins(0,10,0,10)    
            self.ui.item.addWidget(self.ui.title)   
            
            self.ui.analogsScrollArea = QtWidgets.QScrollArea()
            self.ui.analogsScrollArea.setMinimumSize(410, 350)
            self.ui.analogsScrollArea.setWidgetResizable(True)
            self.ui.analogsScrollArea.setObjectName("analogsScrollArea")
            self.ui.analogsScrollArea.setVerticalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff)
            self.ui.analogsScrollArea.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff)
            self.ui.analogsScrollArea.setFrameShape(QFrame.NoFrame)
            #self.ui.analogsScrollArea.resize(420, 310)
            self.ui.analogsAreaWidgetContents = QtWidgets.QWidget()
            #self.ui.analogsAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 420, 310))
            self.ui.analogsAreaWidgetContents.setObjectName("analogsAreaWidgetContents")
            self.ui.analogsScrollArea.setWidget(self.ui.analogsAreaWidgetContents)    
            self.ui.analogs = QtWidgets.QGridLayout(self.ui.analogsAreaWidgetContents)
            self.ui.analogs.setObjectName("analog") 
            
            for j in range(10):  
                #url = items[i][2]    
                #data = ur.urlopen(url).read()
                self.ui.pixmap = QPixmap()
                self.ui.pixmap.loadFromData(data)
                #self.ui.pixmap = self.ui.pixmap.scaledToWidth(220)
                #self.ui.pixmap = self.ui.pixmap.scaledToHeight(300)
                self.ui.analogImage = QtWidgets.QLabel()
                self.ui.analogImage.setObjectName(items[i][0])
                self.ui.analogImage.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.analogImage.setPixmap(self.ui.pixmap)
                self.ui.analogImage.setFixedWidth(180)
                self.ui.analogImage.setFixedHeight(260)
                self.ui.analogs.addWidget(self.ui.analogImage, 0, j)
                
                self.ui.analogTitle = QtWidgets.QLabel()
                self.ui.analogTitle.setObjectName(str(items[i][0]))
                self.ui.analogTitle.setText(items[i][3])
                self.ui.analogTitle.setContentsMargins(0,10,0,10)  
                
                self.ui.analogs.addWidget(self.ui.analogTitle, 1,  j) 
                
            self.ui.item.addWidget(self.ui.analogsScrollArea)
            
            
            
            self.ui.complementImageScrollArea = QtWidgets.QScrollArea()
            self.ui.complementImageScrollArea.setMinimumSize(410, 350)
            self.ui.complementImageScrollArea.setFrameShape(QFrame.NoFrame) #убирает рамку
            self.ui.complementImageScrollArea.setVerticalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff) #убирает видимость скролла
            self.ui.complementImageScrollArea.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff)
            self.ui.complementImageScrollArea.setWidgetResizable(True)
            self.ui.complementImageScrollArea.setObjectName("complementImageScrollArea")
            #self.ui.complementImageScrollArea.resize(420, 310)
            self.ui.complementImageWidgetContents = QtWidgets.QWidget()
            #self.ui.analogsAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 420, 310))
            self.ui.complementImageWidgetContents.setObjectName("complementImageWidgetContents")
            self.ui.complementImageScrollArea.setWidget(self.ui.complementImageWidgetContents)    
            self.ui.complement = QtWidgets.QGridLayout(self.ui.complementImageWidgetContents)
            self.ui.complement.setObjectName("complement")
            
            for j in range(10):             
                #url = items[i][2]    
                #data = ur.urlopen(url).read()
                self.ui.pixmap = QPixmap()
                self.ui.pixmap.loadFromData(data)
                #self.ui.pixmap = self.ui.pixmap.scaledToWidth(220)
                #self.ui.pixmap = self.ui.pixmap.scaledToHeight(300)
                self.ui.complementImage = QtWidgets.QLabel()
                self.ui.complementImage.setObjectName(items[i][0])
                self.ui.complementImage.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.complementImage.setPixmap(self.ui.pixmap)
                self.ui.complementImage.setFixedWidth(180)
                self.ui.complementImage.setFixedHeight(260)
                self.ui.complement.addWidget(self.ui.complementImage, 0, j)
                
                self.ui.complementImageTitle = QtWidgets.QLabel()
                self.ui.complementImageTitle.setObjectName(str(items[i][0]))
                self.ui.complementImageTitle.setText(items[i][3])
                self.ui.complementImageTitle.setContentsMargins(0,10,0,10)  
                
                self.ui.complement.addWidget(self.ui.complementImageTitle, 1,  j) 
                
            self.ui.item.addWidget(self.ui.complementImageScrollArea)
                 
                                
            self.ui.verticalLayout_2.addWidget(self.ui.scrollArea)
            self.ui.stackedWidget.addWidget(self.ui.page)  

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
