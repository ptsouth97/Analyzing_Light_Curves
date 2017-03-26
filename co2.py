import os
import re
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Blake\PycharmProjects\Analyzing_Light_Curves") # change to the working directory


x = []                                                  # initialize empty lists for x and y data
y = []

readFile = open("co2_mm_mlo.txt", "r")                  # open the file in read mode
sepFile = readFile.read().split('\n')                   # split the list on new lines
sepFile = [x for x in sepFile if not x.startswith('#')] # get rid of lines that begin with '#'
readFile.close()

sepFile.pop()                                           # removes last item on list
sepFile.pop()                                           # removes last item on list

for i in sepFile:
    string = str(i)
    first_space = string.lstrip()                       # remove the first space in each line
    stripped = re.sub(' +', ' ', first_space)           # remove any multiple spaces
    xAndY = stripped.split(" ")                         # split each element on the spaces
    x.append(float(xAndY[2]))                           # add the first number to the x list
    y.append(float(xAndY[4]))                           # add the second number to the y list
    
plt.plot(x, y)
plt.title('Atmospheric CO2 at Mauna Loa Observatory')
plt.xlabel('Year')
plt.ylabel('Parts Per Million')

plt.show()
