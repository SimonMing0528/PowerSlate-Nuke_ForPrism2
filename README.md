# PowerSlate-Nuke / ForPrism2

![FOR_PrismLOGO](https://github.com/SimonMing0528/PowerSlate-Nuke-_-ForPrism2/assets/137688513/094063fd-9a88-4312-9be5-2295bb90b96e)

A Nuke slate plugin developed using Prism2, a VFX project workflow management software, capable of displaying current shot version information within the frame (e.g., shot ID, version number, frame range, project naming, etc.). This facilitates daily progress checks, comparisons, and allows for shot review personnel to confirm version details efficiently during regular work tasks


# Installation

1. Copy the entire folder into the Nuke environment directory. it's usually at `C:\Users(your username).nuke` . 
2. Then find the `init.py` file at Nuke environment directory and add the following code:
```
nuke.pluginAddPath('./PowerSlate_ForPrism2')
nuke.pluginAddPath('./PowerSlate_ForPrism2/py')
```

3. Once you've completed the above steps, launch your Nuke application. If the installation was successful, you should see the icon on the left side of the interface


