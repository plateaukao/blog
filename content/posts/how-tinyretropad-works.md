+++
title = "How TinyRetroPad Works — a Notepad Clone in 2,794 Bytes of Assembly"
date = "2026-06-10T00:00:00+08:00"
description = "A deep dive into trpad.asm: how a complete Windows Notepad clone — menus, dialogs, printing, find & replace — fits in 2,794 bytes of x86 MASM assembly, with diagrams of the architecture, message loop, and the Crinkler build pipeline."
summary = "A complete Windows Notepad clone — menus, dialogs, printing, find & replace, drag-and-drop — in 2,794 bytes. A Win95-styled walkthrough of trpad.asm: the RICHEDIT50W wrapper idea, the MASM + Crinkler build, the message loop, WndProc, and the byte-shaving playbook."
slug = "how-tinyretropad-works"
tags = ["Assembly", "Windows", "Programming"]
layout = "report"
[cover]
  hidden = true
+++
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>trpad.asm — How a 2,794-byte Notepad Works</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">

<style>
  :root {
    --desktop: #008080;
    --face: #c0c0c0;
    --face-light: #dfdfdf;
    --face-dark: #808080;
    --shadow: #0a0a0a;
    --title-a: #000080;
    --title-b: #1084d0;
    --ink: #111;
    --paper: #fffef7;
    --accent: #000080;
    --ui-font: Tahoma, "Segoe UI", Geneva, Verdana, sans-serif;
    --mono: "IBM Plex Mono", "Courier New", monospace;
    --px: "Silkscreen", monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    background-color: var(--desktop);
    /* classic teal with a faint dither texture */
    background-image:
      repeating-conic-gradient(rgba(255,255,255,.025) 0% 25%, transparent 0% 50%);
    background-size: 4px 4px;
    font-family: var(--ui-font);
    font-size: 14px;
    color: var(--ink);
    padding: 28px 16px 96px;
    cursor: default;
  }
  .desk { max-width: 880px; margin: 0 auto; }
  /* ---------- window chrome ---------- */
  .window {
    background: var(--face);
    box-shadow:
      inset -1px -1px var(--shadow),
      inset 1px 1px var(--face-light),
      inset -2px -2px var(--face-dark),
      inset 2px 2px #fff,
      6px 6px 0 rgba(0,0,0,.35);
    padding: 3px;
    margin: 0 0 34px;
  }
  .window:nth-of-type(even)  { transform: rotate(.18deg); }
  .window:nth-of-type(odd)   { transform: rotate(-.14deg); }
  .window:hover { transform: none; }
  .titlebar {
    display: flex; align-items: center; gap: 8px;
    background: linear-gradient(90deg, var(--title-a), var(--title-b));
    color: #fff;
    padding: 4px 6px;
    font-weight: bold;
    font-size: 13px;
    letter-spacing: .02em;
    user-select: none;
  }
  .titlebar .ticon {
    width: 16px; height: 16px; flex: 0 0 16px;
    background: #fff;
    box-shadow: inset 0 0 0 2px var(--title-a), inset 0 0 0 3px #fff;
    image-rendering: pixelated;
  }
  .titlebar .tt { flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
  .tbtns { display: flex; gap: 2px; }
  .tbtn {
    width: 18px; height: 16px;
    background: var(--face);
    box-shadow: inset -1px -1px var(--shadow), inset 1px 1px #fff,
                inset -2px -2px var(--face-dark), inset 2px 2px var(--face-light);
    color: #000; font-family: var(--px); font-size: 8px;
    display: grid; place-items: center; line-height: 1;
  }
  .tbtn:active { box-shadow: inset 1px 1px var(--shadow), inset -1px -1px #fff; }
  .menubar {
    display: flex; gap: 2px;
    padding: 3px 4px 2px;
    border-bottom: 1px solid var(--face-dark);
    box-shadow: 0 1px 0 #fff;
    font-size: 13px;
  }
  .menubar span { padding: 2px 7px; }
  .menubar span u { text-decoration: underline; }
  .menubar span:hover { background: var(--title-a); color: #fff; }
  .pane { padding: 18px 22px 22px; }
  /* ---------- typography ---------- */
  h1, h2 {
    font-family: var(--px);
    color: var(--accent);
    line-height: 1.25;
    margin: 0 0 14px;
  }
  h1 { font-size: 26px; }
  h2 { font-size: 17px; }
  h3 {
    font-family: var(--ui-font);
    font-size: 14px;
    margin: 22px 0 8px;
    padding-bottom: 3px;
    border-bottom: 1px solid var(--face-dark);
    box-shadow: 0 1px 0 #fff;
  }
  p, li { line-height: 1.62; margin-bottom: 10px; }
  ul, ol { margin: 0 0 12px 22px; }
  li { margin-bottom: 6px; }
  a { color: var(--title-a); }
  strong { color: #000; }
  .small { font-size: 12px; color: #333; }
  code {
    font-family: var(--mono);
    font-size: 12.5px;
    background: #fff;
    padding: 1px 5px;
    box-shadow: inset 1px 1px var(--face-dark), inset -1px -1px #fff;
    white-space: nowrap;
  }
  /* sunken white panels: code blocks + diagrams */
  pre.code, .sunken {
    background: var(--paper);
    box-shadow: inset -1px -1px #fff, inset 1px 1px var(--shadow),
                inset -2px -2px var(--face-light), inset 2px 2px var(--face-dark);
    padding: 14px 16px;
    margin: 12px 0 16px;
    overflow-x: auto;
  }
  pre.code {
    font-family: var(--mono);
    font-size: 12.5px;
    line-height: 1.55;
    tab-size: 8;
  }
  pre.code .c  { color: #1f7a1f; font-style: italic; }   /* comment */
  pre.code .k  { color: #00009f; font-weight: 600; }     /* mnemonic */
  pre.code .l  { color: #9c2700; }                       /* label */
  pre.code .n  { color: #7a0c7a; }                       /* number/const */
  .caption {
    font-family: var(--px);
    font-size: 9px;
    color: #fff;
    background: var(--face-dark);
    display: inline-block;
    padding: 3px 8px;
    margin: -6px 0 14px;
  }
  /* mermaid containers */
  .diagram { text-align: center; padding: 18px 8px; }
  .diagram svg { max-width: 100%; height: auto; }
  /* ---------- ascii hero ---------- */
  pre.ascii {
    font-family: var(--mono);
    font-size: clamp(7px, 1.55vw, 13px);
    line-height: 1.18;
    color: #fff;
    background: #000084;
    padding: 18px 20px 14px;
    box-shadow: inset -1px -1px #fff, inset 1px 1px var(--shadow);
    overflow-x: auto;
    margin-bottom: 14px;
  }
  pre.ascii .dim { color: #6fb7ff; }
  .cursor::after {
    content: "▌";
    animation: blink 1.06s steps(1) infinite;
    color: #fff;
  }
  @keyframes blink { 50% { opacity: 0; } }
  .statusrow {
    display: flex; gap: 3px;
    padding: 3px;
    font-size: 12px;
  }
  .statusrow .cell {
    box-shadow: inset 1px 1px var(--face-dark), inset -1px -1px #fff;
    padding: 3px 10px;
    white-space: nowrap;
  }
  .statusrow .cell.grow { flex: 1; overflow: hidden; }
  /* ---------- tables ---------- */
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0 16px;
    font-size: 13px;
    background: var(--paper);
    box-shadow: inset -1px -1px #fff, inset 1px 1px var(--shadow);
  }
  th {
    background: var(--face);
    font-family: var(--px);
    font-size: 9px;
    text-align: left;
    padding: 7px 10px;
    border: 1px solid var(--face-dark);
  }
  td { padding: 6px 10px; border: 1px solid #cfcabc; vertical-align: top; line-height: 1.5; }
  td code { box-shadow: none; background: #efece0; }
  .num { text-align: right; font-family: var(--mono); white-space: nowrap; }
  /* byte badge */
  .byte-badge {
    font-family: var(--px);
    font-size: 11px;
    background: #ffff00;
    color: #000;
    border: 2px solid #000;
    padding: 6px 12px;
    display: inline-block;
    box-shadow: 3px 3px 0 #000;
    margin: 4px 0 12px;
  }
  /* dialog aside */
  .dialog {
    max-width: 560px;
    margin: 18px auto;
    background: var(--face);
    box-shadow: inset -1px -1px var(--shadow), inset 1px 1px var(--face-light),
                inset -2px -2px var(--face-dark), inset 2px 2px #fff,
                5px 5px 0 rgba(0,0,0,.3);
    padding: 3px;
  }
  .dialog .body { padding: 16px 18px; display: flex; gap: 14px; align-items: flex-start; }
  .dialog .q {
    width: 32px; height: 32px; flex: 0 0 32px; border-radius: 50%;
    background: #fff; color: var(--title-a);
    font: bold 22px/32px var(--ui-font); text-align: center;
    box-shadow: inset -2px -2px var(--face-dark), 1px 1px 0 var(--face-dark);
  }
  .btnrow { display: flex; gap: 8px; justify-content: center; padding: 0 0 14px; }
  .btn95 {
    font-family: var(--ui-font); font-size: 13px;
    min-width: 78px; padding: 5px 14px;
    background: var(--face);
    border: none;
    box-shadow: inset -1px -1px var(--shadow), inset 1px 1px #fff,
                inset -2px -2px var(--face-dark), inset 2px 2px var(--face-light);
  }
  .btn95:active { box-shadow: inset 1px 1px var(--shadow), inset -1px -1px #fff; padding: 6px 13px 4px 15px; }
  /* taskbar */
  .taskbar {
    position: fixed; left: 0; right: 0; bottom: 0; z-index: 50;
    background: var(--face);
    box-shadow: inset 0 1px #fff, 0 -1px var(--shadow);
    display: flex; align-items: center; gap: 6px;
    padding: 4px 6px;
    font-size: 12.5px;
  }
  .start {
    display: flex; align-items: center; gap: 6px;
    font-weight: bold;
    padding: 3px 10px 3px 7px;
    background: var(--face);
    box-shadow: inset -1px -1px var(--shadow), inset 1px 1px #fff,
                inset -2px -2px var(--face-dark), inset 2px 2px var(--face-light);
  }
  .start .flag { font-family: var(--px); font-size: 10px; color: var(--title-a); }
  .task {
    flex: 0 1 260px;
    padding: 3px 10px;
    box-shadow: inset 1px 1px var(--shadow), inset -1px -1px #fff,
                inset 2px 2px var(--face-dark);
    background: var(--face-light);
    font-weight: bold;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .tray {
    margin-left: auto;
    padding: 3px 12px;
    box-shadow: inset 1px 1px var(--face-dark), inset -1px -1px #fff;
    font-family: var(--mono); font-size: 12px;
    white-space: nowrap;
  }
  /* table of contents chips */
  .toc { display: flex; flex-wrap: wrap; gap: 8px; margin: 4px 0 6px; }
  .toc a {
    font-family: var(--px); font-size: 9px;
    text-decoration: none; color: #000;
    background: var(--face);
    padding: 6px 10px;
    box-shadow: inset -1px -1px var(--shadow), inset 1px 1px #fff,
                inset -2px -2px var(--face-dark), inset 2px 2px var(--face-light);
  }
  .toc a:active { box-shadow: inset 1px 1px var(--shadow), inset -1px -1px #fff; }
  @media (max-width: 640px) {
    body { padding: 14px 8px 84px; }
    .pane { padding: 14px 14px 18px; }
    .task { display: none; }
  }
</style>
</head>
<body>
<div class="desk">
  <!-- ============ HERO ============ -->
  <section class="window" style="transform:none">
    <div class="titlebar"><span class="ticon"></span><span class="tt">Untitled - TinyRetroPad</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span>
    </div>
    <div class="menubar"><span><u>F</u>ile</span><span><u>E</u>dit</span><span>F<u>o</u>rmat</span><span><u>V</u>iew</span><span><u>H</u>elp</span></div>
    <div class="pane">
<pre class="ascii">  _____      _             _____          _
 |  __ \    | |           |  __ \        | |
 | |__) |___| |_ _ __ ___ | |__) |_ _  __| |
 |  _  // _ \ __| '__/ _ \|  ___/ _` |/ _` |
 | | \ \  __/ |_| | | (_) | |  | (_| | (_| |
 |_|  \_\___|\__|_|  \___/|_|   \__,_|\__,_|
 <span class="dim">T I N Y  X 8 6   D E S K T O P   E D I T O R</span><span class="cursor"></span></pre>
      <h1>How trpad.asm works</h1>
      <p>
        <strong>TinyRetroPad</strong> is a real, working Windows text editor — menus, dialogs, printing,
        find &amp; replace, drag-and-drop file open — whose entire executable is
        <strong>2,794 bytes</strong>. That's smaller than this paragraph's screenshot.
        It is written in a single 2,687-line x86 MASM assembly file,
        <a href="https://github.com/PlummersSoftwareLLC/TinyRetroPad/blob/main/trpad.asm">trpad.asm</a>,
        and forked from Matt Power's <em>Dave's Tiny Editor</em>, itself grown from Dave Plummer's
        <code>tiny.asm</code> / HelloAssembly.
      </p>
      <div class="byte-badge">★ 2,794 BYTES — THE WHOLE APP ★</div>
      <p>This page walks through the entire program: the big idea, the build pipeline, the data and
         code layout, startup, the message loop, the window procedure, every feature, and the
         byte-shaving tricks that keep it tiny.</p>
      <div class="toc">
        <a href="#idea">1·THE BIG IDEA</a>
        <a href="#build">2·BUILD</a>
        <a href="#anatomy">3·ANATOMY</a>
        <a href="#startup">4·STARTUP</a>
        <a href="#loop">5·MSG LOOP</a>
        <a href="#wndproc">6·WNDPROC</a>
        <a href="#features">7·FEATURES</a>
        <a href="#tricks">8·SIZE TRICKS</a>
      </div>
    </div>
    <div class="statusrow"><span class="cell grow">For Help, press F1</span><span class="cell">Ln 1, Col 1</span></div>
  </section>
  <!-- ============ 1 THE BIG IDEA ============ -->
  <section class="window" id="idea">
    <div class="titlebar"><span class="ticon"></span><span class="tt">1 — The Big Idea: don't write an editor, borrow one</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p>
        TinyRetroPad writes <strong>zero</strong> text-editing code. No buffer management, no caret
        drawing, no clipboard handling, no undo stack, no word-wrap algorithm, no print
        rasterization. All of that lives inside <strong>RICHEDIT50W</strong> — the modern Rich Edit
        control shipped in every copy of Windows as <code>Msftedit.dll</code>.
      </p>
      <p>
        The program is, in its own README's words, <em>"basically a wrapper around the RICHEDIT50W
        control."</em> Its job is reduced to three things:
      </p>
      <ol>
        <li><strong>Create</strong> one main window with the Rich Edit control filling its client area.</li>
        <li><strong>Route</strong> menu clicks and keystrokes into <code>SendMessage</code> calls
            (<code>WM_CUT</code>, <code>EM_FINDTEXTEXA</code>, <code>EM_FORMATRANGE</code>, …) aimed at that control.</li>
        <li><strong>Borrow</strong> every dialog — Open, Save, Font, Find, Replace, Print, Page Setup —
            from <code>comdlg32</code>, the Windows common-dialog library.</li>
      </ol>
      <div class="sunken diagram">
<pre class="mermaid">
flowchart TB
    subgraph EXE["trpad.exe (2,794 bytes)"]
        MAIN["MainEntry&lt;br/&gt;message loop + Ctrl-key accelerators"]
        WP["WndProc&lt;br/&gt;flat cmp/je message dispatcher"]
        HP["Helper procs&lt;br/&gt;SaveFile, LoadStartupFile, PrintDoc,&lt;br/&gt;DoFindNext, BuildTitle, ToggleWrap ..."]
    end
    subgraph OS["Windows does the heavy lifting"]
        RE["RICHEDIT50W control (Msftedit.dll)&lt;br/&gt;all editing, undo, clipboard, wrap, print render"]
        CD["comdlg32 common dialogs&lt;br/&gt;Open / Save / Font / Find / Replace / Print / Page Setup"]
        K32["kernel32&lt;br/&gt;CreateFile, ReadFile, WriteFile, GlobalAlloc"]
        U32["user32&lt;br/&gt;window, menus, MessageBox, STATIC status bar"]
    end
    MAIN --&gt;|DispatchMessage| WP
    WP --&gt; HP
    HP --&gt;|SendMessage EM_xxx| RE
    HP --&gt; CD
    HP --&gt; K32
    WP --&gt; U32
</pre>
      </div>
      <span class="caption">FIG 1 · 2.7KB OF GLUE AROUND MEGABYTES OF WINDOWS</span>
      <h3>The growth log: every feature has a price tag</h3>
      <p>The file header keeps an honest ledger of what each feature cost. The bare RICHEDIT wrapper
         was 981 bytes; everything else was added a few hundred bytes at a time:</p>
      <table>
        <tr><th>Feature added</th><th style="text-align:right">Total bytes</th></tr>
        <tr><td>FILE menus</td><td class="num">1,375</td></tr>
        <tr><td>EDIT menus</td><td class="num">1,428</td></tr>
        <tr><td>Expanded FILE menus (Open / Save As)</td><td class="num">1,517</td></tr>
        <tr><td>HELP menus</td><td class="num">1,557</td></tr>
        <tr><td>FILE save-prompt flow ("Save changes?")</td><td class="num">1,622</td></tr>
        <tr><td>EDIT Time/Date</td><td class="num">1,668</td></tr>
        <tr><td>FORMAT Word Wrap</td><td class="num">1,694</td></tr>
        <tr><td>Right-click context menu</td><td class="num">1,779</td></tr>
        <tr><td>FORMAT Font dialog</td><td class="num">1,910</td></tr>
        <tr><td>EDIT Find / Find Next / Replace</td><td class="num">2,143</td></tr>
        <tr><td>FILE Print</td><td class="num">2,476</td></tr>
        <tr><td>VIEW status bar (Ln/Col)</td><td class="num">2,476</td></tr>
        <tr><td>DIALOG-based Go To</td><td class="num">2,686</td></tr>
        <tr><td>Keyboard accelerators</td><td class="num"><strong>2,794</strong></td></tr>
      </table>
      <p class="small">The status bar registered as "free" because Crinkler's compression absorbed
         it — more on that below.</p>
    </div>
  </section>
  <!-- ============ 2 BUILD ============ -->
  <section class="window" id="build">
    <div class="titlebar"><span class="ticon"></span><span class="tt">2 — Build pipeline: MASM + Crinkler</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p>The whole build is two commands in <code>build.bat</code>:</p>
<pre class="code"><span class="k">ml</span> /nologo /c /coff /Cp /IC:\masm32\include trpad.asm
&nbsp;
<span class="k">crinkler</span> trpad.obj /OUT:trpad.exe /ENTRY:MainEntry /SUBSYSTEM:WINDOWS
    /NOINITIALIZERS /TINYIMPORT /ORDERTRIES:2000
    kernel32.lib user32.lib shell32.lib comdlg32.lib gdi32.lib</pre>
      <div class="sunken diagram">
<pre class="mermaid">
flowchart LR
    SRC["trpad.asm&lt;br/&gt;2,687 lines MASM"] --&gt;|"ml /c /coff /Cp"| OBJ["trpad.obj&lt;br/&gt;COFF object"]
    OBJ --&gt; CR["Crinkler&lt;br/&gt;compressing linker"]
    L1["kernel32.lib user32.lib&lt;br/&gt;shell32.lib comdlg32.lib gdi32.lib"] --&gt; CR
    CR --&gt;|"/TINYIMPORT /NOINITIALIZERS&lt;br/&gt;/ORDERTRIES:2000 /ENTRY:MainEntry"| EXE["trpad.exe&lt;br/&gt;2,794 bytes"]
</pre>
      </div>
      <span class="caption">FIG 2 · THE TWO-STEP BUILD</span>
      <p>
        <strong>Crinkler</strong> is the secret weapon. It is not a normal linker — it's a
        <em>compressing</em> linker from the demoscene. Instead of emitting a standard PE layout
        (which costs ~1KB in headers alone), it produces an executable whose header doubles as a
        decompression stub: at run time the program literally decompresses itself into memory
        using a context-modeling compressor, then jumps to <code>MainEntry</code>. Flags that matter:
      </p>
      <ul>
        <li><code>/TINYIMPORT</code> — replaces the normal PE import table with compressed hashes of
            DLL function names, resolved by the stub at startup. This is why the assembly declares
            imports the unusual way it does (next section), and also why antivirus engines
            distrust Crinkler output: self-decompressing code that hash-resolves its own imports
            is what packers used by malware do too. The README warns Defender may eat the EXE.</li>
        <li><code>/NOINITIALIZERS</code> — no CRT, no constructors. The program never links a C runtime;
            <code>MainEntry</code> is raw machine code from instruction one.</li>
        <li><code>/ORDERTRIES:2000</code> — Crinkler reorders code/data sections 2,000 times searching for
            the ordering that compresses best. Compression context is shared, so a "free" feature
            (like the status bar's 0-byte cost) happens when new code resembles existing code
            closely enough to compress to almost nothing.</li>
      </ul>
    </div>
  </section>
  <!-- ============ 3 ANATOMY ============ -->
  <section class="window" id="anatomy">
    <div class="titlebar"><span class="ticon"></span><span class="tt">3 — Anatomy of the file</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p>The file has the classic MASM two-segment shape — a <code>.DATA</code> section and a
         <code>.CODE</code> section — preceded by directives and constants:</p>
      <table>
        <tr><th>Region</th><th>Lines</th><th>What lives there</th></tr>
        <tr><td>Directives</td><td class="num">39–41</td>
            <td><code>.386</code>, <code>.model flat, stdcall</code> — 32-bit flat memory, callee-cleans-stack calling convention (every Win32 API is stdcall).</td></tr>
        <tr><td>Feature switches</td><td class="num">49–50</td>
            <td><code>FEAT_LINENUMBERS</code> and <code>FEAT_DARKMODE</code>, assembly-time <code>IF</code> flags. At 0 the optional code isn't merely disabled — it is never assembled, so the baseline binary is byte-identical.</td></tr>
        <tr><td>Constants</td><td class="num">62–147</td>
            <td>Window size, Rich Edit message numbers (<code>EM_SETCHARFORMAT = WM_USER+68</code>, …) defined by hand rather than pulling in a big include, and every menu command ID (<code>IDM_FILE_OPEN = 0E202h</code>, …).</td></tr>
        <tr><td><code>.DATA</code></td><td class="num">149–351</td>
            <td>Import declarations, all strings (menu labels, captions), global state, an in-memory dialog template, and a prebuilt <code>CHARFORMATW</code> selecting Courier.</td></tr>
        <tr><td><code>.CODE</code></td><td class="num">355–2687</td>
            <td>~25 procedures: helpers, <code>MainEntry</code>, and <code>WndProc</code>.</td></tr>
      </table>
      <h3>Imports without an import library</h3>
      <p>Instead of <code>includelib</code> + <code>invoke</code>, every API is declared as a raw pointer to
         its import-address-table slot, and called through that pointer:</p>
<pre class="code"><span class="c">; declare (in .DATA)</span>
<span class="k">EXTERN</span> _imp__CreateWindowExA@48 :<span class="n">PTR</span>   <span class="c">; the @48 = 48 bytes of stdcall args</span>
&nbsp;
<span class="c">; call (anywhere) - push args right-to-left, then:</span>
<span class="k">call</span>    [_imp__CreateWindowExA@48]</pre>
      <p>This is exactly the shape Crinkler's <code>/TINYIMPORT</code> wants: each call is an indirect
         call through a 4-byte slot the decompression stub fills in at startup. The decorated name
         encodes the argument byte count, so the linker can match it against the real
         <code>kernel32.lib</code>/<code>user32.lib</code> symbols.</p>
      <h3>Global state: seven variables run the whole app</h3>
      <table>
        <tr><th>Variable</th><th>Purpose</th></tr>
        <tr><td><code>hMain</code> / <code>hEdit</code> / <code>hStatus</code></td><td>Window handles: frame, Rich Edit, status pane.</td></tr>
        <tr><td><code>CmdFile</code> (128 bytes)</td><td>THE current file path. Shared by command-line parsing, the Open dialog, the Save dialog, load and save. One buffer, five users.</td></tr>
        <tr><td><code>fDirty</code></td><td>Set on the first <code>EN_CHANGE</code>; drives the title-bar and the "Save changes?" prompt.</td></tr>
        <tr><td><code>fWrap</code> / <code>fStatus</code></td><td>Word-wrap and status-bar toggles.</td></tr>
        <tr><td><code>fr</code> / <code>FindWhat</code> / <code>ReplaceWith</code></td><td>The shared <code>FINDREPLACEA</code> request used by the modeless Find and Replace dialogs.</td></tr>
      </table>
      <h3>A dialog with no resources</h3>
      <p>The Go To dialog is not an <code>.rc</code> resource (resources cost a whole PE section). It is a
         <code>DLGTEMPLATE</code> built by hand in <code>.DATA</code> as raw dwords and words — caption
         <code>"Go To"</code> spelled out as <code>dw 'G','o',' ','T','o',0</code>, an <code>ES_NUMBER</code> edit
         box, and an OK button, referenced by the ordinal atoms <code>0081h</code> (Edit) and
         <code>0080h</code> (Button). <code>DialogBoxIndirectParamA</code> happily eats it from memory.</p>
<pre class="code">GoToTmpl <span class="k">LABEL</span> <span class="n">DWORD</span>
    <span class="k">dd</span>  DS_MODALFRAME <span class="k">or</span> WS_POPUP <span class="k">or</span> WS_CAPTION <span class="k">or</span> WS_SYSMENU
    <span class="k">dw</span>  <span class="n">2</span>                      <span class="c">; control count</span>
    <span class="k">dw</span>  <span class="n">0,0,150,46</span>             <span class="c">; x,y,cx,cy</span>
    <span class="k">dw</span>  <span class="l">'G','o',' ','T','o'</span>,<span class="n">0</span>  <span class="c">; caption, hand-spelled UTF-16</span>
    ...
    <span class="k">dw</span>  <span class="n">0FFFFh,0081h</span>           <span class="c">; "class is the Edit atom"</span></pre>
    </div>
  </section>
  <!-- ============ 4 STARTUP ============ -->
  <section class="window" id="startup">
    <div class="titlebar"><span class="ticon"></span><span class="tt">4 — Startup: MainEntry</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p>Execution begins at <code>MainEntry</code> (line 1794) — remember, there is no C runtime.
         Startup is a straight line:</p>
      <div class="sunken diagram">
<pre class="mermaid">
flowchart TD
    A["MainEntry"] --&gt; B["GetModuleHandle - HINSTANCE"]
    B --&gt; C["LoadLibrary 'Msftedit'&lt;br/&gt;registers RICHEDIT50W class"]
    C --&gt; D["RegisterWindowMessage 'commdlg_FindReplace'&lt;br/&gt;saved in uFindMsg"]
    D --&gt; E["zero WNDCLASS, set WndProc + class name '.'&lt;br/&gt;RegisterClassA"]
    E --&gt; F["ParseStartupFile&lt;br/&gt;scan GetCommandLine for a dropped file path"]
    F --&gt; G["CreateWindowExA 800x640&lt;br/&gt;WS_OVERLAPPEDWINDOW or WS_VISIBLE"]
    G --&gt;|"WM_CREATE fires inside WndProc"| H["create RICHEDIT50W child&lt;br/&gt;set event mask, raise text limit&lt;br/&gt;append Save to system menu&lt;br/&gt;CreateNotepadMenus, STATIC status bar"]
    H --&gt; I["LoadStartupFile&lt;br/&gt;read file into control if path given"]
    I --&gt; J["ApplyTitle - 'name - TinyRetroPad'"]
    J --&gt; K["message loop until WM_QUIT"]
    K --&gt; L["ExitProcess"]
</pre>
      </div>
      <span class="caption">FIG 3 · COLD START TO MESSAGE LOOP</span>
      <p>Details worth noticing:</p>
      <ul>
        <li><strong>The window class is named <code>"."</code></strong> — one byte plus terminator.
            The same string is reused as both class name <em>and</em> initial window title in the
            <code>CreateWindowExA</code> call, because the real title is set moments later by
            <code>ApplyTitle</code> anyway. The comment admits: <em>"save bytes here (seems to work)."</em></li>
        <li><strong><code>LoadLibrary("Msftedit")</code></strong> — no <code>.dll</code> extension; Windows
            appends it, the string saves four bytes. Loading the DLL is what registers the
            <code>RICHEDIT50W</code> window class so <code>WM_CREATE</code> can instantiate it.</li>
        <li><strong><code>ParseStartupFile</code></strong> hand-parses <code>GetCommandLineA</code>: skip the
            (possibly quoted) exe path, skip whitespace, copy the first argument into
            <code>CmdFile</code>, stripping quotes. This is the entire drag-a-file-onto-the-exe feature —
            Explorer passes the dropped path as <code>argv[1]</code>.</li>
        <li><strong><code>WNDCLASS</code> is zeroed with <code>rep stosd</code></strong> (10 dwords), then only
            3 fields are set: <code>lpfnWndProc</code>, <code>hInstance</code>, <code>lpszClassName</code>. No icon,
            no cursor, no background brush — defaults are free.</li>
        <li><strong><code>BuildTitle</code></strong> scans <code>CmdFile</code> for the last <code>'\'</code> to isolate
            the filename, copies it into <code>TitleBuf</code>, appends <code>" - TinyRetroPad"</code>.
            (Checks for <code>'/'</code> and <code>':'</code> were commented out — "surprised me disabling this
            works" — because Explorer always hands over backslash paths.)</li>
      </ul>
    </div>
  </section>
  <!-- ============ 5 MESSAGE LOOP ============ -->
  <section class="window" id="loop">
    <div class="titlebar"><span class="ticon"></span><span class="tt">5 — The message loop and hand-rolled accelerators</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p>A normal Windows app uses an accelerator table resource and
         <code>TranslateAccelerator</code>. Resources cost bytes, so TinyRetroPad pattern-matches
         keystrokes <em>inside the message loop itself</em>:</p>
      <div class="sunken diagram">
<pre class="mermaid">
flowchart TD
    GM["GetMessageA"] --&gt;|returns 0 on WM_QUIT| XQ["ExitProcess"]
    GM --&gt; FD{"find/replace dialog open?"}
    FD --&gt;|"yes: IsDialogMessageA handled it"| GM
    FD --&gt;|no| KD{"WM_KEYDOWN?"}
    KD --&gt;|no| TD2["TranslateMessage&lt;br/&gt;DispatchMessage to WndProc"]
    TD2 --&gt; GM
    KD --&gt;|yes| FK{"F3 or F5?"}
    FK --&gt;|F3| AC["map to IDM command id"]
    FK --&gt;|F5| AC
    FK --&gt;|no| CTL{"Ctrl held?&lt;br/&gt;GetKeyState VK_CONTROL"}
    CTL --&gt;|no| TD2
    CTL --&gt;|"yes: N O S P F H G"| AC
    AC --&gt; SM["SendMessage WM_COMMAND to hMain&lt;br/&gt;Ctrl+Shift+S becomes Save As"]
    SM --&gt; GM
</pre>
      </div>
      <span class="caption">FIG 4 · EVERY KEYSTROKE PASSES THROUGH HERE</span>
      <ul>
        <li><strong>F3</strong> → Find Next, <strong>F5</strong> → Time/Date (exactly like classic Notepad).</li>
        <li><strong>Ctrl+N/O/S/P/F/H/G</strong> → New, Open, Save, Print, Find, Replace, Go To.
            <strong>Ctrl+Shift+S</strong> is detected with a second <code>GetKeyState(VK_SHIFT)</code> and
            upgraded to Save As.</li>
        <li>Each hit is converted to the <em>same</em> <code>IDM_…</code> command ID the menus use and
            re-sent as <code>WM_COMMAND</code> — so accelerators add zero new handler code, only the
            mapping table above.</li>
        <li>Ctrl+C/X/V/Z/A are <em>not</em> here: the Rich Edit control implements those natively.
            Only the chords the control can't know about are handled.</li>
        <li><code>IsDialogMessageA(hFindDlg, …)</code> runs first when a modeless Find/Replace dialog is
            open, so Tab and Enter work inside it — the documented requirement for modeless
            common dialogs.</li>
      </ul>
    </div>
  </section>
  <!-- ============ 6 WNDPROC ============ -->
  <section class="window" id="wndproc">
    <div class="titlebar"><span class="ticon"></span><span class="tt">6 — WndProc: one big cmp/je ladder</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p><code>WndProc</code> (line 1985, ~700 lines) is the whole personality of the app. There is no
         message-cracker macro, no jump table — just sequential <code>cmp</code>/<code>je</code> checks, because
         short conditional branches are 2 bytes each and compress superbly:</p>
      <div class="sunken diagram">
<pre class="mermaid">
flowchart TD
    M["message arrives at WndProc"] --&gt; C1{"WM_CREATE?"}
    C1 --&gt;|yes| H1["build RICHEDIT50W, menus,&lt;br/&gt;system-menu Save, status bar"]
    C1 --&gt;|no| C2{"uFindMsg?&lt;br/&gt;(registered FINDMSGSTRING)"}
    C2 --&gt;|yes| H2["OnFindReplaceMsg&lt;br/&gt;find / replace one / replace all"]
    C2 --&gt;|no| C3{"WM_SYSCOMMAND&lt;br/&gt;IDM_SAVE?"}
    C3 --&gt;|yes| H3["SaveFile"]
    C3 --&gt;|no| C4{"WM_COMMAND?"}
    C4 --&gt;|"EN_CHANGE notify"| H4["set fDirty, retitle with *"]
    C4 --&gt;|"menu id"| H5["flat cmp/je table:&lt;br/&gt;CmdFileNew ... CmdHelpView"]
    C4 --&gt;|no| C5{"WM_NOTIFY?"}
    C5 --&gt;|EN_SELCHANGE| H6["UpdateStatus - Ln, Col"]
    C5 --&gt;|"EN_MSGFILTER + WM_RBUTTONUP"| H7["ShowContextMenu"]
    C5 --&gt;|no| C6{"WM_SIZE?"}
    C6 --&gt;|yes| H8["place status bar at bottom,&lt;br/&gt;size edit to remaining client area"]
    C6 --&gt;|no| C7{"WM_DESTROY?"}
    C7 --&gt;|yes| H9["PostQuitMessage 0"]
    C7 --&gt;|no| H10["DefWindowProcA"]
</pre>
      </div>
      <span class="caption">FIG 5 · THE DISPATCH LADDER, TOP TO BOTTOM</span>
      <h3>WM_CREATE — the app assembles itself</h3>
      <p>When the frame window is born, the handler creates the Rich Edit child at size 0×0
         (a deliberate cheat — <code>WM_SIZE</code> arrives immediately after and fixes it), sets an
         event mask so the parent receives <code>EN_CHANGE</code> / <code>EN_SELCHANGE</code> / mouse
         notifications, raises the edit limit to ~2GB with <code>EM_EXLIMITTEXT</code>, appends a
         <strong>Save</strong> item to the <em>system menu</em> (the icon menu — that's why it arrives later
         as <code>WM_SYSCOMMAND</code>, not <code>WM_COMMAND</code>), builds the menu bar, and creates the
         status bar as a humble <code>STATIC</code> control with a sunken edge.</p>
      <h3>Menus from two 4-line helpers</h3>
      <p><code>CreateNotepadMenus</code> builds File/Edit/Format/View/Help with
         <code>CreatePopupMenu</code> + two wrappers: <code>AppendEnabled(menu, id, text)</code> and
         <code>AppendDisabled(menu, text)</code> — and the trick that <code>AppendDisabled(menu, NULL)</code>
         emits a <em>separator</em>, so no third helper is needed. The right-click context menu
         (<code>ShowContextMenu</code>, triggered by <code>EN_MSGFILTER</code> reporting
         <code>WM_RBUTTONUP</code>) reuses the same IDs, so it costs almost nothing.</p>
      <h3>WM_SIZE — layout in 15 instructions</h3>
      <p>Width and height are unpacked from <code>lParam</code>; if the status bar is visible its 20px
         are subtracted and it's parked at the bottom with <code>SetWindowPos</code>; the edit control
         gets the rest. That's the entire layout engine.</p>
    </div>
  </section>
  <!-- ============ 7 FEATURES ============ -->
  <section class="window" id="features">
    <div class="titlebar"><span class="ticon"></span><span class="tt">7 — Feature tour: how each menu item really works</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <h3>Edit menu: mostly one SendMessage each</h3>
      <table>
        <tr><th>Command</th><th>Implementation — complete</th></tr>
        <tr><td>Undo</td><td><code>SendMessage(hEdit, WM_UNDO)</code></td></tr>
        <tr><td>Cut / Copy / Paste / Delete</td><td><code>WM_CUT</code> / <code>WM_COPY</code> / <code>WM_PASTE</code> / <code>WM_CLEAR</code></td></tr>
        <tr><td>Select All</td><td><code>EM_SETSEL(0, −1)</code></td></tr>
        <tr><td>Time/Date</td><td><code>GetLocalTime</code> → <code>GetDateFormatA</code> + <code>GetTimeFormatA</code> → three <code>EM_REPLACESEL</code> (date, space, time)</td></tr>
        <tr><td>Word Wrap</td><td><code>EM_SETTARGETDEVICE</code> with line width 0 (wrap to window) or 0xFFFFFFFF (never wrap)</td></tr>
        <tr><td>Font</td><td><code>ChooseFontW</code> dialog → translate <code>LOGFONT</code> to <code>CHARFORMATW</code> → <code>EM_SETCHARFORMAT</code>. Point size ×2 = twips ÷10. <em>This is also how Courier is set at startup, which is why gdi32 has no font code in the binary.</em></td></tr>
      </table>
      <h3>File I/O: raw Win32, one shared path buffer</h3>
      <p><code>LoadStartupFile</code> and <code>SaveFile</code> are the only places bytes touch disk:</p>
<pre class="code"><span class="c">; load:  CreateFileA(CmdFile, GENERIC_READ, OPEN_EXISTING)</span>
<span class="c">;        GetFileSize -&gt; GlobalAlloc(size+1) -&gt; ReadFile</span>
<span class="c">;        buf[bytesRead] = 0 -&gt; SetWindowTextA(hEdit, buf)</span>
<span class="c">;        EM_SETCHARFORMAT(Courier) -&gt; GlobalFree -&gt; CloseHandle</span>
&nbsp;
<span class="c">; save:  WM_GETTEXTLENGTH -&gt; GlobalAlloc -&gt; WM_GETTEXT</span>
<span class="c">;        CreateFileA(CmdFile, GENERIC_WRITE, CREATE_ALWAYS)</span>
<span class="c">;        WriteFile -&gt; CloseHandle -&gt; fDirty=0 -&gt; ApplyTitle</span></pre>
      <p>Open and Save As are just <code>GetOpenFileNameA</code> / <code>GetSaveFileNameA</code> writing the
         chosen path into the same <code>CmdFile</code> buffer the command line used — then the existing
         load/save routines run unchanged. <strong>Open is literally a replay of app startup.</strong></p>
      <h3>The "Save changes?" guard</h3>
      <p>New, Open and Exit all call <code>MaybeSaveChanges</code> first. It returns 1 (proceed) or 0
         (user cancelled — abort the command):</p>
      <div class="sunken diagram">
<pre class="mermaid">
flowchart TD
    S["MaybeSaveChanges&lt;br/&gt;(runs before New / Open / Exit)"] --&gt; D1{"fDirty set?"}
    D1 --&gt;|no| OK["return 1 - continue"]
    D1 --&gt;|yes| MB["MessageBox Save changes?&lt;br/&gt;Yes / No / Cancel"]
    MB --&gt;|Cancel| NO["return 0 - abort command"]
    MB --&gt;|No| OK
    MB --&gt;|Yes| D2{"CmdFile has a path?"}
    D2 --&gt;|yes| SV["SaveFile"]
    D2 --&gt;|no| PK["PickSaveFile dialog"]
    PK --&gt;|user cancels| NO
    PK --&gt;|path chosen| SV
    SV --&gt; OK
</pre>
      </div>
      <span class="caption">FIG 6 · THE DIRTY-BUFFER DECISION TREE</span>
      <div class="dialog">
        <div class="titlebar"><span class="tt">TinyRetroPad</span><span class="tbtns"><span class="tbtn">×</span></span></div>
        <div class="body"><div class="q">?</div><p style="margin:4px 0 0">Save changes?</p></div>
        <div class="btnrow"><button class="btn95">Yes</button><button class="btn95">No</button><button class="btn95">Cancel</button></div>
      </div>
      <h3>Find / Replace: modeless dialogs and a registered message</h3>
      <p>The common Find and Replace dialogs are <em>modeless</em> — they don't block. They talk back
         to the app through a message whose number is allocated at runtime by
         <code>RegisterWindowMessageA("commdlg_FindReplace")</code>:</p>
      <div class="sunken diagram">
<pre class="mermaid">
sequenceDiagram
    participant U as User
    participant L as Message loop
    participant W as WndProc
    participant D as Find/Replace dialog (comdlg32)
    participant E as RICHEDIT50W
    U-&gt;&gt;W: Edit - Find (or Ctrl+F)
    W-&gt;&gt;W: InitFR fills FINDREPLACEA struct
    W-&gt;&gt;D: FindTextA(fr) - modeless, returns hFindDlg
    U-&gt;&gt;D: types text, clicks Find Next
    D-&gt;&gt;W: posts registered FINDMSGSTRING message
    W-&gt;&gt;W: OnFindReplaceMsg reads fr.Flags
    W-&gt;&gt;E: EM_FINDTEXTEXA from end of selection
    E--&gt;&gt;W: match position or -1
    W-&gt;&gt;E: EM_EXSETSEL + EM_SCROLLCARET
    Note over L,D: every loop pass calls IsDialogMessageA(hFindDlg) so the dialog gets Tab/Enter keys
</pre>
      </div>
      <span class="caption">FIG 7 · FIND, THE MODELESS WAY</span>
      <p><code>OnFindReplaceMsg</code> reads <code>fr.Flags</code>: <code>FR_DIALOGTERM</code> clears
         <code>hFindDlg</code>; <code>FR_REPLACEALL</code> moves the caret to 0 and loops
         find-next/<code>EM_REPLACESEL</code> until no match; <code>FR_REPLACE</code> replaces the selection
         then finds the next; otherwise plain find-next. The searching itself is one Rich Edit
         message, <code>EM_FINDTEXTEXA</code>, searching from the end of the current selection to the
         end of the document.</p>
      <h3>Print: the control prints itself</h3>
      <p><code>PrintDoc</code> shows <code>PrintDlgA</code> with <code>PD_RETURNDC</code> to get a printer device
         context, computes the page rectangle in twips
         (<code>HORZRES × 1440 ÷ LOGPIXELSX</code>), and then just loops:</p>
<pre class="code">PrintPage:
    <span class="k">call</span> StartPage
    <span class="c">; EM_FORMATRANGE: "Rich Edit, render yourself onto this DC,</span>
    <span class="c">;  starting at char cpMin; tell me where you stopped"</span>
    <span class="k">send</span> EM_FORMATRANGE      <span class="c">; eax = first char of NEXT page</span>
    <span class="k">mov</span>  fmt.chrg.cpMin, <span class="n">eax</span>
    <span class="k">call</span> EndPage
    <span class="k">cmp</span>  <span class="n">eax</span>, txtLen
    <span class="k">jl</span>   PrintPage           <span class="c">; until the whole doc is emitted</span></pre>
      <p>Pagination, fonts, margins — all done by the control. The app draws nothing.</p>
      <h3>Status bar: a STATIC control and four messages</h3>
      <p><code>UpdateStatus</code> runs on every <code>EN_SELCHANGE</code>:
         <code>EM_EXGETSEL</code> (caret position) → <code>EM_EXLINEFROMCHAR</code> (line) →
         <code>EM_LINEINDEX</code> (line start, so column = caret − start + 1) →
         <code>wsprintfA("  Ln %d, Col %d")</code> → <code>SetWindowTextA(hStatus)</code>.
         Toggling it shows/hides the window and replays <code>WM_SIZE</code> via
         <code>RelayoutClient</code> to reclaim the 20 pixels.</p>
      <h3>Help</h3>
      <p>About is one <code>MessageBoxA</code>. View Help is <code>ShellExecuteA("open", url)</code> —
         the browser is the help system.</p>
      <h3>Optional features: pay only if you assemble them</h3>
      <p>Two features are wrapped in assembly-time <code>IF</code> blocks, so the shipping binary
         contains zero bytes of them:</p>
      <ul>
        <li><strong><code>FEAT_LINENUMBERS</code></strong> — a 44px gutter painted in a <code>WM_PAINT</code>
            handler: fill the strip, then for each visible line <code>EM_LINEINDEX</code> →
            <code>EM_POSFROMCHAR</code> gives its y-pixel and <code>TextOutA</code> draws the number.
            <code>WM_SIZE</code> shifts the edit control right by the gutter width.</li>
        <li><strong><code>FEAT_DARKMODE</code></strong> — <code>EM_SETBKGNDCOLOR</code> for the background plus an
            <code>EM_SETCHARFORMAT</code> with <code>CFM_COLOR</code> for the text, and a
            <code>CheckMenuItem</code> tick in the View menu.</li>
      </ul>
    </div>
  </section>
  <!-- ============ 8 SIZE TRICKS ============ -->
  <section class="window" id="tricks">
    <div class="titlebar"><span class="ticon"></span><span class="tt">8 — The byte-shaving playbook</span>
      <span class="tbtns"><span class="tbtn">_</span><span class="tbtn">□</span><span class="tbtn">×</span></span></div>
    <div class="pane">
      <p>Everything above is shaped by one constraint: every byte counts <em>twice</em> — once raw,
         once through Crinkler's compressor. The recurring tricks:</p>
      <table>
        <tr><th>Trick</th><th>Why it's smaller</th></tr>
        <tr><td><code>push 1</code> / <code>pop eax</code> instead of <code>mov eax, 1</code></td>
            <td>3 bytes instead of 5. Used everywhere a small constant lands in a register.</td></tr>
        <tr><td><code>xor eax, eax</code> for zero</td>
            <td>2 bytes; also the standard "return 0 from WndProc".</td></tr>
        <tr><td><code>rep stosd</code> / <code>rep stosb</code> to zero structs</td>
            <td>Win32 structs (<code>OPENFILENAME</code>, <code>WNDCLASS</code>, <code>PRINTDLG</code>…) must be zeroed; a 4-byte string-store loop beats field-by-field writes, and the identical idiom repeated 8 times compresses to almost nothing.</td></tr>
        <tr><td>Window class named <code>"."</code></td>
            <td>2 bytes of string, reused as the throwaway initial window title.</td></tr>
        <tr><td><code>"Msftedit"</code> without <code>.dll</code></td>
            <td>LoadLibrary appends the extension for free.</td></tr>
        <tr><td>Save lives on the <em>system</em> menu too</td>
            <td>The original sub-1KB editor's only menu was one <code>AppendMenuA</code> onto <code>GetSystemMenu</code> — kept for compatibility and because it's nearly free.</td></tr>
        <tr><td>One <code>CmdFile</code> buffer for everything</td>
            <td>Command line, Open dialog, Save dialog, load, save — five features, one 128-byte buffer, no path-copying code.</td></tr>
        <tr><td>Accelerators re-send menu IDs</td>
            <td>No second code path: Ctrl+O <em>is</em> File→Open.</td></tr>
        <tr><td>Separator = disabled item with NULL text</td>
            <td>One helper proc fewer.</td></tr>
        <tr><td>In-memory <code>DLGTEMPLATE</code>, no <code>.rc</code></td>
            <td>Avoids a PE resource section (hundreds of bytes of overhead).</td></tr>
        <tr><td>Edit control created at 0×0</td>
            <td>The imminent <code>WM_SIZE</code> sizes it anyway; four <code>push 0</code> are 1 byte each.</td></tr>
        <tr><td>No GDI font code</td>
            <td>Courier arrives via <code>EM_SETCHARFORMAT</code> with a prebuilt <code>CHARFORMATW</code> in <code>.DATA</code>; <code>CreateFont</code> and friends never get imported.</td></tr>
        <tr><td>Repetition is free</td>
            <td>Dozens of near-identical <code>push/push/push/call SendMessage</code> sequences look wasteful in source, but Crinkler's context modeling compresses repeated patterns brutally well — uniformity beats cleverness.</td></tr>
      </table>
      <p>
        The result: a complete, recognizable Notepad — File, Edit, Format, View, Help, printing,
        find &amp; replace, a status bar, drag-and-drop — in fewer bytes than a 50×50 favicon.
      </p>
      <p class="small">
        Source: <a href="https://github.com/PlummersSoftwareLLC/TinyRetroPad">PlummersSoftwareLLC/TinyRetroPad</a>
        · trpad.asm (2,687 lines) · build: MASM 14 + Crinkler · License: Apache 2.0 ·
        Lineage: tiny.asm (HelloAssembly, Dave Plummer) → Dave's Tiny Editor (Matt Power) → TinyRetroPad.
      </p>
    </div>
    <div class="statusrow"><span class="cell grow">2,794 bytes — smaller than this page's CSS</span><span class="cell">Ln 2687, Col 1</span></div>
  </section>
</div>
<!-- taskbar -->
<div class="taskbar">
  <span class="start"><span class="flag">⊞</span> Start</span>
  <span class="task">📝 trpad.asm — explained</span>
  <span class="tray" id="clock">--:--</span>
</div>

<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
  mermaid.initialize({
    startOnLoad: true,
    theme: "neutral",
    themeVariables: {
      fontFamily: '"IBM Plex Mono", monospace',
      fontSize: "13px",
      primaryColor: "#c0c0c0",
      primaryBorderColor: "#404040",
      primaryTextColor: "#111111",
      lineColor: "#000080",
      clusterBkg: "#fffef7",
      clusterBorder: "#808080",
      actorBkg: "#c0c0c0",
      actorBorder: "#404040",
      noteBkgColor: "#ffffcc",
      noteBorderColor: "#808080"
    },
    flowchart: { curve: "linear", htmlLabels: true }
  });
  // taskbar clock
  const clock = document.getElementById("clock");
  const tick = () => {
    const d = new Date();
    clock.textContent = d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  };
  tick(); setInterval(tick, 30000);
</script>
</body>
</html>
