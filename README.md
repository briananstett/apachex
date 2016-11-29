# apachex
python script to sorts through Apache2 access logs using regex. Apachex identifies log values that can then be used with filteres. Which options are specified and in which order tells Apachex which values to display and which order.

python apachex -itp access.log

will display {ip address} {time stampe} {protocol} ---> in that order


There are many options and other verbose output options.






NAME
        Apachex - Sorts raw apache log files
SYNOPSIS
        python apachex [-i ] [--ip-address] LOGFILE...
DESCRIPTION
        Apachex turns a raw apache access log in to sortable, formated, output.
        Apachex sorts through the LOGFILE and finds the different sections of the LOGFILE.
        Then the user can specify whicn sections to display and in which order.
        NOTE: Apachex will only show the sections that are requested in the options 
OPTIONS
        -i, --ip-address
                Displays the IP address of the client requesting access to the Apache server
        -t, --time-stamp
                Displays the time stamp which this event occured
        -m --method
                Displays the method used for request. Usually GET
        -r --resource
                Displays the actual resource the client was requesting.
        -p --protocol
                Displays the protocol used to make the request to the web server.
        -s --status-code
                Displays the status code that is returned to the user's machine
        -d --detail
                Displays verbose information in the prompt for every entry
        -h --help : --man
                Displays help information
LOG FORMAT
         IP address -- [time stamp] "METHOD" Resource\Resource Protocol" Status-code




