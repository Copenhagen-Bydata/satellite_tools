from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

def get_api(user,password):
	api = SentinelAPI(user,password, 'https://scihub.copernicus.eu/dhus')
	return api
  
def download_metadata(db_user,db_pass,api_user,api_pass,table_name='s2_metadata',schema='<SCHEMA>',database='<DATABASE>',platformname='Sentinel-2',aoi='<GEOJSON OF AREA>'):
	api = get_api(api_user,api_pass)
	engine = init_db(db_user,db_pass,database)
	footprint = geojson_to_wkt(read_geojson(aoi))
	products = api.query(footprint,
			     date=('20150623', 'NOW'),
			     platformname=platformname,
			     cloudcoverpercentage=(0,100))
	products_df = api.to_dataframe(products)
	products_df.to_sql(table_name, engine, schema=schema,if_exists='replace')
	engine.execute('alter table {1}.{0} add primary key(index)'.format(table_name,schema))
	engine.execute('alter table {1}.{0} add column thumb_loc text'.format(table_name, schema))
