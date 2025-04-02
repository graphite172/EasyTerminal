import sys
import re
import subprocess
import psutil
import os
from typing import Optional
from packaging import version
from ui.UI_easyterminal import Ui_EasyTerminal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QFont, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

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
def open_terminal(path):
    try:
        "드라이브 루트 경로"
        print(f"현재 드라이브 {path}")
        if not os.path.exists(f"{path}"):
            print(f"{path}를 찾을 수 없습니다.")
            QMessageBox.critical(None, "오류", f"지정된 {path}를 찾을 수 없습니다.")
            return 
        
        command = fr'start wt -p "Git Bash" --title "현재 위치: {path}" -d "{path}"'
        subprocess.run(command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"오류: 터미널 실행 실패 - {e}")
        QMessageBox.critical(None, "오류", f"터미널 실행 실패: {e}")
    
    except FileNotFoundError as e:
        print(f"오류: 파일을 찾을 수 없음 - {e}")
        QMessageBox.critical(None, "오류", str(e))


#권장 설치파일

def get_version_from_winget(cmd:list[str], package_id) -> Optional[str]:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False, shell=False, encoding="utf-8")
        version_list = []
        print(f"[INFO] 명령어 실행 결과: {result.stdout}")
        if result.returncode != 0 and result.returncode != 2:
            print(f"[ERROR] 명령어 실행 실패: {result.stderr}")


        for line in result.stdout.splitlines():
            if package_id in line:
                item = re.search(r"\d+(?:\.\d+)+(?:[-+]?\w*(?:\.\w+)*)?", line)
    
                if item:
                    version_list.append(item.group(0))

        if not version_list:
            print(f"[ERROR] {package_id}의 버전 정보가 없습니다.")            
            return None
        
        latest_version = max(version_list, key=lambda v: version.parse(v))
         # 버전 비교 
        print(f"[INFO] {package_id}의 최신 버전: {latest_version}")
    
        return latest_version
    except Exception as e:
        print(f"[ERROR] 예외 발생: {str(e)}")
    return None

def get_installed_version(package_id:str) -> str | None:
    """설치된 버전 확인"""
    return get_version_from_winget(["winget", "list", "--id", package_id, "-e"],package_id)

def get_avalible_version(package_id:str) -> str | None:
    """설치된 버전 확인"""
    return get_version_from_winget(["winget", "search", "--id", package_id, "-e"],package_id)


def compare_version_check(v1: str, v2: str) -> bool:
    """현재 버전 확인"""
    try:

        if not v1 or not v2:
            return False

        #v1_parts = list(map(int, v1.split('.')))
        #v2_parts = list(map(int, v2.split('.'))) 

        v1_parts = version.parse(v1)
        v2_parts = version.parse(v2) 
        print(f"현재버전: {v1_parts} / 최신버전: {v2_parts}")

        return v1_parts >= v2_parts
    except Exception as e:
        print(f"[ERROR] 버전 비교 중 오류 발생: {str(e)}")
        # 오류 발생 시 업데이트가 필요하다고 가정
        return False
    

def install_windows_terminal(parent=None):
    package_id = "Microsoft.WindowsTerminal"
    app_name = "Windows Terminal"

    current_version = get_installed_version(package_id)

    try:    
     if not current_version:
         subprocess.run(["winget", "install", "--id", package_id], check=True, shell=True)
         QMessageBox.information(None, "설치 완료", f"{app_name} 설치가 완료되었습니다.")
     else:
         latest_version = get_avalible_version(package_id) 

         if not latest_version:
                QMessageBox.warning(None, "경고", f"{app_name}의 최신 버전 정보를 가져올 수 없습니다.")
                return
         
         if not compare_version_check(current_version, latest_version):
             subprocess.run(["winget", "upgrade", "--id", package_id, "-e"], check=True, shell=True)
             QMessageBox.information(None, "업데이트 완료", f"{app_name} 업데이트가 완료되었습니다.")
         else:
                QMessageBox.information(None, "업데이트 완료", f"{app_name}는 최신 버전입니다.\n현재버전: {current_version}\n최신버전: {latest_version}")
    except subprocess.CalledProcessError as e:
        QMessageBox.critical(None, "오류", f"{app_name} 설치 실패: {e}")
    except Exception as e:
        QMessageBox.critical(None, "오류", f"알 수 없는 오류 발생: {e}")

