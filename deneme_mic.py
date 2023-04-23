import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=5) #mikrofonu kaynak olarak belrileyip 5 sn dinleme yapıyor
    print("sesinizi dinliyor")
    text_file = open("test.txt","w") #aynı dizinedeki dosyaya yazma
    text_file2 = open(r"C:\Users\MonsterPC\Desktop\test2.txt","w") # başka dizindeki dosyaya yazma
    try:
        text = r.recognize_google(data,language='tr') #google recognition apisine erişiyor
        text_file.write(text)
        text_file2.write(text)
        print(text)
    except:
        print("ses bulunamadı")