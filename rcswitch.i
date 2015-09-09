%module rcswitch

%{
#define SWIG_FILE_WITH_INIT
#include "RCSwitch.h"
%}

class RCSwitch
{
public:
	RCSwitch();
	void enableTransmit(int nTransmitterPin);
	void disableTransmit();
	void enableLEDNotify(int ledpin);
	void switchOn(char* sGroup , int nSwitchNumber);
        void switchOff(char* sGroup , int nSwitchNumber);
	void switchOn(char* sGroup, char* sDevice);
	void switchOff(char* sGroup, char* sDevice);
	void send(unsigned long Code, unsigned int length);
};
%init %{
  if (wiringPiSetup () == -1) return;
  %}
