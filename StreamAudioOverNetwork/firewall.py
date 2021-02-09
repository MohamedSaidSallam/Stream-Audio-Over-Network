from subprocess import Popen


def toggleFirewall(port):
    Popen(f"firewall.bat {port}")