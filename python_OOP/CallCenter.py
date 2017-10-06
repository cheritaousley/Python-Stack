class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id=unique_id
        self.caller_name=caller_name
        self.caller_phone_number=caller_phone_number
        self.time_of_call=time_of_call
        self.reason_for_call=reason_for_call
    def display_all(self):
        print "Incoming call from", self.unique_id, self.caller_name, self.caller_phone_number, "at", self.time_of_call, "concerning", self.reason_for_call
class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue_size=0
    def add_call(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        new_call=Call(unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call)
        self.call_list.append(new_call)
        self.queue_size=len(self.call_list)
    def remove_call(self,name):
        for x in self.call_list:
            if x.caller_name == name:
                y=self.call_list.index(x)
                del self.call_list[y]
                print "I am being removed"
    def info_call(self):
        for thing in self.call_list:
            print thing.caller_name, thing.caller_phone_number, self.queue_size
# first_caller=Call("jdoe", "Jane Doe", "773-777-9999", "8am", "complaint about service")
# second_caller=Call("pdoe", "Pat Doe", "773-888-0000", "9am", "compliment")
# first_caller.display_all()
# second_caller.display_all()

Cleo_callline=CallCenter()
Cleo_callline.add_call("jdoe", "Jane Doe", "773-777-9999", "8am", "complaint about service")
# Cleo_callline.info_call()
# Cleo_callline.add_call("pdoe", "Pat Doe", "773-888-0000", "9am", "compliment")
# Cleo_callline.info_call()
# Cleo_callline.add_call("jww", "Jen Wlee", "773-999-1111", "10am", "referral")
Cleo_callline.info_call()
Cleo_callline.remove_call("Jane Doe")