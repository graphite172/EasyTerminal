import sys
import subprocess
import psutil
import os
import psutil
from ui.UI_easyterminal import Ui_EasyTerminal
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt6.QtCore import Qt

path = fr":\\"

#############################################################################################
#                                                                                           #
#                                 Windows 11 (24H2)에서 작성됨                               #
#                                   OS 빌드: 26100.2605                                     #
#                                                                                           #
#                                                                                           #
#############################################################################################

# 사용 가능한 파티션 확인
def get_available_partitions():
    drives = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        if os.path.exists(partition.mountpoint):
            drive_letter = partition.device.strip("\\")
            drives.append(drive_letter[0])

    return drives


# Windows Terminal Git bash 실행
# 터미널로 실행할때 사용
def open_terminal(drive_paths):
    try:
        "드라이브 루트 경로"
        print(f"현재 드라이브 {drive_paths}")
        if not os.path.exists(f"{drive_paths}"):
            print(f"{drive_paths}를 찾을 수 없습니다.")
            return 
        
        command = f'start wt -p "Git Bash" --title "현재 위치: {drive_paths}" -d "{drive_paths}"'
        subprocess.run(command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"오류: 터미널 실행 실패 - {e}")
        QMessageBox.critical(None, "오류", f"터미널 실행 실패: {e}")
    
    except FileNotFoundError as e:
        print(f"오류: 파일을 찾을 수 없음 - {e}")
        QMessageBox.critical(None, "오류", str(e))

# PyQt Init
#
class EasyTerminal(QMainWindow, Ui_EasyTerminal):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.load_drive_list()
        self.btn_tmopen.clicked.connect(self.selected_drive)    
    
    

    def load_drive_list(self):
        drives = get_available_partitions()

        if not drives:
            QMessageBox.critical(self,"오류", "사용 가능한 드라이브를 불러오지 못 했습니다.")
            sys.exit()

        model = QStandardItemModel()
        
        for drive in drives:
            item = QStandardItem(f"{drive} 드라이브")

            item.setEditable(False)
            font = QFont()
            font.setPointSize(15)
            item.setFont(font)

            model.appendRow(item)

        self.list_drive.setModel(model)
  
    def selected_drive(self):
        """선택한 드라이브에서 터미널 실행"""
        selected_index = self.list_drive.currentIndex()

        if selected_index.isValid():
            drive_path = selected_index.data().replace(" 드라이브", "").lower()
            drive_path = fr"{drive_path}:\\"

           
            if not drive_path.endswith(path):
                QMessageBox.warning(self, "경고", "잘못된 드라이브 경로입니다.")
                return
            
            print(f"선택한 드라이브: {drive_path}")  # 선택된 드라이브를 출력
            try:   
                open_terminal(drive_path)
            except Exception as e:
                QMessageBox.critical(self,"오류", f"터미널 실행 중 오류 발생: {e}")
        else:
            print("경고: 드라이브가 선택되지 않았습니다.")
            QMessageBox.warning(self, "경고", "드라이브를 선택하세요")

  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EasyTerminal()
    window.show()
    sys.exit(app.exec())

