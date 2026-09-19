const puppeteer = require("puppeteer-core");
const fs = require("fs");

(async () => {
  const rawData = fs.readFileSync("/Users/mac/Downloads/Band-Performance-Proposal-Whitefield (1).html", "utf-8");
  const logoMatch = rawData.match(/src="(data:image\/[^;]+;base64,[^"]+)"/);
  const logoSrc = logoMatch ? logoMatch[1] : "";

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Band Performance Proposal - Whitefield</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;1,6..72,300;0,6..72,400&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    @page {
      size: A4 portrait;
      margin: 0;
    }
    html, body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #FAFAF8;
      color: #0B0B0B;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      margin: 0;
      padding: 0;
    }
    .display {
      font-family: 'Newsreader', Georgia, serif;
      font-weight: 300;
    }
    .page-container {
      width: 210mm;
      height: 297mm;
      min-height: 297mm;
      max-height: 297mm;
      background: #FFFFFF;
      margin: 0 auto;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      page-break-after: always;
      break-after: page;
      box-sizing: border-box;
    }
    @media print {
      body {
        background: transparent !important;
      }
      .page-container {
        box-shadow: none !important;
        margin: 0 !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
      }
    }
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            serif: ['Newsreader', 'serif']
          }
        }
      }
    }
  </script>
