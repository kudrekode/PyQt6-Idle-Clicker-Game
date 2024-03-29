# PyQt6-Idle-Clicker-Game
A simple Idle Clicker game created using Python and PyQt6 modules and QT Designer. 

The Game is inspired by Idle Clicker games in which a user clicks on one item, once they have clicked enough of that item, they obtain capital to click on the next item. This next item provides an automatic amount of the previous item. Thus, the more item levels you engage with/obtain, the more items you get of all the predecessing levels. 

Methodology:
1) Import PyQt6 modules and QT Designer.
   This has to be run in a virtual Python Environment to isolate from rest of computer infrastructure so a venv was set up.

2) Load and create UI using QT Designer.
  This was more tricky than I initially anticipated and I had already created the game logic and code with buttons in raw code before. So I had to change much of my code to work with the QT designer interface. This is achievable using self.findChild(WIDGET).connect(self.FUNCTION) to connect the .ui file and the code that was already implemented.
  To load the .ui files they had to be saved as .py files in the QT designer and then loadedd using PyQt6.uic import loadUi.

3) Create game logic.
   The game logic was fairly simple. Each level had the same structure of logic:
   
       def LEVEL_eco (self):
        LEVEL_label = self.findChild(QLabel, "LEVEL_label")

        if self.PREVIOUS_LEVEL_total < 10: 
            QMessageBox.critical(self,"Error", f"You need {10 - self.PREVIOUS_LEVEL_total} more to buy this")
        else:
            self.PREVIOUS_LEVEL_total -= 10
            self.PREVIOUS_LEVEL_label.setText(f"{self.sprout_total:.6g}")
            self.LEVEL_total += 1
            self.LEVEL_label.setText(f"{self.leafy_total:.6g}")

            self.LEVEL_timer = QTimer(self)
            self.LEVEL_timer.timeout.connect(self.increment_LEVEL)
            self.LEVEL_timer.start(10000)

            if self.LEVEL_bool  == 0:
                self.unlock_new_level()
                self.LEVEL_bool  =1
            else:
                pass
         def increment_LEVEL(self):
            LEVEL:_label = self.findChild(QLabel, "LEVEL_label")
    
            self.LEVEL_total += 1
            self.LEVEL_label.setText(f"{self.LEVEL_total:.6g}")

   Thus, each level has two functions. The first connects the label (output wdiget) of the UI file to the logic. It ensures that you cannot purchase a certain levels item unless you have enough of the previous levels item to afford it (producing an error message if this is the case). The function also starts a timer to increase the previous levels item every certain interval.
   The level is then increased by one (calling the unlock_new_level function) but ensures that a boolean function is set first to ensure that you can only go up a level once.

5) Import images.
   I created the images using some sotck royalty free photos from google images and Photoshop to created images that corresponded to each level. Each time the user obtains a new level, the image will dynamically change to reflect the new level.
   This proved difficult to import images effectively into the code through QT designer. Three functions were used in the GamePage Class to iterate over a code that loads the next image in the level sequence since the name of each image is only different via the number appended to the end of it, thus this sort of function proved concise and effective:
   
      def get_image_path_for_level(self, level):
              base_path = r"C:\Users\Terrarium Background\\"
              image_path = base_path + str(level) + ".png"
              return image_path

7) There is scope to changes this and evaluating it but after debugging i was satisfied with the result as a very basic Idle game strucutre using an iunconventional method (python) for game development. 
   



   
