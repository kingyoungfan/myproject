#!/usr/bin/env bash
if [ ! -n "$1" ]
then
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "wdbadmin" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        uwsgi --ini-paste-logged /Users/yangyang/workspace_my/myproject/production.ini
        echo "Start uwsgi service [OK]"
    fi


elif [ $1 = stop ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    killall -9 uwsgi
    sleep 1s
    uwsgi --ini-paste-logged /Users/yangyang/workspace_my/myproject/production.ini
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
fi