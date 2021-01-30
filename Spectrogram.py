#Spectrogram
#Author: Renata Wietrzyńska

import tkinter as tk
from tkinter import filedialog

import sounddevice as sd

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar
matplotlib.use('TKAgg')
from scipy import signal
from scipy.io import wavfile

global root

class GUI(tk.Frame):

    def recordSave(self, fs, s):
        tk.messagebox.showinfo(title="Record", message="Please speak for 5sec to record")

        nagranie = sd.rec(int(fs * s), samplerate=fs, channels=2)
        sd.wait()

        files = [('WAV Files', '*.wav')]
        filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        filename = filedialog.askopenfilename(initialdir=None, title="Select file", filetypes=(("plikiWav", "*.wav"),))

        if filename:
            wavfile.write(filename=filename, rate=fs, data=nagranie)

        self.drawSpectrogram(filename)
        self.drawSoundWave(filename)

    def drawSpectrogram(self, filename):
        sample_rate, samples = wavfile.read(filename)

        n_channel = samples.shape
        data = None

        if len(n_channel) == 1:
            data = samples[:]
        else:
            data = samples[:, 0]

        frequencies, times, spectrogram = signal.spectrogram(data, sample_rate, nfft=1024, noverlap=900, nperseg=1024)

        fig = Figure(linewidth=0, edgecolor='#000000')
        a = fig.add_subplot(111)
        a.pcolormesh(times, frequencies, 10**(-10)*(spectrogram), shading='auto')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().place(x=30, y=0, width=700, height=390)

        a.set_ylabel('Frequency [Hz]')
        a.set_xlabel('Time [sec]')

        canvas.draw()

        toolbar = NavigationToolbar(canvas, root)
        toolbar.update()
        toolbar.place(x=10, y=400)

    def drawSoundWave(self, filename):
        rate, data = wavfile.read(filename)

        if len(data.shape) == 1:
            channel1 = data[:]
        else:
            channel1 = data[:, 0]

        fig = Figure(linewidth=0, edgecolor='#000000')

        a = fig.add_subplot(111)
        a.plot(channel1, color='black')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().place(x=10, y=450, width=750, height=200)
        canvas.draw()

        toolbar = NavigationToolbar(canvas, root)
        toolbar.update()
        toolbar.place(x=10, y=650)

        fig.tight_layout()

    def open(self):
        filename = filedialog.askopenfilename(initialdir=None, title="Select file", filetypes=(("plikiWav", "*.wav"),))

        self.drawSpectrogram(filename)
        self.drawSoundWave(filename)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        menubar = tk.Menu(self)

        submenu1 = tk.Menu(menubar, tearoff=0)

        submenu1.add_command(label="Open", command=lambda: self.open())
        submenu1.add_command(label="Record & Save", command=lambda: self.recordSave(4410, 5))

        menubar.add_cascade(label="File", menu=submenu1)

        self.parent.config(menu=menubar)

        self.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Spectrogram")
    root.geometry('800x700')
    root.resizable(False, False)
    app = GUI(root)
    root.mainloop()