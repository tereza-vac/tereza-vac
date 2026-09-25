<div align="center">

<p>
<em>
Clouds are not spheres, mountains are not cones,<br>
coastlines are not circles, and bark is not smooth,<br>
nor does lightning travel in a straight line.
</em>
</p>
<p><sub>&mdash; Benoit B. Mandelbrot, <i>The Fractal Geometry of Nature</i></sub></p>

<h3>◈</h3>

<img src="assets/mandelbrot.png" width="720" alt="The Mandelbrot set rendered by a recursive SQL query">

<p><sub>The Mandelbrot set, computed by a single recursive SQL query &mdash; every pixel and every iteration is a row.</sub></p>

<details>
<summary><b>The math</b></summary>
<br>

For every point $c$ of the complex plane, iterate

$$z_{n+1} = z_n^{2} + c \qquad z_0 = 0$$

The Mandelbrot set is the set of all $c$ for which the orbit stays bounded:

$$\mathcal{M} = \lbrace c \in \mathbb{C} \mid \sup_{n \ge 0} \lvert z_n \rvert < \infty \rbrace$$

Once $\lvert z_n \rvert > 2$ the orbit escapes to infinity, so $c \notin \mathcal{M}$. The colour of each outside point comes from the smooth escape time

$$\nu = n + 1 - \log_2 \log \lvert z_n \rvert$$

which removes the visible bands of a plain iteration count. The boundary of $\mathcal{M}$ is so wrinkled that its Hausdorff dimension is exactly $2$ (Shishikura, 1998).

</details>

<details>
<summary><b>How it's rendered</b></summary>
<br>

<p>
<a href="mandelbrot/mandelbrot.sql"><code>mandelbrot.sql</code></a> is one <code>WITH RECURSIVE</code> query in plain SQLite.<br>
It builds the pixel grid, then keeps squaring every <code>z</code> in lock-step until it escapes or hits the iteration limit.<br>
<a href="mandelbrot/render.py"><code>render.py</code></a> only maps the returned escape times to colours.
</p>
<p>
1920 × 1080 points, 200 iterations, 2×2 supersampling &mdash; about three minutes on a laptop.
</p>

</details>

<h3>◈</h3>

<details>
<summary><b>Selected Work</b></summary>
<br>
<table border="0" width="90%" align="center">
<tr>
<td width="30%" align="right" valign="top">
<b>AI & Agents</b>
</td>
<td width="70%" align="left" valign="top">
<a href="https://github.com/tereza-vac/AgentVault"><b>AgentVault</b></a><br>
Local-first Markdown knowledge base with semantic search. Notes stay plain files; PostgreSQL + pgvector is a rebuildable index exposed to agents over MCP, a CLI and a web UI.<br><br>
<a href="https://github.com/tereza-vac/AgentMaison"><b>AgentMaison</b></a><br>
Self-hosted multi-agent console: Markdown personas behind an OpenAI-compatible API, each chat turn running one pass of a pluggable CLI agent.<br><br>
<a href="https://github.com/tereza-vac/AgentBridge"><b>AgentBridge</b></a><br>
Telegram bridge for CLI coding agents running on a laptop or VPS, with live tmux sessions, voice and file handling. Builds on <a href="https://github.com/petrludwig-collab/Agent2Telegram">Agent2Telegram</a> by Petr Ludwig.<br><br>
<a href="https://github.com/tereza-vac/TestLab"><b>TestLab</b></a><br>
Test-item authoring with KaTeX/MathLive math editing and RAG validation of each item against source documents (Supabase, pgvector).<br><br>
<a href="https://github.com/tereza-vac/fact-checker"><b>Fact Checker</b></a><br>
Streamlit lab comparing classic retrieval, embeddings, plain LLMs and web RAG for claim verification.
</td>
</tr>
<tr><td colspan="2"><br></td></tr>
<tr>
<td width="30%" align="right" valign="top">
<b>Apps & Tools</b>
</td>
<td width="70%" align="left" valign="top">
<a href="https://github.com/tereza-vac/letterflow"><b>letterflow</b></a><br>
Local-first desktop app (Tauri, React) that turns messy contact files and a rough brief into validated, personalized email drafts, with a safety score and guarded sending.<br><br>
<a href="https://github.com/tereza-vac/in_side_app_demo"><b>Inside</b></a><br>
Mood journal with trend analysis and a pluggable LLM reflection assistant. Expo / React Native and FastAPI from one codebase.<br><br>
<a href="https://github.com/tereza-vac/deskphoto"><b>deskphoto</b></a><br>
CLI that turns a phone photo of a paper document into a flat, clean PDF: contour detection, perspective warp and an optional OCR layer.<br><br>
<a href="https://github.com/tereza-vac/scio_realtime_progress"><b>Realtime Progress</b></a><br>
Classroom tracker with an AI tutor and a live teacher dashboard. Blazor Server, SignalR, SQL Server.
</td>
</tr>
<tr><td colspan="2"><br></td></tr>
<tr>
<td width="30%" align="right" valign="top">
<b>Data</b>
</td>
<td width="70%" align="left" valign="top">
<a href="https://github.com/tereza-vac/StreamWise_Analytics"><b>StreamWise Analytics</b></a><br>
End-to-end pipeline for a fictional streaming platform: synthetic data, star schema in SQL Server, analytical views and a Power BI report.
</td>
</tr>
<tr><td colspan="2"><br></td></tr>
<tr>
<td width="30%" align="right" valign="top">
<b>Web</b>
</td>
<td width="70%" align="left" valign="top">
<a href="https://hafiada.cz"><b>hafiada.cz</b></a><br>
Website for a Czech community dog event. React, Vite, TypeScript.<br><br>
<a href="https://pmu-trinec.cz"><b>pmu-trinec.cz</b></a><br>
Static site for a cosmetics studio, built for speed and accessibility.
</td>
</tr>
</table>
</details>

<h3>◈</h3>

<p><sub>Python · TypeScript · React / React Native · FastAPI · PostgreSQL + pgvector · .NET &nbsp;·&nbsp; <a href="https://terezavac.cz">terezavac.cz</a></sub></p>

</div>
