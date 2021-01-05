import tkinter as tk
import sounddevice as sd
import soundfile as sf

#nowe importy
import matplotlib
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
matplotlib.use('TKAgg') #wazne
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GUI(tk.Frame):
    def fun(self, arg1):
        print("test"+str(arg1))

    def nagraj(self, fs, s):
        from scipy.io.wavfile import write
        #fs = 44100  # probki 1/s
        #s = 3
        self.btn3['state'] = 'normal'
        nagranie = sd.rec(int(fs * s), samplerate=fs, channels=2)
        sd.wait()
        write("pliczek.wav", fs, nagranie)
        sd.play(nagranie, fs)
        sd.wait()

    def wczytaj(self, e):
        filename = e
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        sd.wait()  # Wait until file is done playing

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        menubar = tk.Menu(self)

        submenu1 = tk.Menu(menubar, tearoff=0)
        submenu1.add_command(label="Test 1", command=lambda:self.fun(10))
        submenu1.add_command(label="Test 2", command=lambda: self.fun(10))
        submenu1.add_command(label="Test 3", command=lambda: self.fun(10))

        menubar.add_cascade(label="Plik", menu=submenu1)

        submenu2 = tk.Menu(menubar, tearoff=0)
        submenu2.add_command(label="Test 1", command=lambda: self.fun(10))
        submenu2.add_command(label="Test 2", command=lambda: self.fun(10))
        submenu2.add_command(label="Test 3", command=lambda: self.fun(10))

        menubar.add_cascade(label="Edycja", menu=submenu2)

        submenu3 = tk.Menu(menubar, tearoff=0)
        submenu3.add_command(label="Test 1", command=lambda: self.fun(10))
        submenu3.add_command(label="Test 2", command=lambda: self.fun(10))
        submenu3.add_command(label="Test 3", command=lambda: self.fun(10))

        menubar.add_cascade(label="Wyswietlacz", menu=submenu3)

        submenu4 = tk.Menu(menubar, tearoff=0)
        submenu4.add_command(label="Test 1", command=lambda: self.fun(10))
        submenu4.add_command(label="Test 2", command=lambda: self.fun(10))
        submenu4.add_command(label="Test 3", command=lambda: self.fun(10))

        menubar.add_cascade(label="Widok", menu=submenu2)

        self.parent.config(menu=menubar)

        lbl = tk.Label(self, text="Widok pliku", anchor=tk.W)
        lbl.place(x=0, y=0, width=100, height=25)

        display = tk.Label(self, text=None, background="white", anchor=tk.W)
        display.place(x=30, y=30, width=400, height=200)

        lbl2 = tk.Label(self, text="Spektrogram", anchor=tk.W)
        lbl2.place(x=0, y=240, width=100, height=25)

        display2 = tk.Label(self, text=None, background="white", anchor=tk.W)
        display2.place(x=30, y=270, width=400, height=200)

        btn1 = tk.Button(self, text="Start", command=lambda: self.fun(1), state=tk.ACTIVE)
        btn1.place(x=480, y=50, width=70, height=30)

        btn2 = tk.Button(self, text="Stop", command=lambda: self.fun(2), state=tk.ACTIVE)
        btn2.place(x=550, y=50, width=70, height=30)

        # lbl3 = tk.Label(self, text="Plik do zapisania:")
        # lbl3.place(x=430, y=100, width=100, height=50)
        #
        # e1 = tk.Entry(self)
        # e1.place(x=530, y=110, width=100, height=20)

        self.btn3 = tk.Button(self, text="Nagraj", command=lambda: self.nagraj(4410, 2), state=tk.ACTIVE)
        self.btn3.place(x=630, y=110, width=100, height=20)

        lbl4 = tk.Label(self, text="Plik do wczytania: ")
        lbl4.place(x=430, y=140, width=100, height=50)

        e2 = tk.Entry(self)
        e2.place(x=530, y=150, width=100, height=20)

        btn4 = tk.Button(self, text="Wczytaj", command=lambda: self.wczytaj(e2.get()), state=tk.ACTIVE)
        btn4.place(x=630, y=150, width=100, height=20)

        self.pack(side="top", fill="both", expand=True)

        #wykresiki:
        """
        rate, data = wav.read('test.wav')
        channel1 = data[:, 0]

        fig = Figure(linewidth=5, edgecolor='#000000')
        a = fig.add_subplot(111)
        a.plot(channel1, color='black')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().place(x=10, y=50, width=700, height=200)
        canvas.draw()

        #a.invert_yaxis()
        a.set_title("test")
        a.set_ylabel('test y')
        a.set_xlabel('test x')
        #a.axis('off')
        a.set_yticklabels([])
        a.set_xticklabels([])
        fig.tight_layout()

        fig2 = Figure(linewidth=5, edgecolor='#000000')
        a = fig2.add_subplot(111)
        a.plot(channel1, color='black')

        canvas = FigureCanvasTkAgg(fig2, master=self)
        canvas.get_tk_widget().place(x=10, y=250, width=700, height=200)
        canvas.draw()

        #a.invert_yaxis()
        a.set_title("test")
        a.set_ylabel('test y')
        a.set_xlabel('test x')
        #a.axis('off')
        a.set_yticklabels([])
        a.set_xticklabels([])
        fig2.tight_layout()
        self.pack(side="top", fill="both", expand=True)
        """

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Spektrogram")
    root.geometry('720x480')
    root.resizable(False, False)
    app = GUI(root)
    root.mainloop()

    """
    plt.figure(figsize=(7, 7), dpi=100)
    plt.subplot(3, 3, 1)
    plt.subplot(3, 3, 9)
    plt.subplot(2, 2, 2)
    plt.show()
    """



    """
    rate, data = wav.read('test.wav')
    print(type(rate))
    print(type(data))
    print(data.shape[0])
    print(data.shape[1])

    channel1 = data[:,0]
    channel2 = data[:,1]

    plt.plot(channel2)
    plt.show()
    """

    """
    plt.figure(figsize=(7,7), dpi=100)
    plt.subplot(3,3,1)
    plt.subplot(3,3,9)
    plt.subplot(2,2,2)
    plt.show()
    """





    #grid, place, pack, tk.Button, tk.Lablel, tk.Menu
    #otworzymy pliczek

    """
    import soundfile as sf
    import sounddevice as sd

    filename1 = "BabyElephantWalk60.wav"
    filename2 = "StarWars60.wav"

    data, fs = sf.read(filename2, dtype='float32')
    print(data)
    print(fs)

    sd.play(data, fs)
    sd.wait()

    print("koniec")
    """

    #nagrywamy pliczek

    """
    import sounddevice as sd
    from scipy.io.wavfile import write

    fs = 44100 #probki 1/s
    s = 3

    nagranie = sd.rec(int(fs*s), samplerate=fs, channels=2)
    sd.wait()

    #write("test.wav", fs, nagranie)

    sd.play(nagranie, fs)
    sd.wait()

    print("koniec")
    """

    #polaczymy pliki
    """
    import soundfile as sf

    filename1 = "BabyElephantWalk60.wav"
    filename2 = "StarWars60.wav"

    data, fs = sf.read(filename1, dtype='float32')
    print(fs)
    data, fs = sf.read(filename2, dtype='float32')
    print(fs)

    import wave

    files = [filename1, filename2]
    outputfile ="test2.wav"

    data = []
    for file in files:
        # w = wave.open(file, "rb")
        # w.close()
        with wave.open(file, "rb") as w:
            data.append([w.getparams(), w.readframes(w.getnframes())])

    with wave.open(outputfile, "wb") as output:
        output.setparams(data[0][0])
        for i in range(len(data)):
            output.writeframes(data[i][1])
            """






