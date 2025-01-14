import sys
import subprocess
import psutil
import os
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox 

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
# 터미널로 실행할때 사용용
def open_terminal_partition(drive_paths):
    try:
        "드라이브 루트 경로"
        print(f"현재 드라이브 {drive_paths}")
        if not os.path.exists(f"{drive_paths}"):
            print(f"{drive_paths}를 찾을 수 없습니다.")
            return 
        
        command = f'start wt -p "Git Bash" --title "현재 위치: {drive_paths}" -d "{drive_paths}"'
        subprocess.run(command, shell=True, check=True)

    except subprocess.CalledProcessError as e: 
        QMessageBox.critical(None, "오류", f"드라이브 불러오기 실패: {e}")
    except FileNotFoundError as e:
        QMessageBox.critical(None, "오류", str(e))






# PyQt Init
#
class EasyTerminal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        app_widget = QWidget()
        self.setGeometry(600, 150, 500, 450)
        self.setWindowTitle('EasyTerminal')
     
        self.label = QLabel("사용 가능한 드라이브 목록")

        # 레이아웃 설정
        layout = QVBoxLayout(app_widget)
        layout.addWidget(self.label)
        
        self.select_btn = QPushButton("선택")
        self.select_btn.clicked.connect(self.on_selected_drive)
        layout.addWidget(self.select_btn)

        self.exit_btn = QPushButton("종료")
        self.exit_btn.clicked.connect(self.close)
        layout.addWidget(self.exit_btn)

        self.setCentralWidget(app_widget)

        self.print_drive_lists()       
                
        self.show()

    def print_drive_lists(self):
        drives = get_available_partitions()
        self.drive_list = QListWidget()
        
        if not drives:
            QMessageBox.critical(self, "오류", "사용 가능한 드라이브가 존재하지 않습니다. 시스템을 점검하세요.")
            sys.exit()

        for drive in drives:
            self.drive_list.addItem(f"{drive} 드라이브")

        layout = self.centralWidget().layout()
        layout.addWidget(self.drive_list)

    def on_selected_drive(self):
        sel_item = self.drive_list.currentItem()

        if sel_item:
            drive_letter = sel_item.text().replace(" 드라이브", "")
            drive_path = fr"{drive_letter}:\\"
            open_terminal_partition(drive_path)
        else:
            QMessageBox.warning(self, "경고", "드라이브를 선택하세요")  

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EasyTerminal()
    sys.exit(app.exec_())




# Legecy Code
#
#
#
#
#
#


# 드라이브 선택
# def display_drive_menu():

#     drive_letter = get_available_partitions()

#     if not drive_letter:
#         #print("파티션이 존재하지 않습니다.")
     
#         return None

#     print("파티션을 선택하세요:")
#     for i, partition in enumerate(drive_letter, start=1):
#         print(f"[{i}] - {partition} 드라이브")

#     while True:
#         try:
#             choice = int(input("숫자를 입력하여 드라이브를 선택하세요: "))

#             if 1 <= choice <= len(drive_letter):
#                 return drive_letter[choice - 1]
#             else:
#                 print("존재하지 않는 파티션입니다. 다시 선택해주세요.")
        
#         except ValueError:
#             print("숫자로 입력하세요.")
