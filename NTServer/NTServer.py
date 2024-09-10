#1. Imports
import ntcore #import the NetworkTables library from RobotPy
import time # needed for sleep


# 2. grab the NetworkTables singleton
ntInstance = ntcore.NetworkTableInstance.getDefault()
# 3. start the NetworkTables server
ntInstance.startServer()
# 4. Get (or create) a new NetworkTable called NTDemo
table =  ntInstance.getTable("NTDemo")


# 5. initialize our x value
x = 0.0
# 6. Get (or create) a new Topic with double precision type and publish it
xPublisher = table.getDoubleTopic("x").publish()
# 7. Set the value of the topic
xPublisher.set(x)


# 8. Initialize our deltaX value
deltaX = 1
# 9. Get (or create) a new Topic with integer type and get the Entry
deltaXEntry = table.getIntegerTopic("deltaX").getEntry(deltaX)
# 10. Set the value of the deltaX topic
deltaXEntry.set(deltaX)


# 11. loop forever
while True:
    # 12. Read the current value of the deltaX topic
    delta = deltaXEntry.get()


    # 13. Increment the x variable
    x += delta
    # 14. Update the value of the x topic with the new value
    xPublisher.set(x)


    # 15. Wait a second before looping
    time.sleep(1)


    # 16. print to the terminal so we can compare client and server
    print(x)
