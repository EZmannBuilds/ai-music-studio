#!/usr/bin/env python3
"""Small dependency-free validator for the two optional structured-record types."""
import argparse, json, pathlib, sys
BASE=pathlib.Path(__file__).resolve().parents[1]
REQUIRED={"analysis_finding": {"id","source","observation","status"},"decision_event":{"id","when","scope","decision","reason","status"}}
ENUMS={"analysis_finding":{"status":{"observed","proposed","approved","applied","verified","dismissed"},"approval":{"pending","accepted","rejected","not_required"},"action_layer":{"composition","arrangement","sound_design","level","processing","none","undetermined"}},"decision_event":{"status":{"proposed","accepted","rejected","superseded"},"approved_by":{"user","delegated_agent","not_approved"}}}
def validate(kind,record):
    schema=json.loads((BASE/'schemas'/f'{kind}.schema.json').read_text())
    if not isinstance(record,dict): return ['record must be an object']
    errors=[]
    errors.extend('missing '+k for k in REQUIRED[kind]-record.keys())
    errors.extend('unknown '+k for k in record.keys()-schema['properties'].keys())
    for k,allowed in ENUMS[kind].items():
        if k in record and record[k] not in allowed: errors.append('invalid '+k)
    if kind=='analysis_finding':
        for k,fields in {'source':{'kind','artifact'},'observation':{'statement','basis'}}.items():
            if not isinstance(record.get(k),dict): errors.append(k+' must be object')
            else: errors.extend(k+' missing '+v for v in fields-record[k].keys())
        if isinstance(record.get('observation'),dict) and record['observation'].get('basis') not in {'measured','listened','inferred'}: errors.append('invalid observation basis')
        if record.get('status')=='verified' and not (isinstance(record.get('recheck'),dict) and record['recheck'].get('render_id') and record['recheck'].get('result')):errors.append('verified requires a new recheck')
    return errors
def main():
    a=argparse.ArgumentParser(); a.add_argument('kind',choices=REQUIRED); a.add_argument('files',nargs='+'); opt=a.parse_args(); bad=0
    for f in opt.files:
        try: record=json.loads(pathlib.Path(f).read_text()); errors=validate(opt.kind,record)
        except (ValueError,OSError) as exc: errors=[str(exc)]
        print(f, 'OK' if not errors else '; '.join(errors));bad+=bool(errors)
    return int(bool(bad))
if __name__=='__main__':sys.exit(main())
