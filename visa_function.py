import pyvisa as visa

rm=visa.ResourceManager()

def get_visa_resource_list():
    device_list=rm.list_resources()

    return device_list

def create_visa_equipment(resource_name):
    equipment=rm.open_resource(resource_name)

    return equipment

if __name__ == '__main__':

    devices=get_visa_resource_list()
    escope=create_visa_equipment(devices[1])
    print(escope.query('*IDN?'))
