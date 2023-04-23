from email.mime import audio
import sounddevice as sd
import speech_recognition as sr
import pydub

pydub.AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"

text_file = open("test_speaker.txt","w")
r = sr.Recognizer()#tanıma işi burada olacak

print(sd.query_devices()) # bütün ses i/o cihazlarını listeliyor

sd.default.device[0] = 2 #hoparlrü seçip default ayarlıyrıuz
fs = 44100 #frekans
length = 10 #süre
recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1) #reocr ediyr
sd.wait()
from scipy.io import wavfile
wavfile.write('test.wav',fs,recording) # recordu verilen isimle aynı dizine kayıt ediyor
sound = pydub.AudioSegment.from_wav("test.wav").export("test1.wav", format="wav") #mp3 çeviriyor
file = sr.AudioFile('test1.wav')#file ptr içine ses doyası atılıyor

with file as source:
    r.adjust_for_ambient_noise(source) #??
    audio = r.record(source) # ses dosyasını kayıt ediyoruz
    result = r.recognize_google(audio,language='tr')#kaydı google apiye yollama
    text_file.write(result)#dosyaya yazma

   # ``