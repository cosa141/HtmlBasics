try:
    f = open('simple','w')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    #You can leave it at just exept if you dont know the kind of error to expect
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()
finally:
   print("Always execute finally code blocks")