def install_git_bash(parent=None):
    try:
        package_id = "Git.Git"
        app_name = "Git Bash"

        current_version = get_installed_version(package_id)
        latest_version = get_avalible_version(package_id)

        if not latest_version:
            QMessageBox.warning(None, "경고", f"{app_name}의 최신 버전 정보를 가져올 수 없습니다.")
            return
        
        if not compare_version_check(current_version, latest_version):
            subprocess.run(["winget", "upgrade", "--id", package_id, "-e"], check=True, shell=True)
            QMessageBox.information(None, "업데이트 완료", f"{app_name} 업데이트가 완료되었습니다.")
        else:
            QMessageBox.information(None, "업데이트 완료", f"{app_name}는 최신 버전입니다.\n현재버전: {current_version}\n최신버전: {latest_version}")
    except subprocess.CalledProcessError as e:
        QMessageBox.critical(None, "오류", f"Windows Terminal 설치 실패: {e}")
    except Exception as e:
        QMessageBox.critical(None, "오류", f"알 수 없는 오류 발생: {e}")

def install_powershell(parent=None):
    try:
        package_id = "Microsoft.Powershell"
        app_name = "Powershell"

        current_version = get_installed_version(package_id)
        latest_version = get_avalible_version(package_id)

        if not latest_version:
            QMessageBox.warning(None, "경고", f"{app_name}의 최신 버전 정보를 가져올 수 없습니다.")
            return
        
        if not compare_version_check(current_version, latest_version):
            subprocess.run(["winget", "upgrade", "--id", package_id, "-e"], check=True, shell=True)
            QMessageBox.information(None, "업데이트 완료", f"{app_name} 업데이트가 완료되었습니다.")
        else:
            QMessageBox.information(None, "업데이트 완료", f"{app_name}는 최신 버전입니다.\n현재버전: {current_version}\n최신버전: {latest_version}")
    except subprocess.CalledProcessError as e:
        QMessageBox.critical(None, "오류", f"Windows Terminal 설치 실패: {e}")
    except Exception as e:
        QMessageBox.critical(None, "오류", f"알 수 없는 오류 발생: {e}")

def install_python_lts(parent=None):
    try:
        package_id = "Python.Python"
        app_name = "Python LTS"

        current_version = get_installed_version(package_id)
        latest_version = get_avalible_version(package_id)

        if not latest_version:
            QMessageBox.warning(None, "경고", f"{app_name}의 최신 버전 정보를 가져올 수 없습니다.")
            return
        
        if not compare_version_check(current_version, latest_version):
            subprocess.run(["winget", "upgrade", "--id", package_id, "-e"], check=True, shell=True)
            QMessageBox.information(None, "업데이트 완료", f"{app_name} 업데이트가 완료되었습니다.")
        else:
            QMessageBox.information(None, "업데이트 완료", f"{app_name}는 최신 버전입니다.\n현재버전: {current_version}\n최신버전: {latest_version}")
    except subprocess.CalledProcessError as e:
        QMessageBox.critical(None, "오류", f"Windows Terminal 설치 실패: {e}")
    except Exception as e:
        QMessageBox.critical(None, "오류", f"알 수 없는 오류 발생: {e}")

# Easy Terminal Main
class EasyTerminal(QMainWindow, Ui_EasyTerminal):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.load_drive_list()
        self.btn_tmopen.clicked.connect(self.selected_drive)
        self.btn_find_path.clicked.connect(self.selected_directory)

        # 설치 버튼 연결
        self.btn_installtm.clicked.connect(lambda: install_windows_terminal(self))
        self.btn_installgitbash.clicked.connect(lambda: install_git_bash(self))
        self.btn_installpowershell.clicked.connect(lambda: install_powershell(self))      
        self.btn_installPython.clicked.connect(lambda: install_python_lts(self))

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
  
    # 드라이브 경로 선택 후 터미널 실행
    def selected_directory(self):
        selected_path = QFileDialog.getExistingDirectory(self,  "경로 선택")

        if selected_path:
            print(f"선택한 경로: {selected_path}")

            try:
                open_terminal(selected_path)
            except Exception as e:
                QMessageBox.critical(self,"오류", f"터미널 실행 중 오류 발생: {e}")
        else:
            print("경고: 경로가 선택되지 않았습니다.")
            QMessageBox.warning(self, "경고", "경로를 선택하세요")
    
    # ListView에서 선택한 드라이브로 터미널 실행
    def selected_drive(self):
        """선택한 드라이브에서 터미널 실행"""
        selected_drive = self.list_drive.currentIndex()
        
        if selected_drive.isValid():
            drive_label = selected_drive.data()
           
            drive_letter = drive_label[0].upper()
            drive_path = fr"{drive_letter}:\\"

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

