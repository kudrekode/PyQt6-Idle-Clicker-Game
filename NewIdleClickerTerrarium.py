#terrarium idle clicker:

#modules:
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QMessageBox, QMainWindow, QSizePolicy
import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
import numpy as np
import os
os.environ["QT_USE_PHYSICAL_DPI"] = "1" #ensure high rez compatibility

#Import UI Components from QT Designer .ui/.py files saved
from gamepage import Ui_MainWindow  
print("import succesful")
from homepage import Ui_MainWindow 
print("import succesful")
from PyQt6.uic import loadUi

#Home Page UI Initialisation:
class HomePageMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\pyqt6\pyqt6-env\Scripts\HomePage.ui", self) #Loads the .ui file from QT Designer
        self.setStyleSheet("background-color: white;")  


#Main Window Class that swiches HomePage and GamePage:
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Stacked widget to switch pages on:
        self.stack = QStackedWidget()  
        self.home_page = HomePageMainWindow()
        self.game_page = GamePage()
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.game_page)

        #Sets first page:
        self.stack.setCurrentWidget(self.home_page) 

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        #Opens New Page(GamePage):
        self.home_page.pushButton.clicked.connect(self.open_new_page) 

        #Ensures size policy and Full Screen mode:
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.showMaximized()

    #Open New Page Function:
    def open_new_page(self):
        self.stack.setCurrentWidget(self.game_page)


