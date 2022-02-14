import ftplib

with ftplib.FTP('201.220.136.101') as ftp:

    filename = 'datos.csv'

    try:
        ftp.login('davis', 'cenaoscopeco2021')

        ftp.cwd("C:\raspberry\DAPRUEBA")
        
        with open(filename, 'rb') as fp:


            res = ftp.storlines("STOR " + filename, fp)

            if not res.startswith('226 Transfer OK'):

                print('Upload failed')

    except ftplib.all_errors as e:
        print('FTP error:', e)
