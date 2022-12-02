#distance
import maya.cmds as cmds
import math
def distanceWindow():
    if cmds.window('distance_window',q=True,ex=True):
        cmds.deleteUI('distance_window',window=True)
        
    cmds.window('distance_window',title='Distance Between Two Points')
    cmds.showWindow('distance_window')
    cmds.window('distance_window',e=True,wh=[300,300])
    
    cmds.columnLayout(adj=True)
    
    cmds.rowLayout(numberOfColumns=3)
    cmds.text(label='objectA')
    cmds.textField('objA_textField')
    cmds.button(l='GET',c=getA)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns=3)
    cmds.text(label='objectB')
    cmds.textField('objB_textField')
    cmds.button(l='GET',c=getB)
    cmds.setParent('..')    

    cmds.rowLayout(numberOfColumns=1)
    cmds.button(l='Calculate',c=findDistance)
    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=2)
    cmds.text(label='Result >>')
    cmds.text('result_text',label='')
    cmds.setParent('..')    

def getA(*args1):
    sels=cmds.ls(sl=True)
    if sels:    
        cmds.textField('objA_textField', e=True, tx=sels[0])
    else:
        cmds.textField('objA_textField', e=True, tx='')   

def getB(*args2):
    sels=cmds.ls(sl=True)
    if sels:    
        cmds.textField('objB_textField', e=True, tx=sels[0])
    else:
        cmds.textField('objB_textField', e=True, tx='')    

def findDistance(*args):
    objA = cmds.textField('objA_textField', q=True, tx=True)
    objB = cmds.textField('objB_textField', q=True, tx=True)
    
    objAPos = cmds.xform(objA,q=True,t=True,os=True)#t = translate
    objBPos = cmds.xform(objB,q=True,t=True,os=True)
    
    xLen = abs(objBPos[0]-objAPos[0])
    yLen = abs(objBPos[1]-objAPos[1])
    
    result = math.sqrt((xLen**2)+(yLen**2))    
    cmds.text('result_text', e=True, label=result)
    
distanceWindow()
    
