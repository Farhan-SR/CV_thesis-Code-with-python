import os

def main():
    i = 1
    path = "D:/A2 final data set 115/A2 final data set 115/Atash P"
    for filename in os.listdir(path):
        dest = str(i) + ".jpg"
        source = os.path.join(path, filename)
        dest = os.path.join(path, dest)
        os.rename(source, dest)
        i += 1
main()