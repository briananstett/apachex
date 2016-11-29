import getopt
import sys
import re


def usage():
    print("'Apache Regex' is a simple script which turns a simple Apache2 web access lists\n"
          "into formated output")
    print(" -i --ip-address         Search by ip address")
    print(" -t --time-stamp         Search by time stamp")
    print(" -m --method             Search by client method")
    print(" -r --resource           Search by resource")
    print(" -p --protocol           Search by protocol")
    print(" -s --status-code        Search by status code")
    print(" -d --detail             Provide verbose information in the display")
    print(" -h --help               Displays usage")
    print(" --man                   Display the MAN page")
    sys.exit ()

def man():
    print("NAME\n\tApachex - Sorts raw apache log files")
    print("SYNOPSIS\n\tpython apachex [-i ] [--ip-address] LOGFILE...")
    print("DESCRIPTION\n\tApachex turns a raw apache access log in to sortable, formated, output."
          "\n\tApachex sorts through the LOGFILE and finds the different sections of the LOGFILE."
          "\n\tThen the user can specify whicn sections to display and in which order."
          "\n\tNOTE: Apachex will only show the sections that are requested in the options ")
    print("OPTIONS\n\t-i, --ip-address"
          "\n\t\tDisplays the IP address of the client requesting access to the Apache server"
          "\n\t-t, --time-stamp"
          "\n\t\tDisplays the time stamp which this event occured"
          "\n\t-m --method"
          "\n\t\tDisplays the method used for request. Usually GET"
          "\n\t-r --resource"
          "\n\t\tDisplays the actual resource the client was requesting."
          "\n\t-p --protocol"
          "\n\t\tDisplays the protocol used to make the request to the web server."
          "\n\t-s --status-code"
          "\n\t\tDisplays the status code that is returned to the user's machine"
          "\n\t-d --detail"
          "\n\t\tDisplays verbose information in the prompt for every entry"
          "\n\t-h --help : --man"
          "\n\t\tDisplays help information"
          )
    print("LOG FORMAT\n\t IP address -- [time stamp] \"METHOD\" Resource\\Resource Protocol\" Status-code")
    sys.exit()


def main():

    try:
        #parse command line input
        opts, file = getopt.getopt(sys.argv[1:], "itmrpshd", ["ip-address", "time-stamp", "method",
                                                                "resource", "protocol", "status-code", "help",
                                                                "man", "detail"])
        detailedFlag = 0    #flag for verbose option
        regexList = []      #list that will be used for translation between command line parse to regex group names
        if len(opts) == 0:  #if not options are set, exit and display usage
            usage()
            sys.exit()

        #add group name to regex list depending on options
        #display usage or man page depending on option
        for o,a in opts:
            if o in ('-i', '--ip-address'):
                regexList.append('ip')
            elif o in ('-t', '--time-stamp'):
                regexList.append('timeStamp')
            elif o in ('-m', '--method'):
                regexList.append('method')
            elif o in ('-r', '--resource'):
                regexList.append('resource')
            elif o in ('-p', "--protocol"):
                regexList.append('protocol')
            elif o in ('-s', "--status-code"):
                regexList.append('statusCode')
            elif o in ('-d', "--detail"):
                detailedFlag = 1
            elif o in ('-h', "--help"):
                usage()
            elif o in "--man":
                man()
        #error check: if the file exist, regex-it
        if (file):
            #file creations and usage
            stream = open(file[0])
            data = stream.read()
            stream.close()
            #regex time
            line = (re.compile(r'''(?P<ip>[\d.]*)\s-\s-\s\[
                                            (?P<timeStamp>[\d\w/:]*\s)
                                             [-\d]*]\s"
                                             (?P<method>[\w]{3})\s
                                             (?P<resource>[/.&?=^\w\-]*)\s
                                             (?P<protocol>[HTP/.\d]*)"\s
                                             (?P<statusCode>[\d]*\s[\d]*)
                                        ''', re.X | re.MULTILINE | re.IGNORECASE))
            #output
            #if the user wants a more detailed output
            if detailedFlag:
                for match in line.finditer(data):
                    for i in regexList:
                        print(i.upper()+ "-->" +match.group(i)+" "*5),
                    print("\n")
            else: #normal output
                for match in line.finditer(data):
                    for i in regexList:
                        print(match.group(i)),
                    print("\n")
    except getopt.GetoptError as error: #option not found
        print(error)
        usage()
    except IOError as noFile: #file not found
        print(noFile)
        usage()



if __name__ == '__main__':
    main()