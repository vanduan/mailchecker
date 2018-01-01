# mailchecker
  Use to verify email

# INSTALLTION:
	download & install python 2.7 on your computer

# INSTALL PACKAGES:
	run file install_packages.bat
	
# USAGE: 

>mchecker.py -h

Usage: mchecker.py [-e email] | [-b] [-c charset] [-i filein] [-o fileout] 
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
            
