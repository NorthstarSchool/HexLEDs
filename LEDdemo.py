from adafruit.Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight
import time

PATTERN_N = [0x81, 0x83, 0x85, 0x89, 0x91, 0xA1, 0xC1, 0x81]
PATTERN_A = [0x81, 0x81, 0x81, 0x81, 0xFF, 0x42, 0x24, 0x18]


def writePattern(pattern):
    for row in range(8):
        grid.writeRowRaw(row, pattern[row])

grid = EightByEight(address=0x70)
grid.clear()

while True:
    writePattern( PATTERN_A )
    time.sleep(0.5)
    writePattern( PATTERN_N )
    time.sleep(0.5)
