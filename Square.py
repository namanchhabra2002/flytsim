#!/usr/bin/env python
import time
from flyt_python import api

def main():
    # Initialize the drone navigation API
    drone_navigation = api.navigation(timeout=120000)

    # Wait for the system to be ready
    time.sleep(3)

    # Take off to an altitude of 5 meters
    print('1. Initiating takeoff to an altitude of 5 meters.')
    drone_navigation.take_off(5.0)
    print('Drone is now airborne at Point A of the square ABCD.')

    # Move the drone in a square trajectory with a side length of 6.5 meters at an altitude of 5 meters
    print('Moving the drone in a square pattern with side length 6.5 meters at an altitude of 5 meters.')

    # Move to Point B
    print('2. Moving to Point B of the square ABCD.')
    drone_navigation.position_set(6.5, 0, 0, yaw=1.0472, relative=True)

    # Move to Point C
    print('2. Moving to Point C of the square ABCD.')
    drone_navigation.position_set(0, 6.5, 0, relative=True)

    # Move back to Point D
    print('2. Moving back to Point D of the square ABCD.')
    drone_navigation.position_set(-6.5, 0, 0, relative=True)

    # Move back to Point A
    print('2. Moving back to Point A of the square ABCD.')
    drone_navigation.position_set(0, -6.5, 0, relative=True)

    # Landing the drone
    print('6. Initiating landing sequence.')
    drone_navigation.land(async=False)

    # Disconnect the drone navigation API
    drone_navigation.disconnect()

if __name__ == "__main__":
    main()
