#!/bin/bash


curtime=$(date +"%M")
offcur=$(($curtime + 1))
nodePort1=$((($offcur * 46) + 30000))

firefox 10.102.60.147:$nodePort1/weather/Gandolf_the_White


