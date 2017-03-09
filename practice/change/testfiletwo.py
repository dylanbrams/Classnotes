# class RainMeasurement:
#     def __init__(self, date, amount_inches):
#         self.date = date
#         self.amount_inches = amount_inches
#
# rain_measurements = [
#     RainMeasurement("2016-01-01", 0.5),
#     RainMeasurement("2016-01-02", 0.25),
#     RainMeasurement("2016-01-03", 0.75),
# ]
#
# for measurement in rain_measurements:
#     print (measurement.date)
#     print (measurement.amount_inches)
#

class AddressBookEntry:
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

  def __eq__(self, other_entry):
    return (
      self.name == other_entry.name and
      self.phone_number == other_entry.phone_number and
      id(self) == id(other_entry)
    )

me = AddressBookEntry('David', '503-555-9895')
you = AddressBookEntry('Helen', '503-555-2131')
thisguy = AddressBookEntry('Helen', '503-555-2131')

# These two lines run the same code:
print(me == you)  #> False
print(AddressBookEntry.__eq__(me, you))  #> False

print(str(id(you)) + '  ' + str(id(thisguy)))
print(you == thisguy)
print(AddressBookEntry.__eq__(you, thisguy))
