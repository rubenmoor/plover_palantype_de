Palantype DE
=======================

This is a complete rework of the Possum Palantype steno system for efficient
use with the German language.
Its intended use is with a keyboard, not an actual Palantype machine.
Each finger operates three keys: Home row, top and bottom.
The thumbs are exceptions, they operate four keys.
There is no simultaneous pressing of multiple keys with one finger.

![The Palantype DE keyboard layout](https://raw.githubusercontent.com/rubenmoor/plover_palantype_german/palantype_de/keyboard_layout.bmp)

Like the original Palantype, this adaption is compatible with
Qwerty-keyboards as long as they support N-key roll-over (NKRO).
The optimal experience is to be expected with an Ergodox keyboard
or similar, i.e. a keyboard that allows full use of the thumbs.

How to use
======================

Quick start
----------------------

Head over to [palantype.com](https://palantype.com) to get started right away in
the browser.

Offline use with Plover
----------------------

This is a plugin for the software Plover from
[The Open Steno Project](http://www.openstenoproject.org/).
Download the
[latest version of Plover](https://github.com/openstenoproject/plover/releases/tag/v4.0.0.dev10).
Plover supports plugins from v4.0.0 on.

After installing this plugin, you need to turn on Palantype in Plover:

1. In Plover's configuration, go to the ``Systems`` tab, and change the active system to ``Palantype DE``.
2. In Plover's machine tab, select ``keyboard``.

Run in browser
----------------------

**Work in progress**

Currently, only the tutorial is implemented at [palantype.com](https://palantype.com).
Learning to type requires a lot of practice,
therefore it is recommended starting there in any case.

In future, [palantype.com](https://palantype.com) will also offer
an on-line text editor for steno typing.

Current state
=====================

The dictionary contains over 100'000 thousand words of the German language.
For productive use, a list of over 2'000'000 words has to be included (currently in progress).

Apart from `ILKSn` to delete the last input, there are no command keys implemented.

Missing features
=====================

* numbers
* arrow keys for navigation
* implement capitalize last word
* paragraph (return key)
* hyphenation of arbitrary words
* ...
