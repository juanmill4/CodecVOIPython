
class Codecs(): #Creamos la clase Codecs

    def __init__ (self, name, CBR, CDS, CSI, MOS, VPSb, VPSs, PPS, BWmp, BWcRTP, BWethernet): #Definimos el constructor
        self.name_ = name
        self.CBR_ = CBR
        self.CDS_ = CDS
        self.CSI_ = CSI
        self.MOS_ = MOS
        self.VPSb_ = VPSb
        self.VPSs_ = VPSs
        self.PPS_ = PPS
        self.BWmp_ = BWmp
        self.BWcRTP_ = BWcRTP
        self.BWethernet_ = BWethernet


    def getName(self):
        return self.name_
    
    def getCBR(self):
        return self.CBR_

    def getCDS(self):
        return self.CDS_

    def getCSI(self):
        return self.CSI_

    def getMOS(self):
        return self.MOS_

    def getVPSb(self):
        return self.VPSb_

    def getVPSs(self):
        return self.VPSs_

    def getPPS(self):
        return self.PPS_

    def getBWmp(self):
        return self.BWmp_

    def getBWcRTP(self):
        return self.BWcRTP_

    def getBWethernet(self):
        return self.BWethernet_

    def __repr__(self):
        return str(self.__dict__)


def lista_Codecs():
    list = []

    list.append(Codecs('G711', 64, 80, 10, 4.1, 160, 20, 50, 82.8, 67.6, 87.2))
    list.append(Codecs('G729', 8, 10, 10, 3.92, 20, 20, 50, 26.8, 11.6, 31.2))
    list.append(Codecs('G723.1-6.3Kbps', 6.3, 24, 30, 3.9, 24, 30, 33.3, 18.9, 8.8, 21.9))
    list.append(Codecs('G723.1-5.3Kbps', 5.3, 20, 30, 3.8, 20, 30, 33.3, 17.9, 7.7, 20.8))
    list.append(Codecs('G726-32Kbps', 32, 20, 5, 3.85, 80, 20, 50, 50.8, 35.6, 55.2))
    list.append(Codecs('G726-24Kbps', 24, 15, 5, 0, 0, 20, 50, 42.8, 27.6, 47.2))
    list.append(Codecs('G728', 16, 10, 5, 3.61, 60, 30, 33.3, 28.5, 18.4, 31.5))
    list.append(Codecs('G722_64k', 64, 80, 10, 4.13, 160, 20, 50, 82.8, 67.6, 87.2))
    list.append(Codecs('ilbc_mode_20', 15.2, 38, 20, 0, 38, 20, 50, 34, 18.8, 38.4))
    list.append(Codecs('ilbc_mode_30', 13.33, 50, 30, 0, 50, 30, 33.3, 25867, 15.73, 28.8))

    return list


