LOG="/home/pi/.fldigi/scripts/fldigi-test.log"
if [ ${1} ]
then
        echo -n "${1} ">>$LOG
        echo "${1}" > /home/pi/FLBeacon/FLBeaconReceived.txt
fi
echo "message received `date -u`">>$LOG
echo "message received `date -u`"> /home/pi/FLBeacon/FLBeaconReceived.txt
tail -3 ~/.fldigi/talk/textout.txt > /home/pi/FLBeacon/FLBeaconReceived.txt
sleep 40
tail -3 ~/.fldigi/talk/textout.txt >>$LOG
exit 0
