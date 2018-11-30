import gdal
from osgeo import osr

def get_proj4(InputTIF):
    srs = osr.SpatialReference()
    src = gdal.Open(InputTIF)
    projsrc = src.GetProjection()
    srs.ImportFromWkt(projsrc)
    proj4 = srs.ExportToWkt()
    return proj4
