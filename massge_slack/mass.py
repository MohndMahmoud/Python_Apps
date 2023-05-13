import requests
import sys
import getopt

#send massage
def send_slack_massage(massage):
    payload ='{"text":"%s"}' % massage
      #Function from slack sdk
    response = requests.post('https://hooks.slack.com/services/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',data=payload)
    
    print(response.text)

def main(argv):
    massage=' '
    try : opts ,args =getopt.getopt(argv, "hm:",["massage="])
    except getopt.GetoptError : 
        print("mass.py -m <massage>")
        sys.exit(2)
    if len(opts)==0 :
        massage="Hello People !"
    for opt,arg in opts :
        if opt == '-h' :
            print('mass.py -m <massage>')
            sys.exit()
        elif opt in ("-m","--massage"):
            massage=arg
    send_slack_massage(massage)
if __name__ =="__main__" :
    main(sys.argv[1:])