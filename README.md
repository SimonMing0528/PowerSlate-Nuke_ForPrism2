# PowerSlate-Nuke / ForPrism2


![FOR_PrismLOGO_alpha](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/148a8d52-cd9e-4aa7-8c9a-6b4d6238f68c)


![240103225015](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/0c54f6f2-ad2b-4c4e-a96d-72f9e9bb44df)



A Nuke slate plugin developed using Prism2, a VFX project workflow management software, capable of displaying current shot version information within the frame (e.g., shot ID, version number, frame range, project naming, etc.). This facilitates daily progress checks, comparisons, and allows for shot review personnel to confirm version details efficiently during regular work tasks



 
# Installation

> [!CAUTION]
> This Gizmo is based on [Prism2](https://prism-pipeline.com/)
Please ensure that the project settings are correctly configured in Prism before use.

1. Copy the entire folder into the Nuke environment directory. it's usually at `C:\Users(your username).nuke` . 
2. Then find the `init.py` file at Nuke environment directory and add the following code:
```
nuke.pluginAddPath('./PowerSlate_ForPrism2')
nuke.pluginAddPath('./PowerSlate_ForPrism2/py')
```

3. Once you've completed the above steps, launch your Nuke application. If the installation was successful, you should see the icon on the left side of the interface

![240103214715](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/4c3159d2-f68e-4e56-a37f-71e3016369c9)

# Usage

This plugin, integrated with Prism2 Pipeline management software, automatically retrieves essential information about the current scene, eliminating the need for manual inputs and operations in most cases。
However, there are still several options that require manual operation from you:

![0240103222206](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/cf80bfcd-2f47-43fe-9457-66b8f72fc8aa)

## TaskStatus：

Status markings are divided into three types: `PostViz`; `In-progress`; `Review`.

`PostViz`: Simply combines visual elements to get a rough overall effect of the arrangement.

`In-progress`: Indicates the current lens is still ongoing, used for progress checks.

`Review`: Denotes that the current version of the lens is completed, used for reviewers to inspect visual effects in order to provide feedback for modifications

## LetterBox
Checking this option will display all lens information within a black border outside the frame, preventing it from obstructing the image
> When this option is enabled, the information text at the top of the frame might shift higher or lower from its original position. Please manually adjust their positions in the `Text Position` below

![03225043](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/79844a62-c325-4d4c-b3c3-1fb964121355)

## Use TC code
This option will display the TIMECODE from the metadata within the frame

# Contact

Simon.lee.edu@outlook.com
