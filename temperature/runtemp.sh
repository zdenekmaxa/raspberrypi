#!/bin/sh

# temper temperature reading correction
CORRECTION=-2.5

READING=`sudo /home/pi/temperature/temperv14/temperv14 -c`
RET=$?
if [ $RET -eq 0 ] ; then
    TEMP=`echo $READING+$CORRECTION | bc`
    echo "Temperature reading: $READING, after correction: $TEMP at `date`"
    curl --insecure https://data-watch.appspot.com/store?measurement=$TEMP
    echo "Return value of store curl call: $?"
else
    echo "Error occured at `date` (return code: $RET)."
fi

