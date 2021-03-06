#!/usr/bin/python3

import ftplib 

with ftplib.FTP('201.220.136.101') as ftp:
    
    filename = 'datos.csv'
    
    try:    
        ftp.login('davis', 'cenaoscopeco2021')  
        
        with open(filename, 'rb') as fp:
            ftp.cwd("estacion_davis02")
            
            res = ftp.storlines("STOR " + filename, fp)
            
            if not res.startswith('226 Transfer OK'):
                
                print('Upload failed')

    except ftplib.all_errors as e:
        print('FTP error:', e) 