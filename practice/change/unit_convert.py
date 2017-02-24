"""
Unit Convert:
    Converts values from one unit to another.
"""
class ConversionClass:
    conversion_dictionary = {'in': 0.0254, 'mi': 0.000621371, 'ft': 3.28084, 'n.m.': .000539957}
    conversion_si = {None: 1,
                          'd': 1e-1, 'c': 1e-2, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12, 'f': 1e-15,
                          'a': 1e-18, 'z': 1e-21, 'y': 1e-24,
                          'da': 1e1, 'k': 1e3, 'h': 1e2, 'M': 1e6,
                          'G': 1e9, 'T': 1e12, 'P': 1e15, 'E': 1e18, 'Y': 1e24, 'Z': 1e21}

    def __init__(self):
        self.my_source_units = ''
        self.my_target_units = ''
        self.my_source_value = ''
        self.my_m_value = 0
        self.my_target_value = 0
    def __int__(self, source_units, target_units, my_source_value):
        self.my_source_units = source_units
        self.my_target_units = target_units
        self.my_source_value = my_source_value
        self.my_m_value = 0
        self.my_target_value = 0

    def convert_to_m(self):
        if (self.my_source_units[-1] == 'm'):
            if len(self.my_source_units == 2)
                return (self.my_source_value / self.conversion_si[self.my_source_units[0]])
            else:
                return (self.my_source_value / self.conversion_si[self.my_source_units[:1]])
        else:
            return (self.my_source_value / self.conversion_dictionary[self.my_source_units])

    def convert_from_m(self, input_number):

        return 0
    def parse_value(self, input_string):
        return 0
    def convert(self, in_value, target_unit):
        if (self.source_units != None and self.my_target_units != None and self.my_source_value != None):
            self.my_m_value = self.convert_to_m()
            self.my_target_value = self.convert_from_m(self.my_m_value)

def main():
    run_again_flag = True
    while (run_again_flag == True):
        in_value = input('Please input a distance to convert: ')
        target_unit = input('What unit would you like the output to be in?')
        conversion_object = ConversionClass()
        conversion_object.convert_from_m(in_value, target_unit)
        run_again = input('Run Again.')
        if run_again.lower()[:1] != 'y':
            run_again_flag = False


if __name__ == '__main__':
    main()