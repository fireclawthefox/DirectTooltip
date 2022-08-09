# DirectTooltip

**NOTE:** This widget has been integrated in the DirectGuiExtension package:<br />
https://github.com/fireclawthefox/DirectGuiExtension

Since it got many more useful elements, including this tooltip, this repository is basically deprecated and won't really be maintained anymore.
<br />
<br />
<br />
<br />
<br />
A simple tooltip for Panda3D applications using DirectGUI

## Features
- Easy setup
- The tooltip will respect window bounds and keeps itself inside the window to be always visible
- Follows mouse movements

## How to use
Most simple usage:
```
tt = DirectTooltip()
tt.show("my test message")
```

Attaching it to any DirectGui element
```
from direct.gui import DirectGuiGlobals as DGG

tt = DirectTooltip()
tt.show("my test message")

myGuiElement.bind(DGG.ENTER, tt.show, ["My tooltip text for myGuiElement"])
myGuiElement.bind(DGG.EXIT, tt.hide)
```

State of DirectGui element needs to be specified as `DGG.Normal`

See the example.
