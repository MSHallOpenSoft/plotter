from PyQt4.QtCore import QThread, SIGNAL
from threading import Thread
import time
class MyThread(QThread):
    def on_thread_finished(self, thread, data):
        pass
    def __init__(self, parent=None):
        QThread.__init__(self)
        self.parent = parent
        self.threadlinks=[]
        self.data=0
    def plot3d(self,**kwargs):
        self.data=kwargs
        self.start()
    def run(self):
        #time.sleep(5)
        print("inpuuuuuuuuuuuuuuuuuuuuuuut in thread")
        self.parent.parent.parent.mayavi_widget.visualization.mayavi_implicit_3d(**self.data)
        print("thread finished")
        self.emit(SIGNAL('finished'))

if __name__ == '__main__':
    print("not executable")
 

