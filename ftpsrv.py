#!/usr/bin/python3

import ftplib 

with ftplib.FTP('201.220.136.101') as ftp:
    
    csv = 'datos.csv'
    db = 'weewx.sdb'
    
    try:    
        ftp.login('davis', 'cenaoscopeco2021')  
        
        with open(csv, db, 'rb') as fp:
            
            res = ftp.storlines("STOR " + csv + db, fp)
            
            if not res.startswith('226 Transfer OK'):
                
                print('Upload failed')

    except ftplib.all_errors as e:
        print('FTP error:', e) 
