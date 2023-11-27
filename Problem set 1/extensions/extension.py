userip=input("File name: ")
if(userip.lower().endswith('.gif')):
    print('image/gif')
elif(userip.lower().endswith('.jpg') or userip.lower().endswith('.jpeg') ):
    print('image/jpeg')
elif(userip.lower().endswith('.png')):
    print('image/png')
elif(userip.lower().endswith('.pdf')):
    print('application/pdf')
elif(userip.lower().endswith('.txt')):
    print('text/plain')
elif(userip.lower().endswith('.zip')):
    print('application/zip')
else:
    print('application/octet-stream')