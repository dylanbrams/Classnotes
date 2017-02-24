"""
Unit Convert:
    Converts values from one unit to another.
"""
class ConversionClass:
    """

        >>> t=ConversionClass()
        >>> t.convert(1, 'm', 'mi')
        1.0 m is 0.0006213727366498068 mi
        >>> t.convert(2343221.12, 'in', 'km')
        2343221.12 in is 59.517816448 km
        >>> t.convert(2323.12, 'n.m.', 'cm')
        2323.12 n.m. is 430241824.0 cm
        >>> t.convert(231.12, 'nm', 'pm')
        231.12 nm is 231120.00000000003 pm
        >>> t.convert(15851.12, 'um', 'fm')
        15851.12 um is 15851119999999.998 fm

    """
    conversion_dictionary = {'in': 0.0254, 'mi': 1609.34, 'ft': 0.3048, 'n.m.': 1852}
    conversion_si = {None: 1,
                          'd': 1e-1, 'c': 1e-2, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12, 'f': 1e-15,
                          'a': 1e-18, 'z': 1e-21, 'y': 1e-24,
                          'da': 1e1, 'k': 1e3, 'h': 1e2, 'M': 1e6,
                          'G': 1e9, 'T': 1e12, 'P': 1e15, 'E': 1e18, 'Y': 1e24, 'Z': 1e21}

    def __init__(self):
        self.source_units = ''
        self.target_units = ''
        self.source_value = ''
        self.m_value = 0
        self.target_value = 0
    def __int__(self, source_units, target_units, my_source_value):
        self.source_units = source_units
        self.target_units = target_units
        self.source_value = my_source_value
        self.m_value = 0
        self.target_value = 0

    def convert_to_m(self):
        if (self.source_units[-1] == 'm'):
            if len(self.source_units) == 2:
                return (self.source_value * self.conversion_si[self.source_units[0]])
            elif len(self.source_units) == 1:
                return self.source_value
            else:
                return (self.source_value * self.conversion_si[self.source_units[:1]])
        else:
            return (self.source_value * self.conversion_dictionary[self.source_units])

    def convert_from_m(self):
        if (self.target_units[-1] == 'm'):
            if len(self.target_units) == 2:
                return (self.m_value / self.conversion_si[self.target_units[0]])
            elif len(self.target_units) == 1:
                return self.m_value
            else:
                return (self.m_value / self.conversion_si[self.target_units[:1]])
        else:
            return (self.source_value / self.conversion_dictionary[self.target_units])

    def parse_value(self, input_string):
        return 0

    def print_results(self):
        """
        Prints out the results of conversion.
        :return:
        """
        print (str(self.source_value) + " " + self.source_units + " is " + str(self.target_value) + " " + self.target_units)

    def convert(self, in_value, source_unit, target_unit):
        '''
        Converts
        :param in_value:
        :param source_unit:
        :param target_unit:
        :return:

        '''
        self.source_value = float(in_value)
        self.source_units = source_unit
        self.target_units = target_unit
        if (self.source_units != None and self.target_units != None and self.source_value != None):
            self.m_value = self.convert_to_m()
            self.target_value = self.convert_from_m()
        self.print_results()


def main():
    run_again_flag = True
    while (run_again_flag == True):
        in_value = input('Please input a distance to convert: ')
        source_unit = input('What unit is this input in?')
        target_unit = input('What unit would you like the output to be in?')
        conversion_object = ConversionClass()
        conversion_object.convert(in_value, source_unit, target_unit)
        run_again = input('Run Again.')
        if run_again.lower()[:1] != 'y':
            run_again_flag = False


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(extraglobs={'t': ConversionClass()})