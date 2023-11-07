import arcpy

pro_project_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_9_Automating_map_production\Assignment_9_ProProject\MyProject.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)

maps_list = my_project.listMaps()


for map in maps_list:
    print("Layers in Map: {} are as follows".format(map.name))
    print("----------------------------------------------")
    for layer in map.listLayers():
        print(layer.name)




