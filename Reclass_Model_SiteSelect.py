with arcpy.EnvManager(cellSize="MINOF", mask="indianaBorder", scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="NLCD_IN",
        reclass_field="Value",
        remap="1 1;3 3;4 4;5 5;NODATA 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\NLCD_IN")

with arcpy.EnvManager(cellSize="MINOF", mask="indianaBorder", scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="TWI_IN",
        reclass_field="Value",
        remap="1 1;3 4;4 5;5 1;NODATA 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\TWI_IN")

with arcpy.EnvManager(cellSize="MINOF", mask="indianaBorder", scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="GSCP_IN",
        reclass_field="Value",
        remap="0 1;1 1;2 4;3 5;NODATA 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\GSCP_IN")

with arcpy.EnvManager(scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Transformed SD_IN",
        reclass_field="VALUE",
        remap="1 1.444444 1;1.444444 2.333333 2;2.333333 3.222222 3;3.222222 4.111111 4;4.111111 5 5;NODATA 0",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\SD_IN")

with arcpy.EnvManager(outputCoordinateSystem='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', cellSize=30, scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=' ("SD_IN") + ("TWI_IN") + 2 * ( "NLCD_IN") + 2 * ("GSCP_IN")'
    )
    output_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\SEO_SuitMap")

with arcpy.EnvManager(scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="SEO_SuitMap",
        reclass_field="VALUE",
        remap="5 10 1;10 12.941176 2;12.941176 15.980392 3;15.980392 20 4;20 30 5",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\suit_classed")

with arcpy.EnvManager(scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="suit_classed",
        reclass_field="Value",
        remap="1 NODATA;2 NODATA;3 NODATA;4 4;5 5",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\Reclass_suit1")

with arcpy.EnvManager(scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Reclass_suit1",
        reclass_field="Value",
        remap="5 10 0;10 15 0;15 20 0;20 25 1;25 30 1;NODATA 0",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\suit_binary")

with arcpy.EnvManager(outputCoordinateSystem='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', cellSize=30, mask="SEO_SuitMap", scratchWorkspace=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb"):
    out_raster = arcpy.sa.RegionGroup(
        in_raster="suit_binary",
        number_neighbors="EIGHT",
        zone_connectivity="WITHIN",
        add_link="ADD_LINK",
        excluded_value=0
    )
    out_raster.save(r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\suit_groups")

arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="suit_groups",
    selection_type="NEW_SELECTION",
    where_clause="Count >= 666 And Count NOT IN (174681815)",
    invert_where_clause=None
)

with arcpy.EnvManager(outputCoordinateSystem='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPolygon(
        in_raster="suit_groups",
        out_polygon_features=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\suit_groups_poly",
        simplify="SIMPLIFY",
        raster_field="Value",
        create_multipart_features="SINGLE_OUTER_PART",
        max_vertices_per_feature=None
    )

arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="suit_groups_poly",
    selection_type="NEW_SELECTION",
    where_clause="Shape_Area >= 600000",
    invert_where_clause=None
)

arcpy.conversion.ExportFeatures(
    in_features="suit_groups_poly",
    out_features=r"C:\Users\annee\Desktop\ThesisB\ThesisB.gdb\suit_sites",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Id "Id" true true false 4 Long 0 0,First,#,suit_groups_poly,Id,-1,-1;gridcode "gridcode" true true false 4 Long 0 0,First,#,suit_groups_poly,gridcode,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,suit_groups_poly,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,suit_groups_poly,Shape_Area,-1,-1',
    sort_field=None
)
