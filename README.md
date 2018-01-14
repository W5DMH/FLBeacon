# FLBeacon
Python FLDigi Beacon using XMLRPC &amp; PyFLDigi library

This is a simple program that provides a graphical front end to enter amateur radio beacon information which is saved in a config file then read from the config file to xmlrpc and posted to FLDigi to run as a beacon. 

Use at your own risk, it can leave the transciever in transmit mode on a bad exit (always stop the beacon and wait for it to stop transmitting before exiting) 

PyFLDigi python library/module is required for this software, install pyFLDigi first. 
Python 3 is required to run this software. 
Designed to run on a Raspberry Pi 2 running Stretch. Your mileage may vary on other linux platforms

An Amatuer radio license is required if you use this software to transmit a transceiver. 
