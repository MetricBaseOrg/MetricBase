import os
import re

files_to_update = [
    'contact.html',
    'cookie-policy.html',
    'disclaimer.html',
    'editorial-standards.html',
    'privacy.html',
    'terms.html',
    'about.html',
    'journal.html',
    'journal/weekly-brief-1.html',
    'journal/weekly-brief-2.html',
    'journal/research-retail-trader-2026.html',
    'index.html'
]

nav_replacement = '''    <nav class="nav-links">
      <a href="https://metricbase.org/privacy">Privacy</a>
      <a href="https://metricbase.org/terms">Terms</a>
      <a href="https://metricbase.org/disclaimer">Disclaimer</a>
      <a href="https://metricbase.org/cookie-policy">Cookies</a>
      <a href="https://metricbase.org/editorial-standards">Editorial</a>
      <a href="https://metricbase.org/contact">Contact</a>
    </nav>'''

footer_replacement = '''        <h4>Legal</h4>
        <ul>
          <li><a href="https://metricbase.org/privacy">Privacy Policy</a></li>
          <li><a href="https://metricbase.org/terms">Terms of Service</a></li>
          <li><a href="https://metricbase.org/disclaimer">Disclaimer</a></li>
          <li><a href="https://metricbase.org/cookie-policy">Cookie Policy</a></li>
          <li><a href="https://metricbase.org/editorial-standards">Editorial Standards</a></li>
          <li><a href="https://metricbase.org/contact">Contact</a></li>
        </ul>'''

footer_metricbase_index_replacement = '''        <h4>MetricBase</h4>
        <ul>
          <li><a href="/journal">Journal</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="https://og.metricbase.org">OG-tools</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/terms">Terms of Service</a></li>
          <li><a href="/disclaimer">Disclaimer</a></li>
          <li><a href="/cookie-policy">Cookie Policy</a></li>
          <li><a href="/editorial-standards">Editorial Standards</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>'''

for f in files_to_update:
    path = os.path.join('D:\\\\OneDrive\\\\MetricBase\\\\MetricBase', f)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Nav replacement
    if f in ['contact.html', 'cookie-policy.html', 'disclaimer.html', 'editorial-standards.html', 'privacy.html', 'terms.html']:
        pattern_nav = re.compile(r'<nav class="nav-links">.*?</nav>', re.DOTALL)
        active_map = {
            'contact.html': 'https://metricbase.org/contact',
            'cookie-policy.html': 'https://metricbase.org/cookie-policy',
            'disclaimer.html': 'https://metricbase.org/disclaimer',
            'editorial-standards.html': 'https://metricbase.org/editorial-standards',
            'privacy.html': 'https://metricbase.org/privacy',
            'terms.html': 'https://metricbase.org/terms'
        }
        
        this_nav = nav_replacement.replace(
            f'href="{active_map[f]}"',
            f'href="{active_map[f]}" class="active"'
        )
        content = pattern_nav.sub(this_nav, content)
        
    # 2. Footer replacement
    if f == 'index.html':
        pattern_footer_mb = re.compile(r'<h4>MetricBase</h4>\s*<ul>.*?</ul>', re.DOTALL)
        content = pattern_footer_mb.sub(footer_metricbase_index_replacement, content)
    else:
        pattern_footer_legal = re.compile(r'<h4>Legal</h4>\s*<ul>.*?</ul>', re.DOTALL)
        content = pattern_footer_legal.sub(footer_replacement, content)
        
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated {f}')
