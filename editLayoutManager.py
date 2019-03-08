### Em construção

layoutS = QgsProject.instance().layoutManager().printLayouts()

for layout in layoutS:
    print(
    layout.name()
    layout.referenceMap().extent()
    
# Set a new value to the extent of current map
xmin = _float
ymin = _float
xmax = _float
ymax = _float

rect = QgsRectangle(xmin, ymin, xmax, ymax )
layout.referenceMap().setExtent()



'''
REF
https://gis.stackexchange.com/questions/67084/setting-the-extent-for-a-qgis-map-using-python
Setting a new extent to a LayoutMap
'''
