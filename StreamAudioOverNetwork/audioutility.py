import pyaudio

p = pyaudio.PyAudio()


def getValidDevicesList():
    output = []
    for i in range(p.get_device_count()):
        currentDevice = p.get_device_info_by_index(i)
        isInput = currentDevice["maxInputChannels"] > 0
        isWASAPI = (p.get_host_api_info_by_index(
            currentDevice["hostApi"])["name"]).find("WASAPI") != -1
        if isWASAPI and not isInput:
            output.append((i, currentDevice['name']))
    return output


def getDeviceInfoString(deviceIndex):
    device = p.get_device_info_by_index(deviceIndex)
    return f"""Device Name: {device['name']}\nDevice Index: {device['index']}\nSample Rate: {device['defaultSampleRate']}"""
