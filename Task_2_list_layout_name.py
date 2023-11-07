import arcpy

pro_project_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_9_Automating_map_production\Assignment_9_ProProject\MyProject.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)

layout_list =my_project.listLayouts()

for layout in layout_list:
    print("The Layout named in ArcGIS is: {}".format(layout.name))
    



