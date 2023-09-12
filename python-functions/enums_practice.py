from enum import Enum

# class syntax
class ApplicationType(Enum):
  hybrid = 1
  remote = 2
  onsite = 3

# for item in ApplicationType:
#   print(item)

# functional syntax
FuncApplicationType = Enum('ApplicationType', ['hybrid', 'remote', 'onsite'])

# print(ApplicationType.hybrid)

for type in ApplicationType:
  print(type.value)