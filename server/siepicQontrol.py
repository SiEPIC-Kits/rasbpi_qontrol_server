##
#Author: Stephen
##

channel = 0

import qontrol

class siepicqontrol:
    def connect(self, serial_port_name="/dev/ttyUSB0"):
        # Setup Qontroller
        q = qontrol.QXOutput(serial_port_name = serial_port_name, response_timeout = 0.1)
        print ("Qontroller '{:}' initialised with firmware {:} and {:} channels".format(q.device_id, q.firmware, q.n_chs) )
        return q

    def set_voltage(self, q, channel=0, volts=0):
        q.v[channel] = volts
        reply_string=("Channel "+str(channel)+". Voltage set to: "+ str(volts)+"V.")
        return reply_string

    def set_current(self, q, channel=0, current=0):
        q.i[channel] = current
        reply_string=("Channel "+str(channel)+". Current set to: "+ str(current)+"A.")
        return reply_string

    def get_voltage(self,q,channel=0):
        meas_voltage = q.v[channel]
        reply_string=("Channel "+str(channel)+". Voltage is: "+ str(meas_voltage)+"V.")
        return reply_string

    def get_current(self,q,channel=0):
        meas_current = q.i[channel]
        reply_string=("Channel "+str(channel)+". Current is: "+ str(meas_current)+"A.")
        return reply_string

    def reset_voltage(self,q,channel=0):
        q.v[channel] = 0
        reply_string=("Channel "+str(channel)+". Voltage Reset to 0V.")
        return reply_string

    def reset_current(self,q,channel=0):
        q.i[channel] = 0
        reply_string=("Channel "+str(channel)+". Current Reset to 0A.")
        return reply_string

    def reset_voltage_all(self,q):
        q.v[:] = 0
        reply_string=("All Channels. Voltage Reset to 0V.")
        return reply_string

    def reset_current_all(self,q):
        q.i[:] = 0
        reply_string=("All Channels. Current Reset to 0A.")
        return reply_string

    def reset_voltage_range(self,q,channel1=0,channel2=1):
        q.v[channel1:channel2] = 0
        reply_string=("Channel "+str(channel1)+" to Channel "+str(channel2)+ ". Voltage Reset to 0V.")
        return reply_string

    def reset_current_range(self,q,channel1=0,channel2=1):
        q.i[channel1:channel2] = 0
        reply_string=("Channel "+str(channel1)+" to Channel "+str(channel2)+ ". Current Reset to 0A.")
        return reply_string

    def disconnect(self,q):
        q.close()
        reply_string=("Disconnect.")
        return reply_string

    def test_command(self):
        reply_string = 'This is a Test Command.'
        return reply_string

# =============================================================================
# # Set voltage on each channel to its index in volts, read voltage, current
# for channel in range(q.n_chs):
# 	set_voltage = channel
#
# 	# Set voltage
# 	q.v[channel] = set_voltage
#
# 	# Measure voltage (Q8iv)
# 	measured_voltage = q.v[channel]
#
# 	# Measure current (Q8iv, Q8b, Q8)
# 	measured_current = q.i[channel]
#
# 	print ("Channel {:} set to {:} V, measured {:} V and {:} mA".format(channel, set_voltage, measured_voltage, measured_current) )
#
#
# =============================================================================
# Set all channels to zero
#q.v[:] = 0
