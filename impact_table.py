from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_dlgImpacts      ##pode-se fazer modificações na interface gráfica feita no qtdesigner com esse Ui_dlgImpacts


class DlgTable(QDialog, Ui_dlgImpacts):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)
        
        self.tblImpacts.setColumnWidth(1, 350)  ##alterando a largura de uma coluna ESPECÍFICA (segunda coluna - os indices começam em 0) para tamanho 350) dentro da janela tblImpacts.ui. Reparar que alterar a largura de uma janela específica não é possível de fazer no QTDESIGNER.