#Game Page Window: 
class GamePage(QMainWindow):
    def __init__(self):
        super().__init__()
        #Sets current game level to 1 which is later used to update game images according to level
        self.current_level = 1
        self.setup_ui()
        self.setStyleSheet("background-color: white;")  
        #Function that displays current game level iamge.
        self.load_and_display_image()

    def load_and_display_image(self):
        image_path = self.get_image_path_for_level(self.current_level)
        pixmap = QPixmap(image_path)
        
        #Debugs:
        if not pixmap.isNull():
            print("Image correctly loaded")
            self.image_label.setPixmap(pixmap)
        else:
            print("Image failed to load")
    
    #Unlocks new level and calls the displaying of new image for level.
    def unlock_new_level(self):
        self.current_level += 1
        self.load_and_display_image()

    #For each level will find the correct Image for level since only difference in file is last appended number:
    def get_image_path_for_level(self, level):
        base_path = r"C:\Users\jadcr\Desktop\Terrarium Background\\"
        image_path = base_path + str(level) + ".png"
        return image_path

    #For the Back Button:
    def open_new_page(self):
        self.stack.setCurrentWidget(self.game_page)

    #Loading the .ui file from the QT designer for Game Page:
    def setup_ui(self):
        loadUi("C:\pyqt6\pyqt6-env\Scripts\GamePage.ui", self)

        #Connecting all the buttons in QT Designer to code:
        self.back_button.clicked.connect(self.go_to_home_page)
        self.findChild(QPushButton, "seedling_button").clicked.connect(self.seedling_eco)
        self.findChild(QPushButton, "sprout_button").clicked.connect(self.sprout_eco)
        self.findChild(QPushButton, "leafy_button").clicked.connect(self.leafy_eco)
        self.findChild(QPushButton, "root_button").clicked.connect(self.root_eco)
        self.findChild(QPushButton, "ecosystem_button").clicked.connect(self.ecosystem_eco)
        self.findChild(QPushButton, "moss_button").clicked.connect(self.moss_eco)
        self.findChild(QPushButton, "waterfall_button").clicked.connect(self.waterfall_eco)
        self.findChild(QPushButton, "fauna_button").clicked.connect(self.fauna_eco)
        self.findChild(QPushButton, "blooming_button").clicked.connect(self.blooming_eco)
        self.findChild(QPushButton, "photo_button").clicked.connect(self.photo_eco)
        self.findChild(QPushButton, "bonsai_button").clicked.connect(self.bonsai_eco)
        self.findChild(QPushButton, "insect_button").clicked.connect(self.insect_eco)
        self.findChild(QPushButton, "decor_button").clicked.connect(self.decor_eco)
        self.findChild(QPushButton, "orchids_button").clicked.connect(self.orchids_eco)
        self.findChild(QPushButton, "geode_button").clicked.connect(self.geode_eco)
        self.findChild(QPushButton, "time_button").clicked.connect(self.time_eco)
        self.findChild(QPushButton, "cosmic_button").clicked.connect(self.cosmic_eco)
        self.findChild(QPushButton, "fossils_button").clicked.connect(self.fossils_eco)
        self.findChild(QPushButton, "eternal_button").clicked.connect(self.eternal_eco)

        #Initialising Game Totals:
        self.seedling_total = 0
        self.sprout_total = 0
        self.leafy_total =0
        self.root_total = 0
        self.ecosystem_total = 0
        self.moss_total = 0
        self.waterfall_total = 0
        self.fauna_total = 0
        self.blooming_total = 0
        self.photo_total = 0
        self.bonsai_total = 0
        self.pond_total = 0
        self.insect_total = 0
        self.decor_total = 0
        self.orchids_total = 0
        self.geode_total = 0
        self.time_total = 0
        self.cosmic_total = 0
        self.fossils_total = 0
        self.eternal_total = 0

        # Output for Not Enough Money (needs to be hidden unless envoked):
        self.error_label = QLabel()

        #Initialising Boolean Triggers (later used to ensure right image is shown):
        self.sprout_bool = 0
        self.leafy_bool = 0
        self.root_bool = 0
        self.ecosystem_bool = 0
        self.moss_bool = 0
        self.water_bool = 0
        self.fauna_bool = 0
        self.blooming_bool = 0
        self.photo_bool = 0
        self.bonsai_bool = 0
        self.pond_bool = 0
        self.insect_bool = 0
        self.decor_bool = 0
        self.orchids_bool = 0
        self.geode_bool = 0
        self.time_bool = 0
        self.cosmic_bool = 0
        self.fossils_bool = 0
        self.eternal_bool = 0

    #Function for hiding labels:
    def hide_error_label(self):
        self.error_label.hide()  

    def go_to_home_page(self):
        # Get the parent widget (MainWindow) and switch to the home page
        parent = self.parentWidget().parentWidget()
        parent.stack.setCurrentWidget(parent.home_page)
       
    #Logic For ALL Buttons:
        
    def seedling_eco(self):
        seedling_label = self.findChild(QLabel, "seedling_label")
        self.seedling_total += 1
        seedling_label.setText(f"{self.seedling_total:.6g}")
        #Set to :.6g to ensure no overload of numbers in GUI. 
        
    def sprout_eco (self):
        sprout_label = self.findChild(QLabel, "sprout_label")
        #Causes error message to arise if not enough money for next level:
        if self.seedling_total < 10:
            QMessageBox.critical(self,"Error", f"You need {10 - self.seedling_total} more Seedlings to buy this")
        else:
            self.seedling_total -= 10
            self.seedling_label.setText(f"{self.seedling_total:.6g}")
            self.sprout_total += 1
            self.sprout_label.setText(f"{self.sprout_total:.6g}")

            #Increases amount of previous level item every timer interval:
            self.seedling_timer = QTimer(self)
            self.seedling_timer.timeout.connect(self.increment_seedlings)
            self.seedling_timer.start(5000)

            #Ensures new level image is unlocked ONLY once:
            if self.sprout_bool == 0:
                self.unlock_new_level()
                self.sprout_bool =1
            else:
                pass
            
    #Function to increase Prior Modules when future purchased
    def increment_seedlings(self):
        seedling_label = self.findChild(QLabel, "seedling_label")
        self.seedling_total += 1
        self.seedling_label.setText(f"{self.seedling_total:.6g}")

    def leafy_eco (self):
        leafy_label = self.findChild(QLabel, "leafy_label")

        if self.sprout_total < 10: 
            QMessageBox.critical(self,"Error", f"You need {10 - self.sprout_total} more Sprout Growths to buy this")
        else:
            self.sprout_total -= 10
            self.sprout_label.setText(f"{self.sprout_total:.6g}")
            self.leafy_total += 1
            self.leafy_label.setText(f"{self.leafy_total:.6g}")

            self.sprout_timer = QTimer(self)
            self.sprout_timer.timeout.connect(self.increment_sprout)
            self.sprout_timer.start(10000)

            if self.leafy_bool  == 0:
                self.unlock_new_level()
                self.leafy_bool  =1
            else:
                pass

    def increment_sprout(self):
        sprout_label = self.findChild(QLabel, "sprout_label")

        self.sprout_total += 1
        self.sprout_label.setText(f"{self.sprout_total:.6g}")

    def root_eco(self):
        root_label = self.findChild(QLabel, "root_label")

        if self.leafy_total < 10: 
            QMessageBox.critical(self,"Error", f"You need {10 - self.leafy_total} more Leafy Greens to buy this")
        else:
            self.leafy_total -= 10
            self.leafy_label.setText(f"{self.leafy_total:.6g}")
            self.root_total += 1
            self.root_label.setText(f"{self.root_total:.6g}")

            self.leafy_timer = QTimer(self)
            self.leafy_timer.timeout.connect(self.increment_leafy)
            self.leafy_timer.start(10000)   

            if self.root_bool  == 0:
                self.unlock_new_level()
                self.root_bool  =1
            else:
                pass

    def increment_leafy(self):
        leafy_label = self.findChild(QLabel, "leafy_label")

        self.leafy_total += 1
        self.leafy_label.setText(f"{self.leafy_total:.6g}")  

    def ecosystem_eco(self):
        ecosystem_label = self.findChild(QLabel, "ecosystem_label")

        if self.root_total < 10: 
            QMessageBox.critical(self, "Error", f"You need {10 - self.root_total} more Root Networks to buy this")
        else:
            self.root_total -= 10
            self.root_label.setText(f"{self.root_total:.6g}")
            self.ecosystem_total += 1
            self.ecosystem_label.setText(f"{self.ecosystem_total:.6g}")

            self.root_timer = QTimer(self)
            self.root_timer.timeout.connect(self.increment_root)
            self.root_timer.start(10000)

            if self.ecosystem_bool   == 0:
                self.unlock_new_level()
                self.ecosystem_bool   =1
            else:
                pass

    def increment_root(self):
        root_label = self.findChild(QLabel, "root_label")

        self.root_total += 1
        self.root_label.setText(f"{self.root_total:.6g}")

    def moss_eco(self):
        moss_label = self.findChild(QLabel, "moss_label")

        if self.ecosystem_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.ecosystem_total} more Ecosystem's to grow this")
        else:
            self.ecosystem_total -= 10
            self.ecosystem_label.setText(f"{self.ecosystem_total:.6g}")
            self.moss_total += 1
            self.moss_label.setText(f"{self.moss_total:.6g}")

            self.ecosystem_timer = QTimer(self)
            self.ecosystem_timer.timeout.connect(self.increment_ecosystem)
            self.ecosystem_timer.start(10000)

            if self.moss_bool   == 0:
                self.unlock_new_level()
                self.moss_bool   =1
            else:
                pass

    def increment_ecosystem(self):
        ecosystem_label = self.findChild(QLabel, "ecosystem_label")

        self.ecosystem_total += 1
        self.ecosystem_label.setText(f"{self.ecosystem_total:.6g}")

    def waterfall_eco(self):
        waterfall_label = self.findChild(QLabel, "waterfall_label")

        if self.moss_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.moss_total} more Moss and Ferns to create this")
        else:
            self.moss_total -= 10
            self.moss_label.setText(f"{self.moss_total:.6g}")
            self.waterfall_total += 1
            self.waterfall_label.setText(f"{self.waterfall_total:.6g}")

            self.moss_timer = QTimer(self)
            self.moss_timer.timeout.connect(self.increment_moss)
            self.moss_timer.start(10000)

            if self.water_bool   == 0:
                self.unlock_new_level()
                self.water_bool   =1
            else:
                pass

    def increment_moss(self):
        moss_label = self.findChild(QLabel, "moss_label")

        self.moss_total += 1
        self.moss_label.setText(f"{self.moss_total:.6g}")

    def fauna_eco(self):
        fauna_label = self.findChild(QLabel, "fauna_label")

        if self.fauna_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.waterfall_total} more Minature Waterfalls to foster this")
        else:
            self.waterfall_total -= 10
            self.waterfall_label.setText(f"{self.waterfall_total:.6g}")
            self.fauna_total += 1
            self.fauna_label.setText(f"{self.fauna_total:.6g}")

            self.waterfall_timer = QTimer(self)
            self.waterfall_timer.timeout.connect(self.increment_waterfall)
            self.waterfall_timer.start(10000)

            if self.fauna_bool   == 0:
                self.unlock_new_level()
                self.fauna_bool   =1
            else:
                pass

    def increment_waterfall(self):
        waterfall_label = self.findChild(QLabel, "waterfall_label")

        self.waterfall_total += 1
        self.waterfall_label.setText(f"{self.waterfall_total:.6g}")

    def blooming_eco(self):
        blooming_label = self.findChild(QLabel, "blooming_label")

        if self.blooming_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.fauna_total} more Mini Fauna's to induce this")
        else:
            self.fauna_total -= 10
            self.fauna_label.setText(f"{self.fauna_total:.6g}")
            self.blooming_total += 1
            self.blooming_label.setText(f"{self.blooming_total:.6g}")

            self.fauna_timer = QTimer(self)
            self.fauna_timer.timeout.connect(self.increment_fauna)
            self.fauna_timer.start(10000)

            if self.blooming_bool   == 0:
                self.unlock_new_level()
                self.blooming_bool   =1
            else:
                pass

    def increment_fauna(self):
        fauna_label = self.findChild(QLabel, "fauna_label")

        self.fauna_total += 1
        self.fauna_label.setText(f"{self.fauna_total:.6g}")

    def photo_eco(self):
        photo_label = self.findChild(QLabel, "photo_label")

        if self.photo_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.blooming_total} more Blooming Flowers to capture this")
        else:
            self.blooming_total -= 10
            self.blooming_label.setText(f"{self.blooming_total:.6g}")
            self.photo_total += 1
            self.photo_label.setText(f"{self.photo_total:.6g}")

            self.blooming_timer = QTimer(self)
            self.blooming_timer.timeout.connect(self.increment_blooming)
            self.blooming_timer.start(10000)

            if self.photo_bool   == 0:
                self.unlock_new_level()
                self.photo_bool   =1
            else:
                pass

    def increment_blooming(self):
        blooming_label = self.findChild(QLabel, "blooming_label")

        self.blooming_total += 1
        self.blooming_label.setText(f"{self.blooming_total:.6g}")

    def bonsai_eco(self):
        bonsai_label = self.findChild(QLabel, "bonsai_label")

        if self.bonsai_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.photo_total} more Photosynthesis Boosts to grow this")
        else:
            self.photo_total -= 10
            self.photo_label.setText(f"{self.photo_total:.6g}")
            self.bonsai_total += 1
            self.bonsai_label.setText(f"{self.bonsai_total:.6g}")

            self.photo_timer = QTimer(self)
            self.photo_timer.timeout.connect(self.increment_photo)
            self.photo_timer.start(10000)

            if self.bonsai_bool   == 0:
                self.unlock_new_level()
                self.bonsai_bool   =1
            else:
                pass

    def increment_photo(self):
        photo_label = self.findChild(QLabel, "photo_label")

        self.photo_total += 1
        self.photo_label.setText(f"{self.photo_total:.6g}")

    def pond_eco(self):
        pond_label = self.findChild(QLabel, "pond_label")

        if self.pond_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.bonsai_total} more Mini Bonsai Trees to build this")
        else:
            self.bonsai_total -= 10
            self.bonsai_label.setText(f"{self.bonsai_total:.6g}")
            self.pond_total += 1
            self.pond_label.setText(f"{self.pond_total:.6g}")

            self.bonsai_timer = QTimer(self)
            self.bonsai_timer.timeout.connect(self.increment_bonsai)
            self.bonsai_timer.start(10000)

            if self.pond_bool   == 0:
                self.unlock_new_level()
                self.pond_bool   =1
            else:
                pass

    def increment_bonsai(self):
        bonsai_label = self.findChild(QLabel, "bonsai_label")

        self.bonsai_total += 1
        self.bonsai_label.setText(f"{self.bonsai_total:.6g}")

    def insect_eco(self):
        insect_label = self.findChild(QLabel, "insect_label")

        if self.insect_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.pond_total} more Miniature Pond to attract this")
        else:
            self.pond_total -= 10
            self.pond_label.setText(f"{self.pond_total:.6g}")
            self.insect_total += 1
            self.insect_label.setText(f"{self.insect_total:.6g}")

            self.pond_timer = QTimer(self)
            self.pond_timer.timeout.connect(self.increment_pond)
            self.pond_timer.start(10000)

            if self.insect_bool   == 0:
                self.unlock_new_level()
                self.insect_bool   =1
            else:
                pass

    def increment_pond(self):
        pond_label = self.findChild(QLabel, "pond_label")

        self.pond_total += 1
        self.pond_label.setText(f"{self.pond_total:.6g}")
          
    def decor_eco(self):
        decor_label = self.findChild(QLabel, "decor_label")

        if self.decor_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.insect_total} more Insect Symphony's to adorn this")
        else:
            self.insect_total -= 10
            self.insect_label.setText(f"{self.insect_total:.6g}")
            self.decor_total += 1
            self.decor_label.setText(f"{self.decor_total:.6g}")

            self.insect_timer = QTimer(self)
            self.insect_timer.timeout.connect(self.increment_insect)
            self.insect_timer.start(10000)

            if self.decor_bool   == 0:
                self.unlock_new_level()
                self.decor_bool   =1
            else:
                pass

    def increment_insect(self):
        insect_label = self.findChild(QLabel, "insect_label")

        self.insect_total += 1
        self.insect_label.setText(f"{self.insect_total:.6g}")

    def orchids_eco(self):
        orchids_label = self.findChild(QLabel, "orchids_label")

        if self.orchids_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.decor_total} more Terrarium Decor to cultivate this")
        else:
            self.decor_total -= 10
            self.decor_label.setText(f"{self.decor_total:.6g}")
            self.orchids_total += 1
            self.orchids_label.setText(f"{self.orchids_total:.6g}")

            self.decor_timer = QTimer(self)
            self.decor_timer.timeout.connect(self.increment_decor)
            self.decor_timer.start(10000)

            if self.orchids_bool   == 0:
                self.unlock_new_level()
                self.orchids_boolc   =1
            else:
                pass

    def increment_decor(self):
        decor_label = self.findChild(QLabel, "decor_label")

        self.decor_total += 1
        self.decor_label.setText(f"{self.decor_total:.6g}")

    def geode_eco(self):
        geode_label = self.findChild(QLabel, "geode_label")

        if self.orchids_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.orchids_total} more Rare Orchids to cultivate this")
        else:
            self.orchids_total -= 10
            self.orchids_label.setText(f"{self.orchids_total:.6g}")
            self.geode_total += 1
            self.geode_label.setText(f"{self.geode_total:.6g}")

            self.orchids_timer = QTimer(self)
            self.orchids_timer.timeout.connect(self.increment_orchids)
            self.orchids_timer.start(10000)

            if self.geode_bool   == 0:
                self.unlock_new_level()
                self.geode_bool   =1
            else:
                pass

    def increment_orchids(self):
        orchids_label = self.findChild(QLabel, "orchids_label")

        self.orchids_total += 1
        self.orchids_label.setText(f"{self.orchids_total:.6g}")

    def time_eco(self):
        time_label = self.findChild(QLabel, "time_label")

        if self.time_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.geode_total} more Time-Lapse Growth to unlock this")
        else:
            self.geode_total -= 10
            self.geode_label.setText(f"{self.geode_total:.6g}")
            self.time_total += 1
            self.time_label.setText(f"{self.time_total:.6g}")

            self.geode_timer = QTimer(self)
            self.geode_timer.timeout.connect(self.increment_geode)
            self.geode_timer.start(10000)

            if self.time_bool   == 0:
                self.unlock_new_level()
                self.time_bool   =1
            else:
                pass

    def increment_geode(self):
        geode_label = self.findChild(QLabel, "geode_label")

        self.geode_total += 1
        self.geode_label.setText(f"{self.geode_total:.6g}")

    def cosmic_eco(self):
        cosmic_label = self.findChild(QLabel, "cosmic_label")

        if self.cosmic_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.time_total} more Time-Lapse Growth to discover this")
        else:
            self.time_total -= 10
            self.time_label.setText(f"{self.time_total:.6g}")
            self.cosmic_total += 1
            self.cosmic_label.setText(f"{self.cosmic_total:.6g}")

            self.time_timer = QTimer(self)
            self.time_timer.timeout.connect(self.increment_time)
            self.time_timer.start(10000)

            if self.cosmic_bool   == 0:
                self.unlock_new_level()
                self.cosmic_bool   =1
            else:
                pass

    def increment_time(self):
        time_label = self.findChild(QLabel, "time_label")

        self.time_total += 1
        self.time_label.setText(f"{self.time_total:.6g}")

    def fossils_eco(self):
        fossils_label = self.findChild(QLabel, "fossils_label")

        if self.fossils_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.cosmic_total} more Cosmic Dust to unearth this")
        else:
            self.cosmic_total -= 10
            self.cosmic_label.setText(f"{self.cosmic_total:.6g}")
            self.fossils_total += 1
            self.fossils_label.setText(f"{self.fossils_total:.6g}")

            self.cosmic_timer = QTimer(self)
            self.cosmic_timer.timeout.connect(self.increment_cosmic)
            self.cosmic_timer.start(10000)

            if self.fossils_bool   == 0:
                self.unlock_new_level()
                self.fossils_bool   =1
            else:
                pass

    def increment_cosmic(self):
        cosmic_label = self.findChild(QLabel, "cosmic_label")

        self.cosmic_total += 1
        self.cosmic_label.setText(f"{self.cosmic_total:.6g}")

    def eternal_eco(self):
        eternal_label = self.findChild(QLabel, "eternal_label")

        if self.eternal_total < 10:
            QMessageBox.critical(self, "Error", f"You need {10 - self.fossils_total} more Ancient Fossils to achieve this")
        else:
            self.fossils_total -= 10
            self.fossils_label.setText(f"{self.fossils_total:.6g}")
            self.eternal_total += 1
            self.eternal_label.setText(f"{self.eternal_total:.6g}")

            self.fossils_timer = QTimer(self)
            self.fossils_timer.timeout.connect(self.increment_fossils)
            self.fossils_timer.start(10000)

            if self.eternal_bool   == 0:
                self.unlock_new_level()
                self.eternal_bool   =1
            else:
                pass

    def increment_fossils(self):
        fossils_label = self.findChild(QLabel, "fossils_label")

        self.fossils_total += 1
        self.fossils_label.setText(f"{self.fossils_total:.6g}")

#Calling the App.exec to run:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Terrarium Idle Clicker')
    window.show()
    sys.exit(app.exec())