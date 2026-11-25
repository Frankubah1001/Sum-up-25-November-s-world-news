import os

content = r"""import sharp from 'sharp';

const W = 1024;
const H = 1024;

const INK      = { r: 10,  g: 15,  b: 30 };
const PANEL    = { r: 245, g: 247, b: 250 };
const PANEL2   = { r: 232, g: 236, b: 242 };
const ACCENT   = { r: 16,  g: 132, b: 203 };
const ACCENT2  = { r: 13,  g: 148, b: 136 };
const WARN     = { r: 217, g: 83,  b: 25 };
const INK2     = { r: 255, g: 255, b: 255 };
const MUTED    = { r: 110, g: 120, b: 135 };

async function roundedRect({ svg, x, y, w, h, r, fill }) {
  svg.push(`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" ry="${r}" fill="rgb(${fill.r},${fill.g},${fill.b})" />`);
}

async function text({ svg, x, y, str, fontSize, fill = INK, fontWeight = 600, anchor = 'start' }) {
  const a = anchor === 'middle' ? ' text-anchor="middle"' : '';
  const w = fontWeight === 600 ? 'font-weight="600"' : fontWeight === 700 ? 'font-weight="700"' : 'font-weight="400"';
  svg.push(`<text x="${x}" y="${y}" font-size="${fontSize}" font-family="Arial, Helvetica, sans-serif" ${w} fill="rgb(${fill.r},${fill.g},${fill.b})"${a}>${str}</text>`);
}
"""

path = '/Users/pitasonsmartpro/.cline/data/workspaces/chat/news-image-submission/generate-image.mjs'
with open(path, 'w') as f:
    f.write(content)
print(f'Wrote {len(content)} chars to {path}')