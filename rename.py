import os

def main():
    i = 1
    path = "C:/Users/alien/Desktop/img_aug/out_compressed"
    for filename in os.listdir(path):
        dest = str(i) + ".jpg"
        source = os.path.join(path, filename)
        dest = os.path.join(path, dest)
        os.rename(source, dest)
        i += 1
main()