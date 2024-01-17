# Overview

This is a utility that adds support for the MacOS "New folder with selection" functionality to Windows.

# Usage

**Caution**: This script requires you to edit the Windows Registry. Editing the Windows Registry can be risky. It's important to follow these steps carefully.

At a high level, all we're doing here is adding a button in the context menu, and assigning a command to run our script whenever that option is pressed.

1. Press `Win + R`, type `regedit`, and press `Enter` to open the Registry Editor.
2. Navigate to HKEY_CLASSES_ROOT\*\shell. Right-click on shell, select New -> Key, and name it "CreateFolderWithSelection".
3. Select the "CreateFolderWithSelection" key you just made, and double-click "(Default)" in the right panel. The value you type here is going to be the text that shows up in the context menu. I just went with "New folder with selection"
4. Right-click on "CreateFolderWithSelection", select New -> Key, and name it "command".
5. Now, select the "command" key in the directory; in the right pane, double-click on the text that says "(Default)". A little form should pop up.
6. In the "Value" data box, enter the following, replacing "C:\Path\To\file_away.py" with the actual path to the script:

```
"C:\Python312\python.exe" "C:\Path\To\file_away.py" "%V"
```

7. Click "OK" and close the Registry Editor

You should now be able to select a number of files in File Explorer, right click to open the conext menu, click "Show more options", and use the option that you defined in step 3.

Hope this helps!
