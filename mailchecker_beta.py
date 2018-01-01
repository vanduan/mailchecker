#! /usr/bin/env python
"""
INSTALLATION
   pip install validate_email
   pip install pyDNS

   
Command line options:

-b  -- bruteforce

Command line arguments:
-e email        -- email tempalte to bruteforce (use with -b)
-c characters   -- characters for bruteforce (use with -b)
-i filein       -- read email from file
-o fileout      -- print output into file
-t time         -- time thread sleep (default is 0.3s)


"""

from validate_email import validate_email
import itertools, getopt, sys, re, threading, time

data={
    'bru':'', 
    'email':'', 
    'chars':'1234567890abcdefghijklmnopqrsturwxyz.',
    'filein':'', 
    'fileout':'', 
    'time':0.3,
    'count':0,
    'success':0
}


def usage(code, msg=''):
    print """\nUsage: mchecker.py [-e email] | [-b] [-c charset] [-i filein] [-o fileout] 
    [-t xx] [-h help]
    
    -e <email>          Verify an email address
    -i <file in>        Verify list email from file
                        (Don't use with -e -b)
    -b <email_partent>  Brute-force email
                        Email format "vanduan??.dvp@gmail.com"
                        ?? ==> bruteforce two characters
        -c <characters>     Character set to bruteforce
                            Default is [a-z0-9.]
    -t xxx              Set time between two verify
                        Default is 0.3s 
                        The valid range is 0-600 (10 minutes)
    -o <file out>       Results to file
    -h                  This message
    
    Ex:
        #1. Check email
            mchecker.py -e vanduan95.dvp@gmail.com
        #2. Check list email from file
            mchecker.py -i \path\to\list\file.txt
        #3. Brute-force (default)
            mchecker.py -b vanduan??.dvp@gmail.com
            # set charset:  -c 13579
            # set file out: -o result.txt
            # set time:     -t 0.1
            => mchecker.py -b vanduan??.dvp@gmail.com -c 13579 -o result.txt -t 0.1
            
"""
    if msg:
        print msg
    sys.exit(code)
    
def bruteforce_list(charset, length):
    return itertools.product(charset, repeat=length)
    
def verify(email,fileout=''):
    data['count']+=1
    if fileout:
        try:
            # write to file
            f = open(fileout,'w+')
            if validate_email(email,verify=True):
                data['success']+=1
                f.write("[+] verify " + str(email) + " >>> Success <<<\n")
            else:
                f.write("[-] verify " + str(email) + "--\n")
            f.close()
        except IOError:
            print "The file does not exist, exiting gracefully"
            sys.exit(1)
    else:
        # print to console
        if validate_email(email,verify=True):
            data['success']+=1
            print '[+] verify', email,'>>> Success <<<'
        else:
            print '[-] verify', email,'--'
def from_file():
    # check email from file
    file = data['filein']
    f=open(file,'r')
    while True:
        e = f.readline().replace('\n','').replace('\r','')
        if not e:
            break
        verify(e,data['fileout'])

def run_check():
    if data['bru']:
        # bruteforce email
        if re.findall('\?+',data['bru']):
            print '   Error >>> not find ? in email partent'
            sys.exit(0)
        else:
            lenx = len(re.findall('\?+',data['bru'])[0])
            for e in bruteforce_list(data['chars'], lenx):
                ex = ''.join(e)
                email = data['bru'].replace('?'*lenx, ex)
                
                t = threading.Thread(target=verify, args=(email,data['fileout'],))
                t.start()
                time.sleep(data['time'])
                
    elif data['email']:
        verify(data['email'], data['fileout'])
    elif data['filein']:
        from_file()
    print "\n   \\\\\\\\\    DONE    /////"
    print "       Success",data['success'],"/",data['count']
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'e:i:o:t:c:b:h')
    except getopt.error, msg:
        sys.stdout = sys.stderr
        print msg
    if len(opts) == 0:
        usage(1)
    else:
        for o, a in opts:
            if o == '-e':
                data['email'] = a
            if o == '-i':
                data['filein'] = a
            if o == '-o':
                data['fileout'] = a
            if o == '-t':
                data['time'] = float(a)
            if o == '-c':
                data['chars'] = a
            if o == '-b':
                data['bru'] = a
            if o == '-h':
                usage(1)
                
    run_check()
if __name__ == '__main__':
    main()
