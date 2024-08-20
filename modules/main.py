import json
import ee
import google.auth
from stats import get_stats

def main(request):
  """HTTP Cloud Function."""
  request_json = request.get_json(silent=True)
  region_geojson = request_json['region']

  credentials, _ = google.auth.default(
      scopes=['https://www.googleapis.com/auth/earthengine']
  )
  ee.Initialize(credentials)

  ee_feature = ee.Feature(region_geojson)
  stats_feature = ee.FeatureCollection(get_stats(ee.Feature(ee_feature))).first()

  return json.dumps(stats_feature.getInfo())
