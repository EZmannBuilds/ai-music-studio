#!/usr/bin/env python3
"""Small dependency-free validator for the optional structured-record types."""
import argparse, json, pathlib, sys
BASE=pathlib.Path(__file__).resolve().parents[1]
REQUIRED={"analysis_finding": {"id","source","observation","status"},"decision_event":{"id","when","scope","decision","reason","status"},"sketch_round":{"id","when","project","brief","candidates","outcome"}}
ENUMS={"analysis_finding":{"status":{"observed","proposed","approved","applied","verified","dismissed"},"approval":{"pending","accepted","rejected","not_required"},"action_layer":{"composition","arrangement","sound_design","level","processing","none","undetermined"}},"decision_event":{"status":{"proposed","accepted","rejected","superseded"},"approved_by":{"user","delegated_agent","not_approved"}},"sketch_round":{}}
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
    if kind=='sketch_round':
        errors.extend(sketch_round_errors(record))
    return errors
DIFF={"groove","harmony_and_melody","instrumentation","production_texture","density","structure","emotional_character"}
def sketch_round_errors(r):
    """The protocol's rules (shared/SKETCH_ROUND_PROTOCOL.md): distinct sketches, honest bases, one KEEP."""
    e=[]; c=r.get('candidates')
    if not isinstance(c,list) or len(c)<2: return ['candidates must list at least two sketches']
    labels=[x.get('label') for x in c if isinstance(x,dict)]
    if len(set(labels))!=len(labels): e.append('duplicate labels')
    for x in c:
        if not isinstance(x,dict): e.append('candidate must be object'); continue
        L=x.get('label','?')
        e.extend(f'{L} missing '+k for k in {'label','one_line','differs_on','decision','basis','decided_by'}-x.keys())
        d=x.get('differs_on',[])
        if not isinstance(d,list) or len(set(d))<2: e.append(f'{L} must differ on at least two dimensions')
        elif set(d)-DIFF: e.append(f'{L} unknown dimension '+','.join(sorted(set(d)-DIFF)))
        dec,basis,who=x.get('decision'),x.get('basis'),x.get('decided_by')
        if dec not in {'KEEP','REVISE','RECOMBINE','REJECT','PENDING'}: e.append(f'{L} invalid decision')
        if basis not in {'listened_by_user','audio_model','measured','inferred','pending'}: e.append(f'{L} invalid basis')
        if who not in {'user','director_provisional','pending'}: e.append(f'{L} invalid decided_by')
        if dec!='PENDING' and not x.get('reason'): e.append(f'{L} a decision needs a reason')
        if who=='user' and basis!='listened_by_user': e.append(f'{L} a user decision must rest on listening')
        if dec=='KEEP' and basis in {'measured','inferred'} and who!='director_provisional': e.append(f'{L} a KEEP from measurement or inference can only be provisional')
        if dec=='REVISE' and not x.get('revision_plan'): e.append(f'{L} REVISE needs a revision_plan')
        if dec=='RECOMBINE' and not x.get('recombine_sources'): e.append(f'{L} RECOMBINE needs recombine_sources')
        if not r.get('unrendered') and dec!='PENDING' and not x.get('render'): e.append(f'{L} judged without a render (mark the round unrendered)')
    keeps=[x.get('label') for x in c if isinstance(x,dict) and x.get('decision')=='KEEP']
    if len(keeps)>1: e.append('more than one KEEP')
    out=r.get('outcome')
    if keeps and out!=keeps[0]: e.append('outcome must name the KEEP')
    if not keeps and out in labels: e.append('outcome names a sketch that is not KEEP')
    return e
def main():
    a=argparse.ArgumentParser(); a.add_argument('kind',choices=REQUIRED); a.add_argument('files',nargs='+'); opt=a.parse_args(); bad=0
    for f in opt.files:
        try: record=json.loads(pathlib.Path(f).read_text()); errors=validate(opt.kind,record)
        except (ValueError,OSError) as exc: errors=[str(exc)]
        print(f, 'OK' if not errors else '; '.join(errors));bad+=bool(errors)
    return int(bool(bad))
if __name__=='__main__':sys.exit(main())
