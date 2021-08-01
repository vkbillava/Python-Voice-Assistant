import time
from record import get_audio
from response import response


while(1):
    voice_data = get_audio("Recording")
    print("Done")
    print("Q:", voice_data)
    response(voice_data)