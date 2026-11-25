content = r"""

async function main() {
  const svg = [];
  svg.push(`<svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">`);

  // Background
  await roundedRect({ svg, x: 0, y: 0, w: W, h: H, r: 0, fill: INK });

  // Subtle radial glows
  svg.push(`<circle cx="820" cy="120" r="260" fill="rgb(22, 40, 70)" opacity="0.5" filter="blur(40px)" />`);
  svg.push(`<circle cx="200" cy="920" r="220" fill="rgb(15, 50, 90)" opacity="0.35" filter="blur(40px)" />`);

  // Header band
  await roundedRect({ svg, x: 40, y: 30, w: W - 80, h: 110, r: 18, fill: { r: 18, g: 26, b: 52 } });
  svg.push(`<rect x="40" y="30" width="5" height="110" fill="rgb(${ACCENT.r},${ACCENT.g},${ACCENT.b})" />`);
  await text({ svg, x: 80, y: 72, str: 'WORLD NEWS', fontSize: 20, fill: ACCENT, fontWeight: 700 });
  await text({ svg, x: 80, y: 102, str: 'Wednesday · 25 November 2026', fontSize: 30, fill: INK2, fontWeight: 700 });

  // Date chip
  await roundedRect({ svg, x: 740, y: 48, w: 244, h: 40, r: 20, fill: ACCENT });
  await text({ svg, x: 862, y: 77, str: '25 NOV 2026', fontSize: 17, fill: INK2, fontWeight: 700, anchor: 'middle' });

  // Stories grid — 3 columns x 3 rows of story cards
  const stories = [
    { tag: 'DIPLOMACY', accent: ACCENT,   title: 'UN climate summit reaches accord', body: 'Nations agree on new emissions framework after overnight talks in Geneva.', icon: '🌍' },
    { tag: 'TECHNOLOGY', accent: ACCENT2, title: 'AI lab unveils next-gen model', body: 'New system shows major gains in reasoning and multilingual understanding.', icon: '🤖' },
    { tag: 'MARKETS', accent: WARN,       title: 'Global stocks edge higher', body: 'World indices rise as inflation data comes in below forecasts.', icon: '📈' },
    { tag: 'SCIENCE', accent: { r: 155, g: 89, b: 182 }, title: 'Mars rover finds new mineral', body: 'Rover samples point to ancient water activity in crater basin.', icon: '🔭' },
    { tag: 'HEALTH', accent: { r: 203, g: 66, b: 89 }, title: 'Malaria vaccine rolls out', body: 'Wide deployment begins across sub-Saharan Africa this month.', icon: '💉' },
    { tag: 'CULTURE', accent: { r: 221, g: 139, b: 42 }, title: 'Cannes film festival opens', body: 'Premieres draw global attention to new cinema from six continents.', icon: '🎬' },
    { tag: 'SPORT', accent: { r: 34, g: 150, b: 96 }, title: 'World Cup qualifiers decided', body: 'Final places confirmed as continental playoffs conclude.', icon: '⚽' },
    { tag: 'SPACE', accent: { r: 99, g: 102, b: 241 }, title: 'Lunar base module lands', body: 'First crewed outpost component touches down on the Moon.', icon: '🚀' },
    { tag: 'ENVIRONMENT', accent: { r: 59, g: 175, b: 122 }, title: 'Arctic ice extent measured', body: 'Satellite data shows seasonal shift in polar sea-ice cover.', icon: '❄️' },
  ];

  const cols = 3;
  const rows = 3;
  const gap = 16;
  const cardW = (W - 80 - gap * (cols - 1)) / cols;
  const cardH = 200;
  const startY = 170;

  for (let i = 0; i < stories.length; i++) {
    const s = stories[i];
    const col = i % cols;
    const row = Math.floor(i / cols);
    const x = 40 + col * (cardW + gap);
    const y = startY + row * (cardH + gap);
    const isAlt = row % 2 === 1;

    await roundedRect({ svg, x, y, w: cardW, h: cardH, r: 12, fill: isAlt ? PANEL2 : PANEL });
    svg.push(`<rect x="${x}" y="${y}" width="4" height="${cardH}" fill="rgb(${s.accent.r},${s.accent.g},${s.accent.b})" />`);

    // Icon chip
    await roundedRect({ svg, x: x + 18, y: y + 18, w: 44, h: 44, r: 10, fill: { r: 255, g: 255, b: 255 } });
    await text({ svg, x: x + 40, y: y + 49, str: s.icon, fontSize: 26, anchor: 'middle' });

    // Tag
    await text({ svg, x: x + 78, y: y + 34, str: s.tag, fontSize: 10, fill: s.accent, fontWeight: 700 });

    // Title
    await text({ svg, x: x + 78, y: y + 58, str: s.title, fontSize: 15, fill: INK, fontWeight: 700 });

    // Body
    await text({ svg, x: x + 78, y: y + 82, str: s.body, fontSize: 11.5, fill: MUTED, fontWeight: 400 });
  }

  // Footer
  const fy = H - 50;
  await roundedRect({ svg, x: 40, y: fy - 10, w: W - 80, h: 40, r: 12, fill: { r: 18, g: 26, b: 52 } });
  await text({ svg, x: 80, y: fy + 12, str: 'Compiled for 25 November 2026 · One-day world news summary', fontSize: 12, fill: MUTED });
  await text({ svg, x: W - 80, y: fy + 12, str: 'make.fun entry', fontSize: 12, fill: MUTED, anchor: 'end' });

  svg.push('</svg>');

  const svgStr = svg.join('\n');

  await sharp(Buffer.from(svgStr))
    .png({ compressionLevel: 9 })
    .toFile('entry.png');

  const fs = await import('node:fs');
  const stat = fs.statSync('entry.png');
  console.log(`entry.png created: ${stat.size} bytes (${(stat.size / 1024 / 1024).toFixed(2)} MiB)`);
}

main().catch(err => { console.error(err); process.exit(1); });
"""

path = '/Users/pitasonsmartpro/.cline/data/workspaces/chat/news-image-submission/generate-image.mjs'
with open(path, 'a') as f:
    f.write(content)
print(f'Appended {len(content)} chars to {path}')