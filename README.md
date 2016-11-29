APACHEX: 
	Python script to aid in web server (Apache) system adminstration. Apachex uses a regular expressiong API to sort the log into value groups, then,output them to the user’s specifications. This allows the users to choose which values to output and in which order.
	NOTE:
		As of the writing of this document, Apachex only supports Apache access logs and therefore options are limited to the format of such log.
  

Scenario:
	System adminstrator of a large company is tasked with maintaining the company’s web server. The largest log file of web server is the access log and therefore difficult to sort through in search of key values. The adminstrator could use grep, would require multiple layered commands, or sed, which is difficult to use and requires knowledge of regex. Apachex is the solution to by not only sorting the log but changing the output of the log.



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




