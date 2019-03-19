# -*- coding: utf-8 -*-
### Em construção

# Access the PrintLayouts from the layoutManager.
layoutS = QgsProject.instance().layoutManager().printLayouts()
layouts_name = [layout.name() for layout in QgsProject.instance().layoutManager().printLayouts()]

refExt = QgsProject.instance().layoutManager().layoutByName('DESEN Areas Estrategicas').referenceMap().extent()

# Iterate over the layouts
for layout in layoutS:
    # Create a list with the limits
    OriginExtent = [layout.referenceMap().extent().xMinimum(),\
                    layout.referenceMap().extent().yMinimum(),\
                    layout.referenceMap().extent().xMaximum(),\
                    layout.referenceMap().extent().yMaximum()]
''' 
    # Cria uma variável para cada uma
    xminO = layout.referenceMap().extent().xMinimum(),\
    yminO = layout.referenceMap().extent().yMinimum(),\
    xmaxO = layout.referenceMap().extent().xMaximum(),\
    ymaxO = layout.referenceMap().extent().yMaximum()]
'''
    # Show the result test                
    print(
    layout.name(),\
    OriginExtent)
    
# Set a new value to the extent of current map
xmin = _float
ymin = _float
xmax = _float
ymax = _float

rect = QgsRectangle(xmin, ymin, xmax, ymax )

def changeExtent(nRectangle):
    layout.referenceMap().setExtent()
    
# Find the items from the layout
def items():
    layout.items()
     
             
'''
REF
https://gis.stackexchange.com/questions/67084/setting-the-extent-for-a-qgis-map-using-python
Setting a new extent to a LayoutMap
'''
