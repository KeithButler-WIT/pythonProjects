#!/usr/bin/env python3

from plyer import notification, battery
import time

app_name = title = 'Battery Warning'

while True:
    if battery.status['isCharging'] == False and battery.status['percentage'] <= 20:
        notification.notify(
            title = title,
            message = 'Battery is low better get charging',
            app_name = app_name,
            toast = False,
        )
    elif battery.status['isCharging'] == True and battery.status['percentage'] >= 90:
        notification.notify(
            title = title,
            message = 'Battery is full got to perserve battery health',
            app_name = app_name,
            toast = False,
        )

    time.sleep(60)
