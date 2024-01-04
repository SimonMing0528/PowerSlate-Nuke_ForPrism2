# PowerSlate-Nuke / ForPrism2


![FOR_PrismLOGO_alpha](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/148a8d52-cd9e-4aa7-8c9a-6b4d6238f68c)


![240103225015](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/0c54f6f2-ad2b-4c4e-a96d-72f9e9bb44df)
>source: < The Wandering Earth 2 >


A Nuke slate plugin developed using Prism2, a VFX project workflow management software, capable of displaying current shot version information within the frame (e.g., shot ID, version number, frame range, project naming, etc.). This facilitates daily progress checks, comparisons, and allows for shot review personnel to confirm version details efficiently during regular work tasks <br>
<br>
基于Prism2的 Nuke 镜头信息拍屏插件，能够在画面中显示当前镜头的版本信息（例如镜头编号、版本号、帧范围、项目命名等）。这有助于进行日常进度检查和比较，并允许镜头审核人员在常规工作中高效确认版本细节<br>
<br>
<br>
<br>

# Installation

> [!CAUTION]
> This Gizmo is based on [Prism2](https://prism-pipeline.com/)
Please ensure that the project settings are correctly configured in Prism before use.
<br>
<br>

1. Copy the `PowerSlate_ForPrism2` full folder into the Nuke environment directory.<br>
it's usually at `C:\Users\(your username)\.nuke`
<br>
2. Then find the `init.py` file，If there isn't one, create it. and add the following code:

```
nuke.pluginAddPath('./PowerSlate_ForPrism2')
nuke.pluginAddPath('./PowerSlate_ForPrism2/py')
```

3. Once you've completed the above steps, launch your Nuke application. If the installation was successful, you should see the icon on the left side of the interface
![240103214715](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/4c3159d2-f68e-4e56-a37f-71e3016369c9)

# Usage <br>
![LCT 拷贝](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/eeef577d-961d-4694-95cb-faa61a7a1516)


![103231501](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/d943e9b9-857b-4b74-a07d-0855bd194712)

This plugin, integrated with Prism2 Pipeline management software, automatically retrieves essential information about the current scene, eliminating the need for manual inputs and operations in most cases。
However, there are still several options that require manual operation from you:

![0240103222206](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/cf80bfcd-2f47-43fe-9457-66b8f72fc8aa) <br>
<br>
<br>
## TaskStatus：

Status markings are divided into three types: `PostViz`; `In-progress`; `Review`.<br>
<br>

`PostViz`: Simply combines visual elements to get a rough overall effect of the arrangement.

`In-progress`: Indicates the current lens is still ongoing, used for progress checks.

`Review`: Denotes that the current version of the lens is completed, used for reviewers to inspect visual effects in order to provide feedback for modifications <br>
<br>
<br>
<br>

## LetterBox
Checking this option will display all lens information within a black border outside the frame, preventing it from obstructing the image
> When this option is enabled, the information text at the top of the frame might shift higher or lower from its original position. Please manually adjust their positions in the `Text Position` below

![03225043](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/79844a62-c325-4d4c-b3c3-1fb964121355) <br>
>source: < The Wandering Earth 2 ><br>
<br>
<br>

## Use TC code
This option will display the TIMECODE from the metadata within the frame <br>
<br>
<br>

# Contact
If you have any questions or wish to report a bug related to this gizmo
feel free to leave a message using GitHub's issue section or contact me via the following email: <br>
Simon.lee.edu@outlook.com <br>
<br>
<br>
<br>

