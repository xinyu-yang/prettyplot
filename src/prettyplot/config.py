#!/usr/bin/python3

__all__ = [
        "COLOR_LIGHT",
        "COLOR",
        "GNU_COLOR",
        "LINESTYLE",
        "MARKERSTYLE",
        "HATCH"
        ]


#http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
#http://tableaufriction.blogspot.ro/2012/11/finally-you-can-use-tableau-data-colors.html
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),  
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),  
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),  
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),  
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.  
tableau20 = [(rgb[0]/255., rgb[1]/255., rgb[2]/255.) for rgb in tableau20]

# remove every other color (light version)
COLOR_LIGHT = [tableau20[i] for i in range(len(tableau20)) if i % 2 == 1]
COLOR = [tableau20[i] for i in range(len(tableau20)) if i % 2 == 0]
GNU_COLOR = ["darkviolet", "#009e73", "#56b4e9", "#e69f00", "#f0e442", "#0072b2", "#e51e10", "black", "gray"]

LINESTYLE = ('-', '--', '-.', ':')
MARKERSTYLE = ('o', 'v', '^', 'D', 's', '<', '>', 'h', '8')
HATCH = ('/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*')
