import base64, os, glob, re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Media files are not part of this repository (see ASSETS.md). Place them in media/ and media-compressed/ to rebuild.
O=ROOT+'/src'; M=ROOT+'/media'; G=ROOT+'/media-compressed'
mime={'.webp':'image/webp','.mp3':'audio/mpeg','.woff':'font/woff','.wav':'audio/wav','.jpg':'image/jpeg'}
mp={}
# V1 sıkıştırılmış set (jpg→webp, wav→mp3, ttf→woff) orijinal anahtar adıyla
for f in sorted(os.listdir(G)):
    b,e=os.path.splitext(f)
    key=b+('.jpg' if e=='.webp' else '.ttf' if e=='.woff' else ('.wav' if os.path.exists(M+'/'+b+'.wav') else '.mp3'))
    mp[key]=(G+'/'+f,e)
SKIP=re.compile(r'^(metal-|hucre-\d|sure-cubuk-|Gemini-Rakamlar-1-4)')
for p in glob.glob(M+'/*.webp')+glob.glob(M+'/harf/*.webp'):
    key=os.path.relpath(p,M)
    if SKIP.match(os.path.basename(key)): continue
    mp[key]=(p,'.webp')
data={k:'data:'+mime[e]+';base64,'+base64.b64encode(open(p,'rb').read()).decode() for k,(p,e) in mp.items()}
order=['v1-entegrasyon.js','v1-tema.js','v1-sinema.js','v1-trol.js','v1-boss.js','v1-cehennem.js','v1-yazi.js','v1-menu.js','v1-perf.js','v1-dokunus.js','v1-denge.js']
src=''
for f in order:
    s=open(O+'/'+f).read()
    if f=='v1-entegrasyon.js':
        s=s.replace("const BASE = (globalThis.NEON_V1_BASE || 'media/');\n","const BASE = (globalThis.NEON_V1_BASE || 'media/');\n  const U = f => (globalThis.NEON_V1_MAP && globalThis.NEON_V1_MAP[f]) || BASE + f;\n")
        s=s.replace("i.src = BASE + src;","i.src = U(src);").replace("i.src = BASE + f; ART[k] = i;","i.src = U(f); ART[k] = i;").replace("fetch(BASE + f)","fetch(U(f))")
        for n in ['Oxanium.ttf','BarlowCondensed-Bold.ttf','BarlowCondensed-Medium.ttf']:
            s=s.replace("'url(' + BASE.replace(/media\\/$/, '') + 'fonts/"+n+")'","'url(' + U('"+n+"') + ')'")
        assert 'BASE +' not in s.replace('|| BASE + f',''), 'BASE kaldı'
    src+='\n'+s
head='if (!globalThis.NEON_V1_MAP) globalThis.NEON_V1_MAP = {\n'+',\n'.join('"%s":"%s"'%(k,v) for k,v in sorted(data.items()))+'\n};\n'
patch='/* Neon Sudoku V1.51 yama (medya gömülü) */\n'+head+src
open(ROOT+'/build/neon-yama.js','w').write(patch)
# telefon için tek dosya
h=open(ROOT+'/src/base-game.html',encoding='utf-8').read()
i=h.rfind('<script>const game=')
import re as _r
body=_r.sub(r'^<title>.*?</title><style>.*?</style>','',h,flags=_r.S)
j=body.rfind('<script>const game=')
tel='<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no"><meta name="theme-color" content="#070a1b"><title>Neon Sudoku V1.51</title><style>html,body{margin:0;height:100%;background:#070a1b;overflow:hidden;touch-action:manipulation}</style></head><body>'+body[:j]+'<script>'+patch+'</script>'+body[j:]+'</body></html>'
open(ROOT+'/index.html','w',encoding='utf-8').write(tel)
print(len(data),len(patch),len(tel))
