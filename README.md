This [SublimeText2][sublime] plugin will simply align a number of selections by inserting spaces on each line until they align.

This would typically be used to make long blocks of assignments or function calls more readable. For example:

```javascript
var someVariable = 'foo',
    me           = this,
    Tyrtle       = require('Tyrtle'),
    HtmlRenderer = require('tyrtle/renderers/html')
;
```

By making a selection right before each of the equals signs (by holding `ctrl` and clicking on each line), and then activating the **Align Selections** command (`Selection -> Align Selections`, or `Ctrl+K, Ctrl+A`), the result would look like this:

```javascript
var someVariable = 'foo',
    me           = this,
    Tyrtle       = require('Tyrtle'),
    HtmlRenderer = require('tyrtle/renderers/html')
;
```

Selecting these equals signs is made even easier by the **Select More** command (a built-in command, default shortcut `Ctrl+D`). Simply select the first `=` and then press `Ctrl+D` repeatedly until all are selected. Then `Ctrl+K, Ctrl+A` to align them.

[sublime]: http://www.sublimetext.com/
