import threading
import os,sys,yaml,ctypes,platform
from ctypes import cdll
from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtCore import QTimer, QTime
from ui_ota_hid import Ui_ota_tota_hid
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication , QWidget, QFileDialog
CallbackType = ctypes.CFUNCTYPE(None, ctypes.c_int)

class MainWindow(QWidget,Ui_ota_tota_hid):
    update_progress_signal = Signal(int)
    stop_timer_signal = Signal()
    start_timer_signal = Signal()
    def __init__(self,config_files_path):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(config_files_path,"windowIcon.jpg")))

        #var
        self.bin_path =None
        self.bin_count = 0
        self.bin_sending_index = 0
        self.hid_ota_cfg_name = None
        self.config_path = None
        self.cfg_dict = None
        self.dylib_path = None
        self.config_files_path = config_files_path
        self.dylib_name = None
        self.hid_device_vid = None
        self.hid_device_pid = None
        self.packet_interval = None
        self.work_interval = None
        # self.shakehd_cfg_path = None
        self.log_switch = False
        self.log_switch_enable = False
        self.log_path = None
        self.running = False

        self.load_config_file_info()
        # usb_vid = int(self.hid_device_vid, 16)
        # usb_pid = int(self.hid_device_pid, 16)
        self.btn_browse.clicked.connect(self.onBtn_browse)
        self.btn_upgrade.clicked.connect(self.hid_ota_thread)
        # self.btn_upgrade.clicked.connect(self.startTimer)
        self.btn_log_browse.clicked.connect(self.onBtn_log_browse)
        self.ckbox_log_switch.stateChanged.connect(self.logSwitch_state_changed)
        # self.btn_cfg_browse.clicked.connect(self.onBtn_cfg_browse)
        self.stop_timer_signal.connect(self.upgrade_stop)
        self.start_timer_signal.connect(self.startTimer)
        self.update_progress_signal.connect(self.update_progress)


    def load_config_file_info(self):
        #init local var
        self.hid_ota_cfg_name = "config.yaml"
        self.config_path = os.path.join(self.config_files_path, self.hid_ota_cfg_name)
        win_name = "BESOTAUSBHIDUPGRADE.dll"
        mac_name = "libbes_usb_hid_ota_upgrade_macos.dylib"
        if platform.system() == "Windows":
            architecture = platform.architecture()[0]  # 获取位宽信息
            if architecture == '64bit':
                self.dylib_name = win_name  # 对于64位系统使用的名称
            elif architecture == '32bit':
                self.dylib_name = win_name  # 对于32位系统使用的名称
        elif platform.system() == "Darwin":
            self.dylib_name = mac_name
        else:
            raise Exception("Error: Unsupported OS ")

        self.dylib_path = os.path.join(self.config_files_path,self.dylib_name)

        try:
            # load dll
            self.hid_ota_dll = cdll.LoadLibrary(self.dylib_path)
        except OSError as e:
            print(f"Error loading dynamic library from {self.dylib_path}: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"General Error: {e}")
            sys.exit(1)

        #open config file
        try:
            with open(self.config_path,'r') as f:
                self.cfg_dict = yaml.load(f,Loader=yaml.FullLoader)
            #get hid ota config var
            hid_config = self.cfg_dict.get('HID_CONFIG', {})
            self.bin_path = hid_config.get("hid_ota_bin_path", '')
            self.hid_device_vid = hid_config.get("hid_ota_device_vid", '')
            self.hid_device_pid = hid_config.get('hid_ota_device_pid', '')
            self.log_switch = hid_config.get('hid_ota_log_switch', '')
            self.log_path = hid_config.get('hid_ota_log_path', '')
            # self.shakehd_cfg_path = hid_config.get('hid_ota_shakehd_cfg_path', '')
            self.packet_interval = hid_config.get("hid_ota_packet_interval","")
            self.work_interval = hid_config.get("hid_ota_work_interval","")
            self.log_switch_enable = hid_config.get("hid_ota_log_switch_enable","")
        except:
            print("Error: Failed to open config.yaml !\n")
            assert 0

        #init ui var
        self.label_sending_index.setText(str(0))
        self.label_total_bins.setText(str(0))
        self.line_vid.setText(self.hid_device_vid)
        self.line_pid.setText(self.hid_device_pid)
        self.line_bin_path.setText(self.bin_path)
        self.line_packet_interval.setText(str(self.packet_interval))
        self.line_work_interval.setText(str(self.work_interval))
        self.line_log_path.setText(self.log_path)
        # self.line_cfg_path.setText(self.shakehd_cfg_path)
        self.ckbox_log_switch.setChecked(self.log_switch)
        
        #init QTimer  QTime timeedit
        self.timer = QTimer(self)
        self.time = QTime(0, 0)
        self.timer.timeout.connect(self.updateTime)
        self.timeEdit.setDisplayFormat("mm:ss")

        #init state
        if self.log_switch_enable :
            self.ckbox_log_switch.setVisible(True)
            self.btn_log_browse.setVisible(True)
            self.line_log_path.setVisible(True)
        else:
            
            self.ckbox_log_switch.setVisible(False)
            self.btn_log_browse.setVisible(False)
            self.line_log_path.setVisible(False)
            
            
        if self.ckbox_log_switch.isChecked():
            self.btn_log_browse.setEnabled(True)
        else:
            self.btn_log_browse.setEnabled(False)
        

    def logSwitch_state_changed(self):
        if not self.ckbox_log_switch.isChecked():
            self.btn_log_browse.setEnabled(False)
        else:
            self.btn_log_browse.setEnabled(True)

    def onBtn_log_browse(self):
        dir_path = QFileDialog.getExistingDirectory(self, "select cfg dir path",self.log_path)
        if dir_path:
            self.log_path = dir_path
            self.line_log_path.setText(self.log_path)
    
    # def onBtn_cfg_browse(self):
    #     dir_path = QFileDialog.getExistingDirectory(self, "select cfg dir path",self.shakehd_cfg_path)
    #     if dir_path:
    #         self.shakehd_cfg_path =dir_path
    #         self.line_cfg_path.setText(self.shakehd_cfg_path)

    def updateTime(self):
        # update time and set timeedit
        self.time = self.time.addSecs(1)
        self.timeEdit.setTime(self.time)

    def startTimer(self):
        # reset time and start timer
        self.time.setHMS(0, 0, 0)
        self.timer.start(1000)  # update per second

    def save_config_file_info(self):
        #load local vars
        self.packet_interval = self.line_packet_interval.text()
        self.work_interval = self.line_work_interval.text()
        self.hid_device_vid = self.line_vid.text()
        self.hid_device_pid = self.line_pid.text()
        self.log_path = self.line_log_path.text()
        # self.shakehd_cfg_path = self.line_cfg_path.text()
        self.bin_path = self.line_bin_path.text()
        self.log_switch = self.ckbox_log_switch.isChecked()
        #update dict content
        self.cfg_dict["HID_CONFIG"]["hid_ota_bin_path"] = self.bin_path
        self.cfg_dict["HID_CONFIG"]["hid_ota_device_vid"] = str(self.hid_device_vid)
        self.cfg_dict["HID_CONFIG"]["hid_ota_device_pid"] = str(self.hid_device_pid)
        self.cfg_dict["HID_CONFIG"]["hid_ota_log_path"] = self.log_path
        self.cfg_dict["HID_CONFIG"]["hid_ota_log_switch"] = bool(self.log_switch)
        self.cfg_dict["HID_CONFIG"]["hid_ota_packet_interval"] = self.packet_interval
        self.cfg_dict["HID_CONFIG"]["hid_ota_work_interval"] = self.work_interval
        # self.cfg_dict["HID_CONFIG"]["hid_ota_shakehd_cfg_path"] = self.shakehd_cfg_path

        #write to yaml
        try:
            with open(self.config_path,'w') as f:
                yaml.safe_dump(self.cfg_dict, f,default_flow_style=False, encoding='utf-8', allow_unicode=True)
        except Exception as e:
            print("Error: Failed to save config.yaml !\n", e)

    def hid_ota_thread(self):
        self.hid_upgrade_thread = threading.Thread(target=self.onBtn_upgrade)
        self.hid_upgrade_thread.start()      

    def read_first_four_bytes(self,file_path):
        try:
            with open(file_path, 'rb') as file:
                data = file.read(4)  # read the first four bytes
                return data
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
            return None
        
    def onBtn_browse(self):
        path = ''
        path = self.bin_path
        if path != None:
            str_list : list[str] = QFileDialog.getOpenFileName(self,"Select bin file",path,'*.bin;;*.hex;;*.*')
        else:
            str_list: list[str] = QFileDialog.getOpenFileName(self, 'Select bin file', '', '*.bin;;*.hex;;*.*')
        path = str_list[0]
        if len(path) != 0:
            self.line_bin_path.setText(path)
            self.bin_path = path

    @Slot(int)
    def update_progress(self, value):                 
        self.progressBar_ota.setValue(value)
        if value == 100  and self.bin_sending_index < self.bin_count:
            self.bin_sending_index+=1
            self.label_sending_index.setText(str(self.bin_sending_index))

    #call callback function
    def progress_callback(self,progress):
        # print(progress)
        self.update_progress_signal.emit(progress)
        
    def upgrade_stop(self):
        self.timer.stop()
        self.btn_upgrade.setEnabled(True) 

    def closeEvent(self, event: QCloseEvent):
        if self.btn_upgrade.isEnabled():
            self.save_config_file_info()
        else:
            self.stop_timer_signal.emit()
        return super().closeEvent(event)   

    def onBtn_upgrade(self):
        self.start_timer_signal.emit()
        self.save_config_file_info()

        if self.bin_path == '' or self.bin_path == None:
            print("Note: bin file path is None !\n"
                  "please select one bin file !\n")
            self.stop_timer_signal.emit()
            return
        # read bin file for first four bytes
        first_four_bytes = self.read_first_four_bytes(self.bin_path)
        if first_four_bytes is not None:
            self.bin_count = int.from_bytes(first_four_bytes, byteorder='little')
            print("The bin count is:", self.bin_count)
            self.label_total_bins.setText(str(self.bin_count))

        else:
            print("Error: the bin file is not correct")
            self.stop_timer_signal.emit()
            return
        self.bin_sending_index = 1
        self.label_sending_index.setText(str(self.bin_sending_index))
        #btn disable
        self.btn_upgrade.setEnabled(False)
        # add bin to vector
        self.hid_ota_dll.Add_Bin_File.argtypes = [ctypes.c_char_p]
        self.hid_ota_dll.Add_Bin_File.restype = ctypes.c_bool
        res = self.hid_ota_dll.Add_Bin_File(self.bin_path.encode('utf-8'))  # bool Add_Bin_File(char* pBinFilePath);
        if (res == False):
            print("Error: get the bin file failed in DLL \n")
            self.stop_timer_signal.emit()
            return

        # Convert string to hex int
        usb_vid = int(self.hid_device_vid, 16)
        usb_pid = int(self.hid_device_pid, 16)

        #Set the function's argument types and return type
        self.hid_ota_dll.Start_ota_update.argtypes = [ctypes.c_ushort, ctypes.c_ushort,CallbackType,ctypes.c_int,
                                                      ctypes.c_int,ctypes.c_int,ctypes.c_char_p]
        self.hid_ota_dll.Start_ota_update.restype = ctypes.c_int

        # set up callback function
        self.progress_callback_func = CallbackType(self.progress_callback)   

        #call dll function
        try:
            res = self.hid_ota_dll.Start_ota_update(ctypes.c_ushort(usb_vid), ctypes.c_ushort(usb_pid),
                                                    self.progress_callback_func,int(self.work_interval),
                                                    int(self.packet_interval),int(self.log_switch),
                                                    self.log_path.encode('utf-8'))
        except OSError as e:
            print(f"Error calling Start_ota_update: {e}")
            self.stop_timer_signal.emit()
            return
        if res != 1:
            print("Error: ota upgrade failed ! \n")
            self.stop_timer_signal.emit()
            return
        self.stop_timer_signal.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    os.environ['QT_LOGGING_RULES'] = '*.debug=false;qt.qpa.*=false;qt.qpa.fonts.*=false;qt.font.*=false'
    if getattr(sys,'frozen',False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(__file__)
    config_files_path = os.path.join(current_dir,"config")
    style_path = os.path.join(config_files_path,'style.qss')
    style_sheet: str = open(style_path).read()
    app.setStyleSheet(style_sheet)
    wind =MainWindow(config_files_path)
    wind.show()
    sys.exit(app.exec())


