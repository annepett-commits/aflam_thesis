with arcpy.EnvManager(mask="indianaBorder", scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    out_flow_direction_raster = arcpy.sa.FlowDirection(
        in_surface_raster="output_SRTMGL1.tif",
        force_flow="NORMAL",
        out_drop_raster=None,
        flow_direction_type="D8"
    )
    out_flow_direction_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\FD")

with arcpy.EnvManager(cellSize="MAXOF", mask=None, scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    out_accumulation_raster = arcpy.sa.FlowAccumulation(
        in_flow_direction_raster=r"E:\Thesis\Thesis Master\ThesisMaster.gdb\FD",
        in_weight_raster=None,
        data_type="FLOAT",
        flow_direction_type="D8"
    )
    out_accumulation_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\FA")

with arcpy.EnvManager(cellSize="MAXOF", mask="indianaBorder", scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    out_raster = arcpy.sa.Slope(
        in_raster="output_SRTMGL1.tif",
        output_measurement="DEGREE",
        z_factor=1,
        method="PLANAR",
        z_unit="METER",
        analysis_target_device="GPU_THEN_CPU"
    )
    out_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\slopeDEM")

with arcpy.EnvManager(scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression='("slopeDEM" * 1.570796) /90'
    )
    output_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\slope")

with arcpy.EnvManager(scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression=' Con("slope">0,Tan("slope"),0.001 )'
    )
    output_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\tanslope")

with arcpy.EnvManager(scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression='("FA"+1)*0.0002777777777778146'
    )
    output_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\fasscaled")

with arcpy.EnvManager(scratchWorkspace=r"E:\Thesis\Thesis Master\Thesis Master.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression='Ln( "fasscaled"/ "tanslope")'
    )
    output_raster.save(r"E:\Thesis\Thesis Master\Thesis Master.gdb\wetness")
