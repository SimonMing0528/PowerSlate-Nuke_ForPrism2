# add menu
sideBar = nuke.menu('Nodes')
Pws = sideBar.addMenu('PowerSlate_ForPrism', icon='icon_ForPrism2.png')

def create_and_rename_node():
    new_node = nuke.createNode('PowerSlate_Scene')
    if new_node:
        new_node.setName('PowerSlate_Scene')
        core_button = new_node.knob('Core')
        if core_button:
            core_button.execute()

def create_rename_Ldv():
    new_node = nuke.createNode('PowerSlate_LookDev')
    if new_node:
        new_node.setName('PowerSlate_LookDev')
        core_button = new_node.knob('Load')
        if core_button:
            core_button.execute()

def setOnLoad():
    project_settings = nuke.toNode('root')  
    if 'onScriptLoad' in project_settings.knobs():
        on_script_load_knob = project_settings['onScriptLoad']
        on_script_load_knob.setValue('from mainCallBack import* ;preStart();aftRenderDisable()')


# add Group to menu
Pws.addCommand('Pws_Shot',"create_and_rename_node(); setOnLoad()")
Pws.addCommand('Pws_LookDev',"create_rename_Ldv(); setOnLoad()")




