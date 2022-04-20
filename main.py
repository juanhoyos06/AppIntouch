import sys
from PySide2.QtWidgets import QApplication
from Motel.Mundo.mundo import *
from Motel.Vista.gui.gui import VentanaLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    motel = Motel()
    window = VentanaLogin(motel)
    sys.exit(app.exec_())