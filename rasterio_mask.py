import fiona, rasterio, rasterio.mask

#
# https://rasterio.readthedocs.io/en/latest/api/rasterio.mask.html
# 
def clipper(InputTIF, InputSHP, OutTIF):
    with fiona.open(InputSHP, "r") as shapefile:
        features = [feature["geometry"] for feature in shapefile]
    with rasterio.open(InputTIF) as src:
        out_image, out_transform = rasterio.mask.mask(src, features, invert=True)
        out_meta = src.meta.copy()
    out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})
    with rasterio.open(OutTIF, "w", **out_meta) as dest:
        dest.write(out_image)
