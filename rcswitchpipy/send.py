#!/usr/bin/python

import sys
import rcswitch

PIN = 0
LED = 1

def main(argv):
  switch = rcswitch.RCSwitch()
  switch.enableTransmit(PIN)
  #switch.enableLEDNotify(LED)

  system_code = argv[1]
  unit_code = argv[2]

  command = int(argv[3])

  if(len(unit_code)==1):
	unit_code=int(unit_code)

  if(len(system_code)==1):
	system_code=int(system_code)

  print 'sending systemCode[%s] unitCode[%s] command[%i]' % (system_code, str(unit_code), command)

  if command == 0:
      switch.switchOff(system_code,unit_code)
  elif command == 1:
      switch.switchOn(system_code,unit_code)

if __name__ == '__main__':
  main(sys.argv)
