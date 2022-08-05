from panda3d.core import *
from direct.gui.DirectGui import *

from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectFrame
from direct.gui import DirectGuiGlobals as DGG

from DirectTooltip import DirectTooltip


def _pos2d(x, y):
    return Point3(x, 0, -y)


def _rec2d(width, height):
    return (width, 0, 0, -height)


class Wrapper:
    def __init__(self):

        # this is required for this demo
        self.b = ShowBase()

    def clean(self):
        for element in self.UI_elements:
            element.removeNode()

    def build(self):

        pos = (600, 200)
        pos = _pos2d(*pos)
        size = _rec2d(60, 60)

        myFrame1 = DirectFrame(frameColor=(0, 0, 0, 1),
                               frameSize=size,
                               pos=pos,
                               parent=pixel2d,
                               state=DGG.NORMAL)  # state is important

        myFrame2 = DirectFrame(frameColor=(0, 0, 0, 1),
                               frameSize=(-0.05, 0.05, -0.05, 0.05),
                               pos=(0, -0.5, -0.5),
                               state=DGG.NORMAL)  # state is important

        myFrame3 = DirectFrame(frameColor=(0, 0, 0, 1),
                               frameSize=(-0.05, 0.05, -0.05, 0.05),
                               pos=(0.5, -0.5, -0.5),)
        # state (missing here) is important

        tt = DirectTooltip.DirectTooltip()
        tt.show("my test message")
        tt.hide()

        myFrame1.bind(DGG.ENTER, tt.show, ["My tooltip text for frame1"])
        myFrame1.bind(DGG.EXIT, tt.hide)

        myFrame2.bind(DGG.ENTER, tt.show, ["My other text for frame2"])
        myFrame2.bind(DGG.EXIT, tt.hide)

        myFrame3.bind(DGG.ENTER, tt.show, ["no show frame3 wrong state"])
        myFrame3.bind(DGG.EXIT, tt.hide)

        self.UI_elements = [tt, myFrame1, myFrame2, myFrame3]


def main():
    W = Wrapper()
    W.build()

    while True:
        W.b.taskMgr.step()


if __name__ == "__main__":
    main()
