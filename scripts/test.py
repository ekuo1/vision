#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import rospy

import numpy as np
import cv2

def receive():
    print("owl")
    cap = cv2.VideoCapture("udpsrc port=5000 ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink",cv2.CAP_GSTREAMER)
    print("cat")
    if not cap.isOpened():
        print('VideoCapture not opened')
        exit(0)

    while True:
        ret,frame = cap.read()
        print("dog")
        if not ret:
            print('empty frame')
            break

        cv2.imshow('receive', frame)
        print("fish")
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    print("bird")
    cap.release()

if __name__ == '__main__':
    receive()

    cv2.destroyAllWindows()