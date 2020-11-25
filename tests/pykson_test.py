from PyKsonLib.models import KTHS_415BS

if __name__ == '__main__':
    p = KTHS_415BS("/dev/ttyUSB0")
    if not p.power_status:
        print("not power on")
    p.get_status()
    p_list = p.list_all_pgm()
    p.load_pgm('-40.pgm')
    p.get_status()
    p.stop()
    p.close()
