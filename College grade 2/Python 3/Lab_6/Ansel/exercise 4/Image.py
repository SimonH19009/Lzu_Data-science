#!/usr/bin/env python3
# Copyright (c). All rights reserved.

"""
This module provides the Image class which holds (x, y, color) triples
and a background color to provide a kind of sparse-array representation of
an image. A method to export the image in XPM format is also provided.

>>> import os
>>> import tempfile
>>> red = "#FF0000"
>>> blue = "#0000FF"
>>> img = os.path.join(tempfile.gettempdir(), "test.img")
>>> xpm = os.path.join(tempfile.gettempdir(), "test.xpm")
>>> image = Image(10, 8, img)
>>> for x, y in ((0, 0), (0, 7), (1, 0), (1, 1), (1, 6), (1, 7), (2, 1),
...             (2, 2), (2, 5), (2, 6), (2, 7), (3, 2), (3, 3), (3, 4),
...             (3, 5), (3, 6), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4),
...             (5, 5), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1),
...             (7, 2), (7, 5), (7, 6), (7, 7), (8, 0), (8, 1), (8, 6),
...             (8, 7), (9, 0), (9, 7)):
...    image[x, y] = blue
>>> for x, y in ((3, 1), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2),
...             (6, 1)):
...    image[(x, y)] = red
>>> print(image.width, image.height, len(image.colors), image.background)
10 8 3 #FFFFFF
>>> image.save()
>>> newimage = Image(1, 1, img)
>>> newimage.load()
>>> print(newimage.width, newimage.height, len(newimage.colors), newimage.background)
10 8 3 #FFFFFF
>>> image.export(xpm)
>>> image.thing
Traceback (most recent call last):
...
AttributeError: 'Image' object has no attribute 'thing'
>>> for name in (img, xpm):
...     try:
...         os.remove(name)
...     except EnvironmentError:
...         pass
"""

import os
import pickle


class ImageError(Exception): pass
class CoordinateError(ImageError): pass
class LoadError(ImageError): pass
class SaveError(ImageError): pass
class ExportError(ImageError): pass
class NoFilenameError(ImageError): pass


class Image:

    def __init__(self, width, height, filename="",
                 background="#FFFFFF"):
        
        self.filename = filename
        self.__background = background
        self.__data = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}



    @property
    def background(self):
        return self.__background


    @property
    def width(self):
        return self.__width


    @property
    def height(self):
        return self.__height


    @property
    def colors(self):
        return set(self.__colors)


    def __getitem__(self, coordinate):
        
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)


    def __setitem__(self, coordinate, color):
       
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)


    def __delitem__(self, coordinate):
       
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        self.__data.pop(tuple(coordinate), None)


    def save(self, filename=None):
        
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            data = [self.width, self.height, self.__background,
                    self.__data]
            fh = open(self.filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

        
    def load(self, filename=None):
        
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            fh = open(self.filename, "rb")
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background,
             self.__data) = data
            self.__colors = (set(self.__data.values()) |
                             {self.__background})
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


    def export(self, filename):
       
        if filename.lower().endswith(".xpm"):
            self.__export_xpm(filename)
        else:
            raise ExportError("unsupported export format: " +
                              os.path.splitext(filename)[1])


    def __export_xpm(self, filename):
        
        name = os.path.splitext(os.path.basename(filename))[0]
        count = len(self.__colors)
        chars = [chr(x) for x in range(32, 127) if chr(x) != '"']
        if count > len(chars):
            chars = []
            for x in range(32, 127):
                if chr(x) == '"':
                    continue
                for y in range(32, 127):
                    if chr(y) == '"':
                        continue
                    chars.append(chr(x) + chr(y))
        chars.reverse()
        if count > len(chars):
            raise ExportError("cannot export XPM: too many colors")
        fh = None
        try:
            fh = open(filename, "w", encoding="ascii")
            fh.write("/* XPM */\n")
            fh.write("static char *{0}[] = {{\n".format(name))
            fh.write("/* columns rows colors chars-per-pixel */\n")
            fh.write('"{0.width} {0.height} {1} {2}",\n'.format(
                     self, count, len(chars[0])))
            char_for_colour = {}
            for color in self.__colors:
                char = chars.pop()
                fh.write('"{char} c {color}",\n'.format(**locals()))
                char_for_colour[color] = char
            fh.write("/* pixels */\n")
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    color = self.__data.get((x, y), self.__background)
                    row.append(char_for_colour[color])
                fh.write('"{0}",\n'.format("".join(row)))
            fh.write("};\n")
        except EnvironmentError as err:
            raise ExportError(str(err))
        finally:
            if fh is not None:
                fh.close()

