import re

WEBHOOK = 'https://script.google.com/macros/s/AKfycbwiYK9LDhZdbx3-r66rgRmfTClEyfH0VOWMFtKPw5nSzd_YRV7YETaqTVrOCaxpn7zNtg/exec'

LOG_SCRIPT = (
    '<script id="qs-calc-logger">\n'
    '(function(){\n'
    'var WEBHOOK="' + WEBHOOK + '",_t=null;\n'
    'window.qsLogCalc=function(tool,data){\n'
    '    clearTimeout(_t);\n'
    '    _t=setTimeout(function(){\n'
    '        var s=sessionStorage.getItem("qs_user_"+tool),name="",email="";\n'
    '        if(s){try{var d=JSON.parse(s);name=d.name||"";email=d.email||"";}catch(e){}}\n'
    '        if(!name)return;\n'
    '        var p={type:"calculation",name:name,email:email,tool:tool,timestamp:new Date().toISOString(),url:location.href,data:data};\n'
    '        try{navigator.sendBeacon(WEBHOOK,JSON.stringify(p));}catch(e){}\n'
    '    },2000);\n'
    '};\n'
    '})();\n'
    '</script>'
)

def read_all_inputs_js(tkey):
    return (
        'if(window.qsLogCalc) qsLogCalc("' + tkey + '", {'
        'inputs: Array.from(document.querySelectorAll("input[id],select[id]")).reduce(function(a,el){a[el.id]=el.value;return a;},{}), '
        'results: Array.from(document.querySelectorAll("[id^=r-],[id*=result],[id*=Result],[id*=total],[id*=Total],[id*=verdict]")).reduce(function(a,el){a[el.id]=el.textContent.trim();return a;},{})'
        '});'
    )

def insert_log(js, func_name, tkey):
    pat = r'(function\s+' + re.escape(func_name) + r'\s*\([^)]*\)\s*\{)'
    m = re.search(pat, js)
    if not m:
        return js, False
    depth, i = 0, m.end() - 1
    while i < len(js):
        ch = js[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                call = '\n    ' + read_all_inputs_js(tkey) + '\n'
                js = js[:i] + call + js[i:]
                return js, True
        i += 1
    return js, False

TOOLS = [
    ('tool-salary-calculator.html', 'salary', 'recalculate'),
    ('tool-home-loan-calculator.html', 'home_loan', 'calculate'),
    ('tool-artha-wealth.html', 'artha_wealth', 'calculate'),
    ('tool-job-transition.html', 'job_transition', 'calculate'),
    ('tool-buy-vs-rent.html', 'buy_vs_rent', 'calc'),
]

for fname, tkey, tfunc in TOOLS:
    fp = 'd:\\Vibe Code\\Quantum Step\\' + fname
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'qs-calc-logger' in html:
        print('SKIP (already injected): ' + fname)
        continue

    # Inject the logger script block before </body>
    html = html.replace('</body>', LOG_SCRIPT + '\n</body>', 1)

    # Inject the log call into the calc function
    html, ok = insert_log(html, tfunc, tkey)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)

    status = 'OK' if ok else 'WARN(func not hooked - logger still added)'
    print(status + ': ' + fname)

print('\nDone.')