</head>
<body>

  <!-- ================= PAGE 1 ================= -->
  <div class="page-container">
    <div>
      <!-- Hero Banner -->
      <div class="bg-[#0B0B0B] px-12 py-10 flex flex-col items-center justify-center">
        <img src="${logoSrc}" alt="BOOMRANG - Experience The Fusion" class="w-[240px] h-auto object-contain select-none" />
        <div class="mt-5 w-[24px] h-[1px] bg-white/20"></div>
      </div>

      <!-- Proposal Header & Meta -->
      <div class="px-14 pt-8 pb-2">
        <div class="text-center">
          <p class="text-[10px] tracking-[0.28em] font-medium uppercase text-black/30">Proposal</p>
          <h1 class="display text-[34px] leading-[1.1] tracking-[-0.02em] text-[#0B0B0B] mt-2.5">Live Band<br>Performance</h1>
          <div class="mt-5 flex items-center justify-center gap-3 text-[11px] tracking-[0.18em] uppercase font-medium text-black/40">
            <span>Whitefield</span>
            <span class="w-[3px] h-[3px] rounded-full bg-black/20"></span>
            <span>18th / 19th October</span>
            <span class="w-[3px] h-[3px] rounded-full bg-black/20"></span>
            <span>2 Hours</span>
          </div>
        </div>

        <div class="mt-7 h-[1px] bg-black/[0.06]"></div>

        <!-- About -->
        <div class="mt-6">
          <p class="text-[10px] tracking-[0.2em] font-semibold uppercase text-black/30 mb-2.5">About</p>
          <p class="text-[14px] leading-[1.75] text-black/70 font-[400]">
            BOOMRANG — Experience The Fusion is a versatile live act bringing together retro to new age Bollywood with a perfect balance for all age groups.
          </p>
        </div>

        <!-- Lineup -->
        <div class="mt-7">
          <p class="text-[10px] tracking-[0.2em] font-semibold uppercase text-black/30 mb-3.5">Lineup — 5 Piece</p>
          <div class="border-t border-black/[0.08]">
            <div class="flex items-baseline justify-between py-[9px] border-b border-black/[0.06]">
              <span class="text-[13px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Male Vocalist</span>
              <span class="text-[10px] tracking-[0.16em] text-black/25 font-medium tabular-nums">01</span>
            </div>
            <div class="flex items-baseline justify-between py-[9px] border-b border-black/[0.06]">
              <span class="text-[13px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Female Vocalist</span>
              <span class="text-[10px] tracking-[0.16em] text-black/25 font-medium tabular-nums">02</span>
            </div>
            <div class="flex items-baseline justify-between py-[9px] border-b border-black/[0.06]">
              <span class="text-[13px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Guitarist</span>
              <span class="text-[10px] tracking-[0.16em] text-black/25 font-medium tabular-nums">03</span>
            </div>
            <div class="flex items-baseline justify-between py-[9px] border-b border-black/[0.06]">
              <span class="text-[13px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Keyboardist</span>
              <span class="text-[10px] tracking-[0.16em] text-black/25 font-medium tabular-nums">04</span>
            </div>
            <div class="flex items-baseline justify-between py-[9px] border-b border-black/[0.06]">
              <span class="text-[13px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Drummer</span>
              <span class="text-[10px] tracking-[0.16em] text-black/25 font-medium tabular-nums">05</span>
            </div>
          </div>
        </div>

        <!-- Curation -->
        <div class="mt-7 grid grid-cols-[140px_1fr] gap-6">
          <p class="text-[10px] tracking-[0.2em] font-semibold uppercase text-black/30 pt-1 leading-[1.6]">Performance<br>Curation</p>
          <div>
            <p class="display text-[18px] leading-[1.3] tracking-[-0.01em] text-[#0B0B0B]">Retro to New Age Bollywood —<br>classics to chartbusters.</p>
            <p class="mt-2 text-[12px] leading-[1.6] text-black/50">Sufi &amp; energetic dance numbers curated for all age groups. A journey from soulful retro to high-energy contemporary.</p>
          </div>
        </div>

      </div>
    </div>

    <!-- Page 1 Bottom Footer -->
    <div class="px-14 pb-6 flex justify-between items-center text-[9px] tracking-[0.18em] uppercase text-black/25 border-t border-black/[0.04] pt-3">
      <span>Boomrang · Live Band Performance</span>
      <span>Page 01 / 02</span>
    </div>
  </div>

  <!-- ================= PAGE 2 ================= -->
  <div class="page-container">
    <div class="px-14 pt-8 pb-0">
      <div class="flex items-start justify-between gap-6">
        <div>
          <p class="text-[10px] tracking-[0.24em] font-semibold uppercase text-black/30">02 — Rider</p>
          <h2 class="display text-[26px] leading-[1.1] tracking-[-0.02em] text-[#0B0B0B] mt-1.5">Technical Rider /<br>Stage Requirements</h2>
        </div>
        <div class="flex mt-1 h-[28px] w-[28px] border border-black/[0.08] items-center justify-center">
          <div class="h-[1px] w-[14px] bg-black/20 rotate-45"></div>
        </div>
      </div>
      <p class="mt-2.5 text-[11px] leading-[1.5] text-black/40 max-w-[420px]">Clean stage setup for 5-piece live. Please provide as per list below.</p>

      <!-- Technical Rider Table -->
      <div class="mt-4 border border-black/[0.08] overflow-hidden rounded-[1px]">
        <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#0B0B0B] text-white">
          <div class="px-4 py-[6px] text-[8.5px] tracking-[0.18em] uppercase font-medium">Item</div>
          <div class="px-4 py-[6px] text-[8.5px] tracking-[0.18em] uppercase font-medium border-l border-white/10">Quantity / Notes</div>
        </div>
        <div class="divide-y divide-black/[0.06] text-[10.5px]">
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Shure SM58 / SM57 microphones</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">5</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Mic stands</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">5</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Stage monitors</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">6</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Digital mixer</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">32-channel digital console with multitrack recording</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Extension boards on stage</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">4</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">DI boxes</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">5</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">DI boxes for guitars</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">2</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Lyric stands</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">2</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Laptop XLR</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">1</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">In-ear monitors</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">6</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Talkback mic</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">2</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">XLR for keyboard</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">4 DI boxes</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-white"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Laptop stands</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">1</div></div>
          <div class="grid grid-cols-[1.45fr_0.85fr] bg-[#FAFAF8]/50"><div class="px-4 py-[4.5px] tracking-[-0.01em] text-[#0B0B0B] font-[400]">Keyboard stands</div><div class="px-4 py-[4.5px] text-black/60 font-[400] border-l border-black/[0.06] tabular-nums">1</div></div>
        </div>
      </div>

      <!-- Stamp Badge -->
      <div class="mt-3.5 flex flex-col items-center justify-center gap-1.5 py-3 border border-dashed border-black/[0.08] bg-[#FAFAF8]/60">
        <img src="${logoSrc}" alt="BOOMRANG" class="w-[84px] h-auto object-contain opacity-[0.85] mix-blend-multiply select-none" />
        <div class="flex items-center gap-2">
          <div class="w-[12px] h-[1px] bg-black/15"></div>
          <p class="text-[8.5px] tracking-[0.32em] font-bold uppercase text-black/30">BOOMRANG · Technical Rider</p>
          <div class="w-[12px] h-[1px] bg-black/15"></div>
        </div>
      </div>

      <!-- Terms -->
      <div class="mt-3 pt-2.5 border-t border-black/[0.06]">
        <p class="text-[10px] leading-[1.5] text-black/35 tracking-wide text-center max-w-[380px] mx-auto">
          Dates are subject to availability.<br>Advance booking recommended to block the date.
        </p>
      </div>
    </div>

    <!-- CTA & Footer -->
    <div>
      <div class="bg-[#0B0B0B] px-8 py-7 flex flex-col items-center text-center">
        <p class="display text-[20px] leading-[1.2] tracking-[-0.01em] text-white">Let's make your evening<br><span class="italic opacity-60">unforgettable.</span></p>
        <div class="mt-4 w-full max-w-[240px] h-[1px] bg-white/10"></div>
        <div class="mt-4 space-y-1.5 text-center">
          <p class="uppercase tracking-[0.2em] text-[8.5px] text-white/25">For bookings &amp; enquiries</p>
          <a href="tel:+919738397933" class="block text-[14px] tracking-[0.04em] text-white/90 font-[400] tabular-nums">+91 97383 97933</a>
        </div>
      </div>
      <div class="py-2.5 flex justify-between items-center px-14 text-[8.5px] tracking-[0.16em] uppercase text-black/25 border-t border-black/[0.04]">
        <span>BOOMRANG · Experience The Fusion · Whitefield · Bangalore</span>
        <span>Page 02 / 02</span>
      </div>
    </div>
  </div>

</body>
</html>`;

  fs.writeFileSync("/tmp/generate_proposal.html", html);

  const browser = await puppeteer.launch({
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: "new",
    args: ["--no-sandbox", "--disable-gpu"]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 794, height: 1123, deviceScaleFactor: 2 });
  await page.goto("file:///tmp/generate_proposal.html", { waitUntil: "networkidle0" });
  await page.evaluateHandle("document.fonts.ready");

  // Generate the PDF
  const pdfBuffer = await page.pdf({
    format: "A4",
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
    preferCSSPageSize: true
  });

  const targetPath1 = "/Users/mac/Downloads/Band-Performance-Proposal-Whitefield (1).pdf";
  const targetPath2 = "/Users/mac/Downloads/Band-Performance-Proposal-Whitefield.pdf";
  fs.writeFileSync(targetPath1, pdfBuffer);
  fs.writeFileSync(targetPath2, pdfBuffer);

  console.log("Successfully written PDFs to:", targetPath1);
  await browser.close();
})();
