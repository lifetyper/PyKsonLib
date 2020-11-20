from PyKsonLib.models import KTHS_415BS

if __name__ == '__main__':
    p = KTHS_415BS("/dev/ttyUSB0")
    p.get_status()
