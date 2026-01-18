#!/usr/bin/env node
/* Offline, no-deps builder (Node built-ins only). */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SRC = path.join(ROOT, 'src');
const DIST = path.join(ROOT, 'dist');

const CSS_TOKEN = '/*__INJECT_CSS__*/';
const JS_TOKEN  = '/*__INJECT_JS__*/';

function read(p){ return fs.readFileSync(p, 'utf8'); }
function write(p, s){ fs.writeFileSync(p, s, 'utf8'); }

const template = read(path.join(SRC, 'template.html'));
if (!template.includes(CSS_TOKEN) || !template.includes(JS_TOKEN)) {
  console.error('Template is missing injection tokens');
  process.exit(1);
}
const css = read(path.join(SRC, 'styles.css'));
const js  = read(path.join(SRC, 'app.js'));

const out = template.replace(CSS_TOKEN, css).replace(JS_TOKEN, js);
fs.mkdirSync(DIST, { recursive: true });
write(path.join(DIST, 'index.html'), out);
write(path.join(ROOT, 'index.html'), out);
console.log('Built dist/index.html');
