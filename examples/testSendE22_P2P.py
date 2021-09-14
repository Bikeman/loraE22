# Simple test program for loraE22 transmitter
# based on https://github.com/effevee/loraE32

###########################################
# sending fixed point to point
###########################################
# transmitter - address 0001 - channel 02
# receiver    - address 0003 - channel 04
###########################################

from loraE22 import ebyteE22
import utime

M0pin = 25
M1pin = 26
AUXpin = 14

e22 = ebyteE22(M0pin, M1pin, AUXpin, Address=0x0001, Channel=0x02, debug=False)

e22.start()

to_address = 0x0003
to_channel = 0x04
message = "HELLO WORLD "

teller = 0
while True:
    message = { 'msg': 'HELLO WORLD %s'%str(teller) }
    print('Sending fixed P2P: address %d - channel %d - message %s'%(to_address, to_channel, message))
    e22.sendMessage(to_address, to_channel, message, useChecksum=True)
    teller += 1
    utime.sleep_ms(2000)

e22.stop()
