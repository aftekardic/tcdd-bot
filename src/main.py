from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from ui import Ui_MainWindow
from datetime import datetime
from rpa import RPA
from custom_tools import Tools


istasyonList = ['Adana', 'Adana (Kiremithane)', 'Adapazarı', 'Adnanmenderes Havaalanı', 'Afyon A.Çetinkaya', 'Ahmetler', 'Ahmetli', 'Akgedik', 'Akhisar', 'Aksakal', 'Akçadağ', 'Akçamağara', 'Akşehir', 'Alayunt', 'Alayunt Müselles', 'Alaşehir', 'Alifuatpaşa', 'Aliköy', 'Alp', 'Alpu', 'Alpullu', 'Alöve', 'Amasya', 'Ankara Gar', 'Araplı', 'Argıthan', 'Arifiye', 'Artova', 'Arıkören', 'Asmakaya', 'Atça', 'Avşar', 'Aydın', 'Ayran', 'Ayrancı', 'Ayvacık', 'Aşkale', 'Bahçe', 'Bahçeli (Km.755+290 S)', 'Bahçeşehir', 'Bahçıvanova', 'Bakır', 'Balıkesir', 'Balıkesir (Gökköy)', 'Balıköy', 'Balışıh', 'Banaz', 'Bandırma Şehir', 'Baraklı', 'Baskil', 'Batman', 'Battalgazi', 'Bağıştaş', 'Bedirli', 'Belemedik', 'Bereket', 'Beyhan', 'Beylikköprü', 'Beylikova', 'Beyoğlu', 'Beşiri', 'Bilecik', 'Bilecik YHT', 'Bismil', 'Biçer', 'Bor', 'Bostankaya', 'Bozkanat', 'Bozkurt', 'Bozüyük', 'Bozüyük YHT', 'Boğazköprü', 'Boğazköprü Müselles', 'Boğazköy', 'Buharkent', 'Burdur', 'Böğecik', 'Büyükderbent YHT', 'Büyükçobanlar', 'Caferli', 'Ceyhan', 'Cürek', 'Dazkırı', 'Demirdağ', 'Demiriz', 'Demirkapı', 'Demirli', 'Demiryurt', 'Demirözü', 'Denizli', 'Derince YHT', 'Değirmenözü', 'Değirmisaz', 'Diliskelesi YHT', 'Dinar', 'Divriği', 'Diyarbakır', 'Doğançay', 'Doğanşehir', 'Dumlupınar', 'Durak', 'Dursunbey', 'Döğer', 'ERYAMAN YHT', 'Edirne', 'Ekerek', 'Ekinova', 'Elazığ', 'Elmadağ', 'Emiralem', 'Emirler', 'Erbaş', 'Ereğli', 'Ergani', 'Eriç', 'Erzincan', 'Erzurum', 'Eskişehir', 'Evciler', 'Eşme', 'Fevzipaşa', 'Fırat', 'Gazellidere', 'Gaziantep', 'Gaziemir', 'Gazlıgöl', 'Gebze', 'Genç', 'Germencik', 'Germiyan', 'Gezin', 'Goncalı', 'Goncalı Müselles', 'Gökçedağ', 'Gökçekısık', 'Gölbaşı', 'Gölcük', 'Gömeç', 'Göçentaşı', 'Güllübağ', 'Gümüş', 'Gümüşgün', 'Gündoğan', 'Güneyköy', 'Güneş', 'Güzelbeyli', 'Güzelyurt', 'Hacıbayram', 'Hacıkırı', 'Hacırahmanlı', 'Hanlı', 'Hasankale', 'Havza', 'Hekimhan', 'Hereke YHT', 'Himmetdede', 'Horasan', 'Horozköy', 'Horozluhan', 'Horsunlu', 'Huzurkent', 'Hüyük', 'Ildızım', 'Ilgın', 'Ilıca', 'Irmak', 'Isparta', 'Ispartakule', 'Kabakça', 'Kadılı', 'Kadınhan', 'Kaklık', 'Kalecik', 'Kalkancık', 'Kalın', 'Kandilli', 'Kangal', 'Kanlıca', 'Kapaklı', 'Kapıdere İstasyonu', 'Kapıkule', 'Karaali', 'Karaali', 'Karaağaçlı', 'Karabük', 'Karaisalıbucağı', 'Karakuyu', 'Karaköy', 'Karalar', 'Karaman', 'Karaosman', 'Karasenir', 'Karasu', 'Karaurgan', 'Karaözü', 'Kars', 'Kavak', 'Kavaklıdere', 'Kayabaşı', 'Kayabeyli', 'Kayaş', 'Kayseri', 'Kayseri (İncesu)', 'Kayışlar', 'Kaşınhan', 'Kelebek', 'Kemah', 'Kemaliye Çaltı', 'Kemerhisar', 'Keykubat', 'Keçiborlu', 'Kireç', 'Km. 30+500', 'Km. 37+362', 'Km.102+600', 'Km.139+500', 'Km.156 Durak', 'Km.171+000', 'Km.176+000', 'Km.186+000',
                'Km.282+200', 'Km.286+500', 'Konaklar', 'Konya', 'Konya (Selçuklu YHT)', 'Kozdere', 'Kumlu Sayding', 'Kunduz', 'Kurbağalı', 'Kurfallı', 'Kurt', 'Kurtalan', 'Kuyucak', 'Kuşcenneti', 'Kuşsarayı', 'Köprüağzı', 'Köprüköy', 'Köprüören', 'Köşk', 'Kürk', 'Kütahya', 'Kılıçlar', 'Kırkağaç', 'Kırıkkale', 'Kırıkkale YHT', 'Kızoğlu', 'Kızılca', 'Kızılinler', 'Ladik', 'Lalahan', 'Leylek', 'Lüleburgaz', 'Maden', 'Malatya', 'Mamure', 'Manisa', 'Mazlumlar', 'Menderes', 'Menemen', 'Mercan', 'Meydan', 'Mezitler', 'Meşelidüz', 'Mithatpaşa', 'Muradiye', 'Muratlı', 'Mustafayavuz', 'Muş', 'Narlı', 'Nazilli', 'Nizip', 'Niğde', 'Nohutova', 'Nurdağ', 'Nusrat', 'Ortaklar', 'Osmancık', 'Osmaneli', 'Osmaniye', 'Oturak', 'Ovasaray', 'Oymapınar', 'Palandöken', 'Palu', 'Pamukören', 'Pancar', 'Pazarcık', 'Paşalı', 'Pehlivanköy', 'Piribeyler', 'Polatlı', 'Polatlı YHT', 'Porsuk', 'Pozantı', 'Pınarbaşı', 'Pınarlı', 'Rahova', 'Sabuncupınar', 'Salat', 'Salihli', 'Sallar', 'Samsun', 'Sandal', 'Sandıklı', 'Sapanca', 'Sarayköy', 'Sarayönü', 'Saruhanlı', 'Sarıdemir', 'Sarıkamış', 'Sarıkent', 'Sarımsaklı', 'Sarıoğlan', 'Savaştepe', 'Sağlık', 'Sekili', 'Selçuk', 'Sevindik', 'Seyitler', 'Sincan', 'Sindirler', 'Sinekli', 'Sivas', 'Sivas(Adatepe)', 'Sivrice', 'Soma', 'Soğucak', 'Subaşı', 'Sudurağı', 'Sultandağı', 'Sultanhisar', 'Suluova', 'Susurluk', 'Suveren', 'Suçatı', 'Söke', 'Söğütlü Durak', 'Süngütaşı', 'Sünnetçiler', 'Sütlaç', 'Sıcaksu', 'Tanyeri', 'Tatvan Gar', 'Tavşanlı', 'Tayyakadın', 'Taşkent', 'Tecer', 'Tepeköy', 'Tokat(Yeşilyurt)', 'Topaç', 'Topdağı', 'Toprakkale', 'Topulyurdu', 'Torbalı', 'Turgutlu', 'Turhal', 'Tuzhisar', 'Tüney', 'Türkoğlu', 'Tınaztepe', 'Ulam', 'Uluköy', 'Ulukışla', 'Uluova', 'Umurlu', 'Urganlı', 'Uyanık', 'Uzunköprü', 'Uşak', 'Velimeşe', 'Vezirhan', 'Yahşihan', 'Yahşiler', 'Yakapınar', 'Yarbaşı', 'Yarımca YHT', 'Yayla', 'Yaylıca', 'Yazlak', 'Yazıhan', 'Yağdonduran', 'Yeni Karasar', 'Yenice', 'Yenice D', 'Yenifakılı', 'Yenikangal', 'Yeniköy', 'Yeniçubuk', 'Yerköy', 'Yeşilhisar', 'Yolçatı', 'Yozgat YHT', 'Yunusemre', 'Yurt', 'Yıldırımkemal', 'Yıldızeli', 'Zile', 'Çadırkaya', 'Çakmak', 'Çalıköy', 'Çamlık', 'Çankırı', 'Çardak', 'Çatalca', 'Çavundur', 'Çavuşcugöl', 'Çay', 'Çağlar', 'Çerikli', 'Çerkezköy', 'Çerkeş', 'Çetinkaya', 'Çiftehan', 'Çizözü', 'Çiğli', 'Çobanhasan', 'Çorlu', 'Çukurbük', 'Çukurhüseyin', 'Çumra', 'Çöltepe', 'Çöğürler', 'İhsaniye', 'İliç', 'İnay', 'İncirlik', 'İncirliova', 'İsabeyli', 'İshakçelebi', 'İsmetpaşa', 'İstanbul(Bakırköy)', 'İstanbul(Bostancı)', 'İstanbul(Halkalı)', 'İstanbul(Pendik)', 'İstanbul(Söğütlüçeşme)', 'İzmir (Basmane)', 'İzmit YHT', 'Şakirpaşa', 'Şarkışla', 'Şefaatli', 'Şefkat', 'Şehitlik', 'Şerbettar']


class RpaThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, parent=None, rpa_path="", data=None, password=None, to_email=None):
        super(RpaThread, self).__init__(parent)
        self.rpa_path = rpa_path
        self.data = data
        self.wdPID = None
        self.tools = Tools()
        self.password = password
        self.mail = to_email

    def run(self):
        availables_seats = ""
        try:
            self.rpa = RPA(self.data["from"], self.data["to"],
                           self.data["departure_date"], self.data["clock_start"],
                           self.data["clock_end"], str(self.data["exist_business"]), str(self.data["exist_disabled"]))
            availables_seats = self.rpa.runner()

            self.finished_signal.emit(str(availables_seats))

            try:
                if len(availables_seats[0]["ECONOMY"]) != 0 or len(availables_seats[0]["BUSINESS"]) != 0:
                    self.tools.sendEmail(password=self.password,
                                         to_email=self.mail, body=availables_seats, _from=self.data["from"], _to=self.data["to"])
            except:

                pass

        except:
            try:
                self.rpa.driver.close()
            except:
                pass

        self.run()

    def onKill(self):
        try:
            self.rpa.closeDriver()
        except:
            pass


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.from_list.addItems(istasyonList)
        self.ui.to_list.addItems(istasyonList)

        self.ui.search_from.textChanged.connect(self.searchInFromList)
        self.ui.search_to.textChanged.connect(self.searchInToList)
        self.ui.search_button.clicked.connect(self.runRPA)
        self.today = datetime.now().strftime("%d.%m.%Y")

        self.rpa_thread = None  # RpaThread nesnesini tanımlayın

    def searchInFromList(self):
        search_text = self.ui.search_from.toPlainText().lower()

        for i in range(self.ui.from_list.count()):
            item = self.ui.from_list.item(i)

            if search_text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def searchInToList(self):
        search_text = self.ui.search_to.toPlainText().lower()

        for i in range(self.ui.to_list.count()):
            item = self.ui.to_list.item(i)

            if search_text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def getData(self):
        _from = self.ui.from_list.selectedItems()[0].text(
        ) if self.ui.from_list.selectedItems() else None
        _to = self.ui.to_list.selectedItems()[0].text(
        ) if self.ui.to_list.selectedItems() else None
        _departure_date = self.ui.date.selectedDate().toString(
            "dd.MM.yyyy") if self.ui.date.selectedDate() else None
        _clock_start = self.ui.start_time.time().toString(
            "HH:mm") if self.ui.start_time.time() else None
        _clock_end = self.ui.end_time.time().toString(
            "HH:mm") if self.ui.end_time.time() else None

        _exist_business = True if self.ui.include_business.checkState() != 0 else False
        _not_exist_disabled = True if self.ui.include_disabled.checkState() != 0 else False

        self.mail = self.ui.mail.text()
        self.password = self.ui.password.text()

        return {
            "from": _from,
            "to": _to,
            "departure_date": _departure_date,
            "clock_start": _clock_start,
            "clock_end": _clock_end,
            "exist_business": _exist_business,
            "exist_disabled": _not_exist_disabled
        }

    def ProgressDialog(self):
        progress_dialog = QProgressDialog(
            "Proccess Started", None, 0, 0)
        progress_dialog.setWindowTitle("location is being searched...")
        progress_dialog.setCancelButton(QPushButton("Cancel"))
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.show()

        progress_dialog.canceled.connect(self.on_progress_canceled)
        return progress_dialog

    def runRPA(self):
        try:
            rpa_path = "src/rpa.py"
            data = self.getData()

            self.progress_dialog = self.ProgressDialog()

            if self.rpa_thread and self.rpa_thread.isRunning():
                self.rpa_thread.wait()

            self.rpa_thread = RpaThread(
                self, rpa_path, data, self.password, self.mail)
            self.rpa_thread.finished_signal.connect(
                self.on_rpa_thread_finished)
            self.rpa_thread.start()

        except:
            self.rpa_thread.terminate()
            self.rpa_thread.onKill()
            self.runRPA()

    def on_rpa_thread_finished(self, result):
        print(result)

    def on_progress_canceled(self):
        try:
            self.progress_dialog.accept()
            self.rpa_thread.terminate()
            self.rpa_thread.onKill()
        except:
            self.on_progress_canceled()


if __name__ == "__main__":
    QApp = QApplication([])
    window = Application()
    window.show()
    QApp.exec_()
