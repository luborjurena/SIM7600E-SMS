# https://pypi.org/project/pyserial/
import time,argparse,serial

parser = argparse.ArgumentParser(description='This script is going to read and delete your messages from SIM7600 modem.')
parser.add_argument('--delete', help='Delete all read messages')

next_line = 0

with serial.Serial(port='/dev/ttyUSB2', baudrate=115200, timeout=5) as ser:
    ser.write(b'AT\r')
    time.sleep(0.5)
    ser.write(b'AT+CPMS=\"SM\"\r')
    time.sleep(0.5)
    ser.write(b'AT+CMGL=\"ALL\"\r')
    for i in ser.readlines():
            message = i.decode('utf-8', 'ignore')
            message = str(message)
            if ('CMGL' in message) or next_line == 1:
                    print(message)
                    next_line = 1
            else:
                    next_line = 0

    args = vars(parser.parse_args())
    try:
        if args["delete"] == '1':
                ser.write(b'AT+CMGD=,3\r')
                time.sleep(0.5)
                print('All read messages deleted.')
        else:
                pass
    except KeyError:
        pass
