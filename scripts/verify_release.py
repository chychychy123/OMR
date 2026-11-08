"""CPU-only SHA, complete-matrix, resource, and reported-result validation."""
import csv, hashlib, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
read=lambda p: json.loads(p.read_text(encoding='utf-8'))
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def verify():
    checked=0
    manifest_path=ROOT/'provenance/release_manifest.json'
    if manifest_path.exists():
        for name,h in read(manifest_path).items():
            assert sha(ROOT/name)==h, name
            checked+=1
    config=read(ROOT/'configs/experiment.json')
    values=[]
    for env in config['datasets']:
        base=ROOT/'results/confirmation'/env
        manifest=read(base/'evidence_manifest.json')
        for stem in ('analysis','audit','rows','split'):
            assert sha(base/f'{stem}.json')==manifest[stem+'_sha256'], (env,stem)
        rows=read(base/'rows.json'); analysis=read(base/'analysis.json')
        assert len(rows)==6144 and read(base/'audit.json')['errors']==[]
        keys={(r['root'],r['method'],r['iterations'],r['head_seed'],r['planner_seed']) for r in rows}
        expected=set(); iterations=config['planning']['high_iterations'][env]
        for method,nheads in config['high_methods'].items():
            for head in config['head_seeds'] if nheads==3 else [0]:
                for seed in config['planning_seeds']:
                    for root in range(128): expected.add((root,method,iterations,head,seed))
        assert keys==expected and len(keys)==len(rows), env
        for row in analysis['table']:
            selected=[r for r in rows if r['method']==row['method'] and r['iterations']==row['iterations']]
            actual=100*sum(r['success'] for r in selected)/len(selected)
            assert abs(actual-row['success_percent'])<1e-10, (env,row['method'])
        main=next(r for r in analysis['table'] if r['method']=='refined_self' and r['iterations']==iterations)
        values.append(main['success_percent'])
        prep=read(ROOT/'resources'/env/'prepared.json')
        assert sha(ROOT/'resources'/env/'retrieval.npz')==prep['bank_sha256']
        for key,item in prep['models'].items():
            assert sha(ROOT/'resources'/env/'models'/f'{key}.pt')==item['sha256']
        print(f"{env:9s} {main['success_percent']:.6f}%  95% CI {main['success_root95']}")
    assert abs(sum(values)/4-90.10416666666664)<1e-9
    with (ROOT/'results/all_methods.csv').open(newline='',encoding='utf-8-sig') as f:
        task_rows=list(csv.DictReader(f))
    assert len(task_rows)==40
    with (ROOT/'results/controller_resources.csv').open(newline='',encoding='utf-8-sig') as f:
        resource_rows=list(csv.DictReader(f))
    assert len(resource_rows)==40
    macro=read(ROOT/'results/all_methods_macro.csv') if (ROOT/'results/all_methods_macro.csv').suffix=='.json' else None
    with (ROOT/'results/all_methods_macro.csv').open(newline='',encoding='utf-8-sig') as f:
        macro_rows=list(csv.DictReader(f))
    assert len(macro_rows)==10 and abs(float(next(r for r in macro_rows if r['method']=='refined_self')['success_percent'])-90.10416666666664)<1e-9
    print(json.dumps({'status':'passed','episodes_checked':24576,'macro_success_percent':sum(values)/4,
                      'task_rows_verified':len(task_rows),'macro_rows_verified':len(macro_rows),
                      'resource_rows_verified':len(resource_rows),'manifest_files_checked':checked,
                      'bootstrap_recomputed':False}))

if __name__=='__main__': verify()
