import subprocess
import psutil
import os
from tkinter import *

#############################################################################################
#                                                                                           #
#                                 Windows 11 (24H2)에서 작성됨                               #
#                                   OS 빌드: 26100.2605                                     #
#                                                                                           #
#                                                                                           #
#############################################################################################


# 사용 가능한 파티션  
def get_available_partitions():
    drives = []
    partitions = psutil.disk_partitions()

    ## print(f"실제 파티션 목록:{partitions}")
    
    for partition in partitions:
        if os.path.exists(partition.mountpoint):
            drive_letter = partition.device.strip("\\")
            drives.append(drive_letter[0])


    ## print(f"실제 파티션 목록:{drives}")
    return drives


# Windows Terminal Git bash 실행

def open_terminal_partition(drive_letter):
    try:
        "Windows OS의 정확한 루트디렉터리 선택"
        drive_path = f"{drive_letter}:\\"

        if not os.path.exists(f"{drive_letter}://"):
            print(f"드라이브 {drive_letter}를 찾을 수 없습니다.")
            return 
        
        command = f'start wt -p "Git Bash" --title "현재 위치: {drive_letter}" -d "{drive_path}'

        subprocess.run(command, shell=True, check=True)
        print(f"파워쉘 스크립트 실행성공, 선택된 파티션 {drive_letter}: 드라이브")
    
    except subprocess.CalledProcessError as e: 
        print(f"파워쉘 스크립트 실행 실패: {e}")


# 드라이브 선택
def display_drive_menu():

    drive_letter = get_available_partitions()

    if not drive_letter:
        print("파티션이 존재하지 않습니다.")
        return None

    print("파티션을 선택하세요:")
    for i, partition in enumerate(drive_letter, start=1):
        print(f"[{i}] - {partition} 드라이브")

    while True:
        try:
            choice = int(input("숫자를 입력하여 드라이브를 선택하세요: "))

            if 1 <= choice <= len(drive_letter):
                return drive_letter[choice - 1]
            else:
                print("존재하지 않는 파티션입니다. 다시 선택해주세요.")
        
        except ValueError:
            print("숫자로 입력하세요.")

# def select_terminal_profile()

if __name__ == "__main__":
    selected_drive = display_drive_menu()
    print(f"선택된 드라이브{selected_drive}")
    if selected_drive:
        open_terminal_partition(selected_drive)