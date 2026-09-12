Tally the status and formats avail.

uv run python -c "
from geonorge_portolan_poc import dok_register, feed
import requests, collections

resp = requests.get('https://register.geonorge.no/api/geodatalov-statusregister.csv', timeout=30)
uuids = dok_register.parse_register_uuids(resp.content)

xml = open('cache/tjenestefeed.xml','rb').read()
entries = feed.parse_tjenestefeed(xml)
grouped = feed.group_by_dataset(entries)

supported = {'GEOJSON','GPKG','GEOPACKAGE','SHAPE','FGDB'}

dok_datasets = {did: es for did, es in grouped.items() if dok_register.extract_uuid(es[0].csw_metadata_url) in uuids}
print('DOK datasets total (in feed):', len(dok_datasets))

has_supported = 0
no_supported = 0
all_formats = collections.Counter()
unsupported_only_formats = collections.Counter()
for did, es in dok_datasets.items():
    fmts = {e.format.upper() for e in es}
    for f in fmts:
        all_formats[f]+=1
    if fmts & supported:
        has_supported += 1
    else:
        no_supported += 1
        for f in fmts:
            unsupported_only_formats[f]+=1

print('has supported format:', has_supported)
print('no supported format:', no_supported)
print()
print('all format counts across DOK datasets:')
for f,c in all_formats.most_common():
    print(f, c)
print()
print('formats present ONLY on DOK datasets lacking any supported format:')
for f,c in unsupported_only_formats.most_common():
    print(f, c)
"
