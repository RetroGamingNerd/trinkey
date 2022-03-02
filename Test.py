import time
import board
import adafruit_mcp9808

i2c = board.I2C()  # uses board.SCL and board.SDA

# To initialise using the default address:
mcp = adafruit_mcp9808.MCP9808(i2c)

# To initialise using a specified address:
# Necessary when, for example, connecting A0 to VDD to make address=0x19
# mcp = adafruit_mcp9808.MCP9808(i2c_bus, address=0x19)

gender = input("What would you like to do? ")
gender = gender.lower()
if gender == "check temp":
    for i in range(5):
        print()
        print("Reading", i+1)
        tempC = mcp.temperature
        tempF = tempC * 9 / 5 + 32
        print("Temperature: {} C {} F ".format(tempC, tempF))
        time.sleep(2)
elif gender == "female":
    print("Your cat is female")
else:
    print("Invalid input")

age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")
