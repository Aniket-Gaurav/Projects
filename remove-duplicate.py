import hashlib
import os
# Returns the hash string of the given file name
 
def hashFile(filename):
    # For large files, if we read it all together it can lead to memory overflow, So we take a blocksize to read at a time
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        # Reads the particular blocksize from file
        buf = file.read(BLOCKSIZE)
        while(len(buf) > 0):
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()
 
if __name__ == "__main__":
    # Dictionary to store the hash and filename
    hashMap = {}
    # List to store deleted files
    deletedFiles = []
    directory_path = 'Z:/New/Downloads'
    filelist = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for f in filelist:
        key = hashFile(f)
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key] = f
    if len(deletedFiles) != 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')