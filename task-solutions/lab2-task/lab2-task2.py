# Task 2
diskSize = 1000
diskSizeUsed = 650

fileSize = float(input("Enter your file size: "))

freeSpace = diskSize - diskSizeUsed

if fileSize < freeSpace:
    print("File download completed successfully.")
else:
    print("Insufficient disk space!")
