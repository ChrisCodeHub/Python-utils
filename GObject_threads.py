#!/usr/bin/python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

loopCount = 0

class Counter(object):
    def __init__(self):
        self.iterations = 0

    def updateCounts(self):
        self.iterations += 1



def janitor(counts, mainLoop):
    counts.updateCounts()
    print ("timed loop " + str(counts.iterations))
    if counts.iterations > 3:
        mainLoop.quit()
    return True

def main():
    print("in main")
    counts = Counter()
    loopCount = 0
    GObject.threads_init()
    mainLoop = GObject.MainLoop()

    GObject.timeout_add(1000, janitor, counts, mainLoop)
    mainLoop.run()




if __name__ == "__main__":
    main()
    exit(0)
