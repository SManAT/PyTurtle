# -*- coding: utf-8 -*-
"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class SVG:
    debug = False
    height, width = 0, 0

    fh = None

    Pkt = []
    extra_svg_shapes = []
    defaultstyle = "fill:none;stroke:rgb(0,0,0);stroke-width:2"

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self._initPktArray(0, 0)

    def setDefaultStyle(self, **kwargs):
        self.defaultstyle = self._handle_Styles(kwargs)

    def getX(self, data):
        """extract X from e.g. 200,345"""
        items = data.split(",")
        return items[0].strip()

    def getY(self, data):
        """extract Y from e.g. 200,345"""
        items = data.split(",")
        return items[1].strip()

    def _SplitPoints(self, data):
        """
        splitte Points
        828.442325904,452.0944533##fill:none;fill-opacity:1;stroke:rgb(255,0,0);stroke-width:2 23,12## 23,23....
        M533.0,400.0 [stroke:#4567AE,stroke-width:2]733.0,500.0 -->
        M533.0,400.0, [stroke:#4567AE,stroke-width:2], 733.0,500.0
        """
        erg = []
        if len(data) > 0:
            items = data.split(" ")
            for item in items:
                # try split on ]
                part = item.split("]")
                if len(part) > 1:
                    # hat style
                    erg.append("%s]" % part[0])
                    erg.append(part[1])
                else:
                    erg.append(item)
        return erg

    def _getStyles(self, txt):
        """extract from '633.0,400.0##stroke:rgb(255,0,0);stroke-width:2' styles and coordinates"""
        parts = txt.split("##")
        # gibt es immer
        coordinates = parts[0]
        # muss es nicht geben
        try:
            styles = parts[1]
        except:
            styles = ""
        return [coordinates, styles]

    def _clearStyleSeperator(self, pt):
        """230,456## zu 230,456"""
        data = pt.split("##")
        return data[0]

    def _parsePktStr(self, data):
        """extract attributes and create SVG Lines"""
        # Data sieht so aus
        # M533.0,400.0## M533.0,400.0## 633.0,400.0##stroke:rgb(255,0,0);stroke-width:2 633.0,500.0##stroke:rgb(255,0,0);stroke-width:2

        # Split am Leerzeichen
        newdata = self._SplitPoints(data)

        # Erstelle die SVG Linien
        data = []
        style = ""
        # ['M533.0,400.0##', 'M533.0,400.0##', '633.0,400.0##stroke:rgb(255,0,0);stroke-width:2', '633.0,500.0##stroke:rgb(255,0,0);stroke-width:2']
        if self.debug:
            print("Newdata: %s" % newdata)

        # we draw allwasy lines from startPt to endPt
        startPt = ""
        endPt = ""
        for item in newdata:
            if len(item) > 0:
                # print("Item: %s" % item)
                new_item = self._getStyles(item)
                if new_item[0][0] == "M":
                    # Move To Command
                    startPt = self._clearStyleSeperator(item[1:])  # ohne M
                else:
                    # Start und Endpoint the same?
                    endPt = self._clearStyleSeperator(new_item[0])
                    style = new_item[1]

                    if self.getX(startPt) != self.getX(endPt) or self.getY(startPt) != self.getY(endPt):
                        if len(style) == 0:
                            style = self.defaultstyle
                        if self.debug:
                            print("Line:  %s, %s -> %s, %s" % (self.getX(startPt), self.getY(startPt), self.getX(endPt), self.getY(endPt)))
                        line = '<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />' % (self.getX(startPt), self.getY(startPt), self.getX(endPt), self.getY(endPt), style)
                        data.append(line)
                    else:
                        pass
                    startPt = endPt
        return data

    def _handle_Styles(self, kwargs):
        styles = ""
        if "fill" in kwargs:
            w = kwargs.get("fill")
            styles += ";fill:%s;fill-opacity:1" % w
        if "stroke" in kwargs:
            w = kwargs.get("stroke")
            styles += ";stroke:%s" % w
        if "stroke_width" in kwargs:
            w = kwargs.get("stroke_width")
            styles += ";stroke-width:%s" % w
        # dont start with ,
        if styles != "":
            if styles[:1] == ";":
                styles = styles[1:]
        return styles

    def SVG_MoveTo(self, x, y, **kwargs):
        """move to Coordinates"""
        erg = "M%s,%s"
        # Move to hat keine Styles!
        self.Pkt.append([erg % (x, y)])

    def SVG_DrawTo(self, x, y, **kwargs):
        """move to Coordinates"""
        erg = "%s,%s"
        if len(kwargs.items()) != 0:
            styles = self._handle_Styles(kwargs)
        else:
            styles = self.defaultstyle
        # Styles werden von den Koordinaten mit ## getrennt
        erg += "##%s" % styles
        self.Pkt.append([erg % (x, y)])

    def SVG_Circle(self, x, y, radius, **kwargs):
        """draws a circle, non filled"""
        # Transformation to center
        x = x + self.width / 2
        y = y + self.height / 2

        if len(kwargs.items()) != 0:
            styles = self._handle_Styles(kwargs)
        else:
            styles = self.defaultstyle

        self.extra_svg_shapes.append('<circle cx="%s" cy="%s" r="%s" style="%s" />' % (x, y, radius, styles))

    def _initPktArray(self, x, y):
        self.Pkt = []
        self.Pkt.append(["M%s,%s" % (x, y)])

    def getColor(self, data):
        """create Color for SVG Output"""
        return "stroke:%s" % data.strip()

    def getWidth(self, data):
        """create Width for SVG Output"""
        return "stroke-width:%s" % data.strip()

    # Übergeben wird ein Array aus Arrays bestehenden aus Punkten mit x,y Koordinaten
    # Erstellt wird ein  String Array aus Punkten im SVG Style
    # [M 130,10], [M 180,20], [170,10] ...
    # Pkt1x, Pkt1y Pkt2x, Pkt2y ...
    # M ... move to
    # Uppercase ... absolute Koordinaten
    # Lowercase ... relative Koordinaten
    def _array_to_SVG(self):
        # Alle Koordinaten auf Mitte Ausgabe beziehen
        TransformedPkt = []
        if self.debug:
            print("Original Data: %s" % self.Pkt)

        for i in range(len(self.Pkt)):
            data = self.Pkt[i]

            prefix = ""
            # extract "M "
            content = data[0]
            if content[0] == "M":
                content = content[1 : len(content)]
                prefix = "M"

            # are there Styles [3,5##color: rgb... ]?
            parts = content.split("##")
            coordinates = parts[0]
            items = coordinates.split(",")

            # muss es nicht geben
            try:
                styles = parts[1]
            except:
                styles = ""

            if items[0]:
                x = float(items[0]) + self.width / 2
            if items[1]:
                y = float(items[1]) + self.height / 2

            data_str = "%s%s,%s##%s" % (prefix, x, y, styles)
            TransformedPkt.append(data_str)

        erg = ""
        for i in range(0, len(TransformedPkt)):
            erg += TransformedPkt[i]
            if i != (len(TransformedPkt) - 1):
                erg += " "
        if self.debug:
            print("Transformed Data: %s" % erg)
        return erg

    # https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Shapes
    def _write_SVG_header(self):
        self._write_file('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
        self._write_file("<svg")
        self._write_file('xmlns:dc="http://purl.org/dc/elements/1.1/"')
        self._write_file('xmlns:cc="http://creativecommons.org/ns#"')
        self._write_file('xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"')
        self._write_file('xmlns:svg="http://www.w3.org/2000/svg"')
        self._write_file('xmlns="http://www.w3.org/2000/svg"')
        self._write_file('height="%s"' % (self.height))
        self._write_file('width="%s"' % (self.width))
        self._write_file('version="1.1">')
        self._write_file("<title>Tigerjython SVG</title>")
        self._write_file("<desc>Tigerjython SVG</desc>")

    def _write_SVG_footer(self):
        self._write_file("</svg>")

    def _write_file_path(self):
        """create SVG Data, color and width are in front within []"""
        pktstr = self._array_to_SVG()
        paths = self._parsePktStr(pktstr)

        for p in paths:
            self._write_file(p)

        # extra shapes
        for i in range(len(self.extra_svg_shapes)):
            item = self.extra_svg_shapes[i]
            # css einsetzen
            item = item[:-2]
            erg = "%s />" % (item)
            self._write_file(erg)

    def open_file(self, name):
        self.fh = open(name, "w")
        self._write_SVG_header()

    def close_file(self):
        if self.fh is not None:
            self._write_SVG_footer()
            self.fh.close()

    def _write_file(self, data):
        if self.fh is not None:
            self.fh.write(data + "\n")


if __name__ == "__main__":
    # Running some Tests
    svg = SVG(400, 400)
    svg.SVG_MoveTo(0, 0)
    svg.SVG_DrawTo(200, 200)

    svg.open_file("SVGTest.svg")
    svg._write_file_path()
    svg.close_file()
