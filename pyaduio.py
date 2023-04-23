import sounddevice as sd
import pyaudio

print(sd.query_devices())
'''
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print (p.get_device_info_by_index(i))
    print("------------")
p.get_device_info_by_index(2)    
print(p.name)
'''


audio = pyaudio.PyAudio()

info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            if(audio.get_device_info_by_host_api_device_index(0, i).get('name')=='Stereo Karışımı (Realtek High D'):
                print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))