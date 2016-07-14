from tkinter import *
import threading
import cpuinfo.cpuinfo as cpuinfo
import psutil


class pyMonitor:
    def storageRender(self):
        def storage():
            try:
                storageFreeLabel.configure(text="Disk(0) Free: " + str(psutil.disk_usage("/").free) + " Bytes")
                storageUsedLabel.configure(text="Disk(0) Used: " + str(psutil.disk_usage("/").used) + " Bytes")
                storagePercentLabel.configure(text="Disk(0) Total: " + str(psutil.disk_usage("/").percent) + "%")
                threading.Timer(1, storage)
            except:
                pass
        storageUsageLabel = Label(self.storageFrame,
                                  text="Disk(0) Total: " + str(psutil.disk_usage("/").total) + " Bytes")
        storageUsedLabel = Label(self.storageFrame,
                                  text="Disk(0) Used: " + str(psutil.disk_usage("/").used) + " Bytes")
        storageFreeLabel = Label(self.storageFrame,
                                 text="Disk(0) Free: " + str(psutil.disk_usage("/").free) + " Bytes")
        storagePercentLabel = Label(self.storageFrame,
                                 text="Disk(0) Used: " + str(psutil.disk_usage("/").percent) + "%")

        storageUsageLabel.pack()
        storageUsedLabel.pack()
        storageFreeLabel.pack()
        storagePercentLabel.pack()

        storageThread = threading.Thread(target=storage, name="storage", daemon=True)
        storageThread.start()

    def ramRender(self):
        def usedRam():
            try:
                usedRamLabel.configure(text="Used RAM: " + str(psutil.virtual_memory().used) + " Bytes")
                avaailableRamLabel.configure(text="Available RAM: " + str(psutil.virtual_memory().available) + " Bytes")
                percentRamLabel.configure(text="Used RAM: " + str(psutil.virtual_memory().percent) + "%")
                threading.Timer(1, usedRam).start()
            except:
                pass

        totalRamLabel = Label(self.ramFrame, text="Total RAM: " + str(psutil.virtual_memory().total) + " Bytes")
        usedRamLabel = Label(self.ramFrame, text="Used RAM: " + str(psutil.virtual_memory().used) + " Bytes")

        avaailableRamLabel = Label(self.ramFrame,
                                   text="Available RAM: " + str(psutil.virtual_memory().available) + " Bytes")
        percentRamLabel = Label(self.ramFrame,
                                text="Used RAM: " + str(psutil.virtual_memory().percent) + "%")

        totalRamLabel.pack()
        usedRamLabel.pack()
        avaailableRamLabel.pack()
        percentRamLabel.pack()

        usedRamThread = threading.Thread(target=usedRam, name="usedRam", daemon=True)
        usedRamThread.start()

    def cpuRender(self):
        def getUsage():
            try:
                cpuPercentLabel.configure(text="Usage: " + str(psutil.cpu_percent(interval=1)) + "%")
                threading.Timer(1, getUsage).start()
            except:
                pass

        cpuName = cpuinfo.get_cpu_info()["brand"]
        cpuNameLabel = Label(self.cpuFrame, text="Name: " + cpuName)

        cpuFreqActual = cpuinfo.get_cpu_info()["hz_actual"]
        cpuFreqActualLabel = Label(self.cpuFrame, text="Actual Speed: " + cpuFreqActual)

        cpuCoreCount = cpuinfo.get_cpu_info()["count"]
        cpuCoreCountLabel = Label(self.cpuFrame, text="Cores: " + str(cpuCoreCount))

        cpuPercentLabel = Label(self.cpuFrame, text="Usage: " + str(psutil.cpu_percent()) + "%")

        cpuNameLabel.pack()
        cpuFreqActualLabel.pack()
        cpuCoreCountLabel.pack()
        cpuPercentLabel.pack()
        getUsageThread = threading.Thread(target=getUsage, name="getUsage", daemon=True)
        getUsageThread.start()

    def createContainers(self):
        self.storageFrame = LabelFrame(self.window, text="Storage")
        self.ramFrame = LabelFrame(self.window, text="RAM")
        self.cpuFrame = LabelFrame(self.window, text="CPU")

        self.storageFrame.pack(side=LEFT, expand=YES, fill=BOTH)
        self.ramFrame.pack(side=LEFT, expand=YES, fill=BOTH)
        self.cpuFrame.pack(side=LEFT, expand=YES, fill=BOTH)

        cpuRenderThread = threading.Thread(target=self.cpuRender, name="cpuRender", daemon=True)
        cpuRenderThread.start()

        ramRenderThread = threading.Thread(target=self.ramRender, name="ramRender", daemon=True)
        ramRenderThread.start()

        storageRenderThread = threading.Thread(target=self.storageRender, name="storageRender", daemon=True)
        storageRenderThread.start()

    def __init__(self, master):
        self.window = Toplevel(master)
        self.window.title("pyMonitor")
        # self.window.geometry("800x400")

        containerThread = threading.Thread(target=self.createContainers, name="createContainers", daemon=True)
        containerThread.start()

        self.window.mainloop()