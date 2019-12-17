COLOUR_CODES={"aquamarine1": "#7fffd4", "black": "#000000", "brown1": "#ff4040",
              "burlywood": "#deb887", "chocolate": "#d2691e", "coral": "#ff7f50",
              "DarkGreen": "#006400", "gray": "#bebebe", "HotPink": "#ff69b4", "light": "#eedd82"}

name=input("Enter a name of a colour: ")
while name!= "":
    print("The code for {} is {}".format(name, COLOUR_CODES.get(name)))
    name=input("Enter a name of a colour: ")