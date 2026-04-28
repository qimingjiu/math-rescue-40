# -*- coding: utf-8 -*-
import re

with open('templates.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 数列
old1 = '''  <!-- ============ 2. 数列 ============ -->
  <div class="topic-header" id="sequence">
    <h2>② 数列</h2>
    <div class="topic-meta">第 17/18 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>设首项与公差/比 → 列方程组 → 求通项 → 求和（看类型选公式）。
  </div>

  <div class="placeholder">
    <div class="placeholder-stamp">UNDER CONSTRUCTION</div>
    <div class="placeholder-title">数列大题模板 · 内容补充中</div>
    <p style="font-size:0.85rem; margin-top:8px;">
      将包含：<br>
      · 等差/等比通项与求和模板<br>
      · 错位相减、裂项相消<br>
      · 已知 $S_n$ 求 $a_n$ 的标准解法<br>
      · 真题示范
    </p>
  </div>'''

new1 = '''  <!-- ============ 2. 数列 ============ -->
  <div class="topic-header" id="sequence">
    <h2>② 数列</h2>
    <div class="topic-meta">第 17/18 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>判断类型 → 写通项 → 选对求和方法 → 规范作答。第一问求通项是送分，第二问求和是分水岭。
  </div>

  <section class="card">
    <h3 class="card-title">套路总纲</h3>
    <ol class="steps">
      <li>
        <strong>判断数列类型</strong>
        <span class="step-note">题目出现"等差""等比"直接套公式；出现 $S_n$ 考虑 $a_n=S_n-S_{n-1}$；出现递推考虑构造法</span>
      </li>
      <li>
        <strong>求通项 $a_n$</strong><br>
        等差：$a_n=a_1+(n-1)d$　等比：$a_n=a_1q^{n-1}$<br>
        已知 $S_n$：$a_n=\\begin{cases}S_1 & n=1\\\\ S_n-S_{n-1} & n\\ge 2\\end{cases}$ <strong>（必须分类）</strong>
        <span class="step-note">写完通项后，一定要验 $n=1$ 是否满足 $n\\ge 2$ 的式子</span>
      </li>
      <li>
        <strong>求和——看类型选方法</strong><br>
        等差/等比：直接用公式<br>
        等差×等比：错位相减法<br>
        分式型：裂项相消法<br>
        分组型：拆开分别求和
        <span class="step-note">错位相减最容易算错，建议写完后再代 $n=1,2$ 验算</span>
      </li>
      <li>
        <strong>证明/不等式（第二问）</strong><br>
        放缩法、构造函数法、数学归纳法——<span class="mark">不会做先写"由（1）知 $a_n=\\dots$"，把通项摆出来就有 1 分</span>
      </li>
    </ol>
  </section>

  <section class="card">
    <h3 class="card-title">三类高频求和模型</h3>

    <div class="formula-block">
      <div class="formula-name">模型 A · 错位相减（等差×等比）<span class="formula-tag">必会</span></div>
      若 $c_n=(an+b)\\cdot q^n$，求 $T_n=\\sum c_n$。<br>
      <strong>套路：</strong>写出 $T_n$ → 乘 $q$ 得 $qT_n$ → 两式相减 → 整理成等比求和 → 解出 $T_n$。
    </div>

    <div class="formula-block">
      <div class="formula-name">模型 B · 裂项相消（分式型）<span class="formula-tag">高频</span></div>
      $$\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1},\\quad \\dfrac{1}{n(n+2)}=\\dfrac{1}{2}\\!\\left(\\dfrac{1}{n}-\\dfrac{1}{n+2}\\right)$$
      <strong>套路：</strong>拆开 → 前后项相消 → 只剩首末两项 → 代入求值。
    </div>

    <div class="formula-block">
      <div class="formula-name">模型 C · 已知 $S_n$ 求 $a_n$<span class="formula-tag">送分</span></div>
      <strong>标准三步：</strong>① $n=1$ 时 $a_1=S_1$；② $n\\ge 2$ 时 $a_n=S_n-S_{n-1}$；③ 验 $a_1$ 是否满足通式。
    </div>
  </section>

  <section class="card">
    <h3 class="card-title">真题示范 · 2023 新高考 I 卷 18 题</h3>

    <div class="example">
      <span class="example-tag">2023 · 新高考I卷</span>
      <div class="example-q">
        记 $S_n$ 为数列 $\\{a_n\\}$ 的前 $n$ 项和，已知 $a_2=1$，$2S_n=na_n$。<br>
        (1) 求 $\\{a_n\\}$ 的通项公式；<br>
        (2) 求数列 $\\left\\{\\dfrac{a_{n+1}}{2^n}\\right\\}$ 的前 $n$ 项和 $T_n$。
      </div>
      <div class="example-a">
        <strong class="note-red">第（1）问 · 套路：已知 $S_n$ 求 $a_n$</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>$n=1$ 时，$2S_1=a_1$，即 $2a_1=a_1$，所以 $a_1=0$</li>
          <li>$n\\ge 2$ 时，$2S_n=na_n$，$2S_{n-1}=(n-1)a_{n-1}$，两式相减得 $2a_n=na_n-(n-1)a_{n-1}$</li>
          <li>整理得 $(n-2)a_n=(n-1)a_{n-1}$，递推得 $\\dfrac{a_n}{a_{n-1}}=\\dfrac{n-1}{n-2}$，累乘得 $a_n=n-1$</li>
          <li>验 $n=1$：$a_1=0$ 符合 $a_n=n-1$。所以 $a_n=n-1$。</li>
        </ol>

        <strong class="note-red" style="display:block; margin-top:14px;">第（2）问 · 套路：错位相减</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>由（1）知 $\\dfrac{a_{n+1}}{2^n}=\\dfrac{n}{2^n}$，设 $T_n=\\sum_{k=1}^{n}\\dfrac{k}{2^k}$</li>
          <li>$T_n=\\dfrac{1}{2}+\\dfrac{2}{2^2}+\\dfrac{3}{2^3}+\\cdots+\\dfrac{n}{2^n}$</li>
          <li>$\\dfrac{1}{2}T_n=\\dfrac{1}{2^2}+\\dfrac{2}{2^3}+\\cdots+\\dfrac{n-1}{2^n}+\\dfrac{n}{2^{n+1}}$</li>
          <li>相减得 $\\dfrac{1}{2}T_n=\\dfrac{1}{2}+\\dfrac{1}{2^2}+\\cdots+\\dfrac{1}{2^n}-\\dfrac{n}{2^{n+1}}=1-\\dfrac{1}{2^n}-\\dfrac{n}{2^{n+1}}$</li>
          <li>所以 $T_n=2-\\dfrac{n+2}{2^n}$</li>
        </ol>
      </div>
    </div>

    <p class="note-red" style="font-size:0.88rem; margin-top:14px;">
      ※ 第（1）问写出 $S_n-S_{n-1}$ 这一步就有 3 分；第（2）问只要写出错位相减的"两式相减"动作，即使后面算错也有 3 分。<span class="mark">步骤在，分就在。</span>
    </p>
  </section>'''

# 2. 立体几何
old2 = '''  <!-- ============ 3. 立体几何 ============ -->
  <div class="topic-header" id="solid">
    <h2>③ 立体几何</h2>
    <div class="topic-meta">第 19 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>第一问几何法证平行/垂直，第二问<span class="mark">建系用向量</span>算二面角。
  </div>

  <div class="placeholder">
    <div class="placeholder-stamp">UNDER CONSTRUCTION</div>
    <div class="placeholder-title">立体几何大题模板 · 内容补充中</div>
    <p style="font-size:0.85rem; margin-top:8px;">
      将包含：<br>
      · 证平行/垂直的判定定理速查<br>
      · 建系四步法（找原点 / 定轴 / 求点坐标 / 求向量）<br>
      · 法向量求二面角公式<br>
      · 真题示范
    </p>
  </div>'''

new2 = '''  <!-- ============ 3. 立体几何 ============ -->
  <div class="topic-header" id="solid">
    <h2>③ 立体几何</h2>
    <div class="topic-meta">第 19 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>第一问几何法证平行/垂直，第二问<span class="mark">建系用向量</span>算二面角。建系对了，这题就稳了。
  </div>

  <section class="card">
    <h3 class="card-title">套路总纲</h3>
    <ol class="steps">
      <li>
        <strong>第一问：证平行/垂直</strong><br>
        平行：线面平行 → 找线线平行（中位线、平行四边形）<br>
        垂直：线面垂直 → 找线线垂直（勾股定理逆定理、等腰三角形三线合一）
        <span class="step-note">写判定定理时，条件一个不能漏。比如线面平行要写明"$l\\not\\subset\\alpha$ 且 $l\\parallel m\\subset\\alpha$"</span>
      </li>
      <li>
        <strong>建系四步法（第二问核心）</strong><br>
        ① <strong>找原点</strong>：三条两两垂直的线的交点（没有就自己作垂线）<br>
        ② <strong>定轴</strong>：$x,y,z$ 轴标清楚，在图上用箭头标出来<br>
        ③ <strong>求点坐标</strong>：利用已知边长、角度，逐个写出关键点坐标<br>
        ④ <strong>求向量</strong>：方向向量 $\\vec{s}$、法向量 $\\vec{n}$
        <span class="step-note">建系前必须先证垂直关系，否则建系不成立！这是第一得分点。</span>
      </li>
      <li>
        <strong>求法向量</strong><br>
        设 $\\vec{n}=(x,y,z)$，由 $\\vec{n}\\cdot\\vec{a}=0$ 且 $\\vec{n}\\cdot\\vec{b}=0$ 列方程组，令一个变量为 1 解出另外两个。
        <span class="step-note">法向量不要求唯一，只要方向对就行。算错了可以用 $\\vec{n_1}\\cdot\\vec{n_2}$ 验算是否垂直于平面内两条线。</span>
      </li>
      <li>
        <strong>套公式求角</strong><br>
        二面角：$\\cos\\theta=\\dfrac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}$　线面角：$\\sin\\theta=\\dfrac{|\\vec{a}\\cdot\\vec{n}|}{|\\vec{a}||\\vec{n}|}$
        <span class="step-note">二面角是钝角还是锐角？<span class="mark">看图判断</span>，算出来是负的但图上是锐角，就取正的。</span>
      </li>
    </ol>
  </section>

  <section class="card">
    <h3 class="card-title">判定定理速查（第一问用）</h3>

    <div class="formula-block">
      <div class="formula-name">线面平行判定<span class="formula-tag">必写</span></div>
      平面外一条直线与此平面内的一条直线平行，则该直线与此平面平行。<br>
      <strong>关键词：</strong>$l\\not\\subset\\alpha$，$m\\subset\\alpha$，$l\\parallel m$ $\\Rightarrow$ $l\\parallel\\alpha$
    </div>

    <div class="formula-block">
      <div class="formula-name">线面垂直判定<span class="formula-tag">必写</span></div>
      一条直线与一个平面内的两条相交直线都垂直，则该直线与此平面垂直。<br>
      <strong>关键词：</strong>$l\\perp a$，$l\\perp b$，$a\\cap b=P$，$a,b\\subset\\alpha$ $\\Rightarrow$ $l\\perp\\alpha$
    </div>
  </section>

  <section class="card">
    <h3 class="card-title">真题示范 · 2022 新高考 I 卷 19 题（节选）</h3>

    <div class="example">
      <span class="example-tag">2022 · 新高考I卷</span>
      <div class="example-q">
        直三棱柱 $ABC-A_1B_1C_1$ 的体积为 4，$\\triangle A_1BC$ 的面积为 $2\\sqrt{2}$。<br>
        (1) 求点 $A$ 到平面 $A_1BC$ 的距离；<br>
        (2) 设 $D$ 为 $A_1C$ 的中点，$AA_1=AB$，平面 $A_1BC\\perp$ 平面 $ABB_1A_1$，求二面角 $A-BD-C$ 的正弦值。
      </div>
      <div class="example-a">
        <strong class="note-red">第（1）问 · 套路：等体积法</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>$V_{A-A_1BC}=V_{A_1-ABC}=\\dfrac{1}{3}S_{\\triangle ABC}\\cdot AA_1=\\dfrac{1}{3}\\times \\dfrac{1}{2}V_{柱}=\\dfrac{2}{3}$</li>
          <li>设点 $A$ 到平面 $A_1BC$ 的距离为 $h$，则 $V_{A-A_1BC}=\\dfrac{1}{3}S_{\\triangle A_1BC}\\cdot h=\\dfrac{1}{3}\\times 2\\sqrt{2}\\cdot h=\\dfrac{2}{3}$</li>
          <li>解得 $h=\\dfrac{\\sqrt{2}}{2}$</li>
        </ol>

        <strong class="note-red" style="display:block; margin-top:14px;">第（2）问 · 套路：建系 + 法向量</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>取 $A_1B$ 中点 $E$，由面 $A_1BC\\perp$ 面 $ABB_1A_1$ 得 $CE\\perp$ 面 $ABB_1A_1$</li>
          <li>以 $E$ 为原点，$EB$ 为 $x$ 轴，$EC$ 为 $y$ 轴，过 $E$ 作平行于 $AA_1$ 的线为 $z$ 轴建系</li>
          <li>设 $AA_1=AB=2$，求得各点坐标，写出 $\\vec{BA}$、$\\vec{BD}$、$\\vec{BC}$</li>
          <li>求平面 $ABD$ 的法向量 $\\vec{n_1}$ 和平面 $CBD$ 的法向量 $\\vec{n_2}$</li>
          <li>$\\cos\\theta=\\dfrac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}=\\dfrac{1}{\\sqrt{3}}$，所以 $\\sin\\theta=\\dfrac{\\sqrt{6}}{3}$</li>
        </ol>
      </div>
    </div>

    <p class="note-red" style="font-size:0.88rem; margin-top:14px;">
      ※ 第（2）问只要"建系 → 写坐标 → 求法向量"这三步写出来，即使最后 $\\sin\\theta$ 算错，也有 <span class="mark">6-8 分</span>。
    </p>
  </section>'''

# 3. 概率统计
old3 = '''  <!-- ============ 4. 概率统计 ============ -->
  <div class="topic-header" id="prob">
    <h2>④ 概率统计</h2>
    <div class="topic-meta">第 18/19 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>读题分类 → 列分布列 → 求期望/方差。<span class="mark">分布列写错就全错</span>。
  </div>

  <div class="placeholder">
    <div class="placeholder-stamp">UNDER CONSTRUCTION</div>
    <div class="placeholder-title">概率统计大题模板 · 内容补充中</div>
    <p style="font-size:0.85rem; margin-top:8px;">
      将包含：<br>
      · 古典概型 / 二项分布 / 超几何分布的区分<br>
      · 分布列三步标准写法<br>
      · 期望方差公式速查<br>
      · 线性回归套路（不强求记，但要知道代入步骤）<br>
      · 真题示范
    </p>
  </div>'''

new3 = '''  <!-- ============ 4. 概率统计 ============ -->
  <div class="topic-header" id="prob">
    <h2>④ 概率统计</h2>
    <div class="topic-meta">第 18/19 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>判断分布类型 → 列分布列 → 求期望/方差。<span class="mark">分布列写错就全错，写完必须验概率和为 1。</span>
  </div>

  <section class="card">
    <h3 class="card-title">套路总纲</h3>
    <ol class="steps">
      <li>
        <strong>判断分布类型</strong><br>
        放回抽样 / $n$ 次独立重复 → <span class="mark">二项分布</span> $B(n,p)$<br>
        不放回抽样 / 有限总体抽样本 → <span class="mark">超几何分布</span><br>
        等可能结果数 → <span class="mark">古典概型</span> $P(A)=\\dfrac{m}{n}$
        <span class="step-note">类型判断错了，后面全错。拿不准时把题设条件往这三个定义里套。</span>
      </li>
      <li>
        <strong>列分布列（标准三步）</strong><br>
        ① <strong>设</strong>：写出"设随机变量 $X$ 的所有可能取值为 $0,1,2,\\dots$"<br>
        ② <strong>算</strong>：逐个计算 $P(X=k)$，每一步写清楚组合数或概率公式<br>
        ③ <strong>列</strong>：画表格，$X$ 一行，$P$ 一行，最后加一行"合计=1"验算
        <span class="step-note">分布列表格是得分核心，<span class="mark">哪怕概率算错，表格格式正确也有 2 分</span>。</span>
      </li>
      <li>
        <strong>求期望与方差</strong><br>
        $E(X)=\\sum x_i p_i$（分布列上下相乘再相加）<br>
        $D(X)=\\sum (x_i-E(X))^2 p_i$ 或直接用公式 $D(X)=np(1-p)$（二项分布）
        <span class="step-note">期望和方差的公式写对了就有 1 分，代入数字对了再得 1-2 分。</span>
      </li>
      <li>
        <strong>线性回归（若考到）</strong><br>
        记住：代入公式求 $\\hat{b}$ 和 $\\hat{a}$，写出回归方程 $\\hat{y}=\\hat{b}x+\\hat{a}$。<br>
        <span class="mark">公式不需要背</span>，卷首会给参考公式，但要知道代哪个数。
        <span class="step-note">回归题近年常和实际情境结合（如销量、温度），读懂题比算对数更重要。</span>
      </li>
    </ol>
  </section>

  <section class="card">
    <h3 class="card-title">三种分布的区分表</h3>

    <table class="score-table">
      <thead>
        <tr><th>特征</th><th>古典概型</th><th>二项分布</th><th>超几何分布</th></tr>
      </thead>
      <tbody>
        <tr><td>核心条件</td><td>等可能</td><td>$n$ 次独立重复</td><td>不放回，有限总体</td></tr>
        <tr><td>公式记忆</td><td>$P=\\dfrac{m}{n}$</td><td>$P(X=k)=C_n^k p^k(1-p)^{n-k}$</td><td>$P(X=k)=\\dfrac{C_M^k C_{N-M}^{n-k}}{C_N^n}$</td></tr>
        <tr><td>期望</td><td>—</td><td>$E(X)=np$</td><td>$E(X)=n\\cdot\\dfrac{M}{N}$</td></tr>
        <tr><td>方差</td><td>—</td><td>$D(X)=np(1-p)$</td><td>—</td></tr>
      </tbody>
    </table>
  </section>

  <section class="card">
    <h3 class="card-title">真题示范 · 2023 新高考 I 卷 20 题（节选）</h3>

    <div class="example">
      <span class="example-tag">2023 · 新高考I卷</span>
      <div class="example-q">
        甲乙两人投篮，每次投篮由其中一人执行。甲每次命中概率 0.6，乙每次命中概率 0.8。第一次由甲投篮。<br>
        (1) 求第 2 次投篮的人是乙的概率；<br>
        (2) 设第 $i$ 次投篮的人是甲的概率为 $p_i$，求 $p_i$ 的通项公式。
      </div>
      <div class="example-a">
        <strong class="note-red">第（1）问 · 套路：分类讨论</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>第 2 次是乙 = 第 1 次甲没中（因为甲投完不中才轮到乙），概率 $1-0.6=0.4$</li>
        </ol>

        <strong class="note-red" style="display:block; margin-top:14px;">第（2）问 · 套路：递推 + 等比数列</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>第 $i+1$ 次是甲的情况：① 第 $i$ 次是甲且命中（概率 $p_i\\times 0.6$）；② 第 $i$ 次是乙且没命中（概率 $(1-p_i)\\times 0.2$）</li>
          <li>所以 $p_{i+1}=0.6p_i+0.2(1-p_i)=0.4p_i+0.2$</li>
          <li>构造等比：$p_{i+1}-\\dfrac{1}{3}=0.4\\left(p_i-\\dfrac{1}{3}\\right)$，所以 $\\left\\{p_i-\\dfrac{1}{3}\\right\\}$ 是等比数列</li>
          <li>$p_1=1$，所以 $p_i=\\dfrac{1}{3}+\\dfrac{2}{3}\\times 0.4^{i-1}$</li>
        </ol>
      </div>
    </div>

    <p class="note-red" style="font-size:0.88rem; margin-top:14px;">
      ※ 这道题容易栽在读题上——<span class="mark">概率题一定要把规则读三遍再动笔</span>。第（2）问写出递推关系就有 4 分，构造等比再有 3 分。
    </p>
  </section>'''

# 4. 圆锥曲线
old4 = '''  <!-- ============ 5. 圆锥曲线 ============ -->
  <div class="topic-header" id="conic">
    <h2>⑤ 圆锥曲线（解析几何）</h2>
    <div class="topic-meta">第 21 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>设直线 → 联立方程 → 韦达定理 → 代入条件。
    <span class="note-red">即使算不到底，前 4 步就有 6 分。</span>
  </div>

  <div class="placeholder">
    <div class="placeholder-stamp">UNDER CONSTRUCTION</div>
    <div class="placeholder-title">圆锥曲线大题模板 · 内容补充中</div>
    <p style="font-size:0.85rem; margin-top:8px;">
      将包含：<br>
      · 椭圆 / 抛物线标准方程速查<br>
      · 联立方程的"五步法"（设 → 立 → 判 → 韦达 → 代）<br>
      · 弦长公式、点到直线距离<br>
      · 何时设 $y=kx+b$、何时设 $x=my+t$<br>
      · 真题示范
    </p>
  </div>'''

new4 = '''  <!-- ============ 5. 圆锥曲线 ============ -->
  <div class="topic-header" id="conic">
    <h2>⑤ 圆锥曲线（解析几何）</h2>
    <div class="topic-meta">第 21 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>设直线 → 联立方程 → 韦达定理 → 代入条件。
    <span class="note-red">即使算不到底，前 4 步就有 6 分。</span>
  </div>

  <section class="card">
    <h3 class="card-title">套路总纲：联立五步法</h3>
    <ol class="steps">
      <li>
        <strong>设直线</strong><br>
        过定点在 $x$ 轴上 → 设 $x=my+t$（避免讨论斜率不存在）<br>
        其他情况 → 设 $y=kx+b$<br>
        <span class="mark">斜率不存在的情况单独写一行</span>，即使后面不用也要写，是踩分点。
        <span class="step-note">设直线这一步写对了就有 1 分。</span>
      </li>
      <li>
        <strong>联立方程</strong><br>
        把直线方程代入曲线方程（椭圆/抛物线），消元得到关于 $x$（或 $y$）的一元二次方程。
        <span class="step-note">写出"联立得"三个字，然后把方程展开整理出来，就有 1-2 分。</span>
      </li>
      <li>
        <strong>写判别式 $\\Delta>0$</strong><br>
        保证有两个交点，必须写 $\\Delta>0$。<br>
        <span class="mark">这一步经常忘，但它是得分点！</span>
        <span class="step-note">$\\Delta>0$ 写出来就有 1 分，后面解出参数范围再得 1-2 分。</span>
      </li>
      <li>
        <strong>韦达定理</strong><br>
        $x_1+x_2=-\\dfrac{b}{a}$，$x_1x_2=\\dfrac{c}{a}$（具体系数用联立后的方程系数）<br>
        <span class="mark">不需要解出 $x_1,x_2$！</span>韦达整体代入是圆锥曲线的灵魂。
        <span class="step-note">韦达定理写对了就有 2 分。后面所有计算都建立在这两个式子上。</span>
      </li>
      <li>
        <strong>代入条件求解</strong><br>
        题目给什么条件（弦长、斜率、向量、面积等），就化什么表达式，全部用 $x_1+x_2$ 和 $x_1x_2$ 表示。<br>
        <span class="mark">算到这一步，即使最后答案没出来，已经有 6-8 分了。</span>
      </li>
    </ol>
  </section>

  <section class="card">
    <h3 class="card-title">常用结论（写在草稿纸上备用）</h3>

    <div class="formula-block">
      <div class="formula-name">弦长公式<span class="formula-tag">必背</span></div>
      $$|AB|=\\sqrt{1+k^2}\\cdot|x_1-x_2|=\\sqrt{1+k^2}\\cdot\\sqrt{(x_1+x_2)^2-4x_1x_2}$$
    </div>

    <div class="formula-block">
      <div class="formula-name">中点弦（点差法）<span class="formula-tag">技巧</span></div>
      若 $M(x_0,y_0)$ 是弦 $AB$ 中点，则 $\\dfrac{x_0}{a^2}+\\dfrac{k y_0}{b^2}=0$（椭圆）。<br>
      <strong>适用：</strong>已知中点求斜率，或已知斜率求中点轨迹。
    </div>
  </section>

  <section class="card">
    <h3 class="card-title">真题示范 · 2023 新高考 I 卷 21 题（节选）</h3>

    <div class="example">
      <span class="example-tag">2023 · 新高考I卷</span>
      <div class="example-q">
        已知椭圆 $C:\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1(a>b>0)$ 的离心率为 $\\dfrac{\\sqrt{5}}{3}$，点 $A(-2,0)$ 在 $C$ 上。<br>
        (1) 求 $C$ 的方程；<br>
        (2) 过点 $(-2,3)$ 的直线交 $C$ 于 $P,Q$ 两点，直线 $AP,AQ$ 与 $y$ 轴交于 $M,N$ 两点，证明：线段 $MN$ 的中点为定点。
      </div>
      <div class="example-a">
        <strong class="note-red">第（1）问 · 送分</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>$A(-2,0)$ 在椭圆上 $\\Rightarrow a=2$</li>
          <li>$e=\\dfrac{c}{a}=\\dfrac{\\sqrt{5}}{3}$ $\\Rightarrow c=\\dfrac{2\\sqrt{5}}{3}$</li>
          <li>$b^2=a^2-c^2=4-\\dfrac{20}{9}=\\dfrac{16}{9}$，所以方程为 $\\dfrac{x^2}{4}+\\dfrac{9y^2}{16}=1$</li>
        </ol>

        <strong class="note-red" style="display:block; margin-top:14px;">第（2）问 · 套路：设直线 → 联立 → 韦达 → 代入</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>设直线 $PQ:y-3=k(x+2)$，即 $y=kx+2k+3$</li>
          <li>联立椭圆方程：$\\dfrac{x^2}{4}+\\dfrac{9(kx+2k+3)^2}{16}=1$</li>
          <li>整理得 $(4+9k^2)x^2+18k(2k+3)x+9(2k+3)^2-16=0$</li>
          <li>设 $P(x_1,y_1),Q(x_2,y_2)$，由韦达：$x_1+x_2=-\\dfrac{18k(2k+3)}{4+9k^2}$，$x_1x_2=\\dfrac{9(2k+3)^2-16}{4+9k^2}$</li>
          <li>直线 $AP:y=\\dfrac{y_1}{x_1+2}(x+2)$，令 $x=0$ 得 $M\\left(0,\\dfrac{2y_1}{x_1+2}\\right)$；同理 $N\\left(0,\\dfrac{2y_2}{x_2+2}\\right)$</li>
          <li>中点纵坐标 $=\\dfrac{1}{2}\\left(\\dfrac{2y_1}{x_1+2}+\\dfrac{2y_2}{x_2+2}\\right)=\\dfrac{y_1}{x_1+2}+\\dfrac{y_2}{x_2+2}$，代入 $y=kx+2k+3$ 化简得 $=3$</li>
          <li>所以 $MN$ 中点为定点 $(0,3)$</li>
        </ol>
      </div>
    </div>

    <p class="note-red" style="font-size:0.88rem; margin-top:14px;">
      ※ 第（2）问即使没证出中点是定点，<span class="mark">设直线、联立、写韦达、写 $M,N$ 坐标这四步写出来就有 6 分</span>。圆锥曲线是"步骤分之王"。
    </p>
  </section>'''

# 5. 导数
old5 = '''  <!-- ============ 6. 导数 ============ -->
  <div class="topic-header" id="deriv">
    <h2>⑥ 导数</h2>
    <div class="topic-meta">第 22 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>求导 → 分析正负 → 列表 → 结论。<span class="mark">第一问稳拿，第二问能写多少写多少</span>。
  </div>

  <div class="placeholder">
    <div class="placeholder-stamp">UNDER CONSTRUCTION</div>
    <div class="placeholder-title">导数大题模板 · 内容补充中</div>
    <p style="font-size:0.85rem; margin-top:8px;">
      将包含：<br>
      · 求单调区间标准四步<br>
      · 切线方程模板<br>
      · 证不等式的"构造函数法"<br>
      · 含参讨论的分类思路<br>
      · 真题示范
    </p>
  </div>'''

new5 = '''  <!-- ============ 6. 导数 ============ -->
  <div class="topic-header" id="deriv">
    <h2>⑥ 导数</h2>
    <div class="topic-meta">第 22 题 · 12 分</div>
  </div>

  <div class="topic-tldr">
    <strong>核心套路：</strong>求导 → 分析正负 → 列表 → 结论。<span class="mark">第一问稳拿 4 分，第二问能写多少写多少。</span>
  </div>

  <section class="card">
    <h3 class="card-title">套路总纲</h3>
    <ol class="steps">
      <li>
        <strong>写定义域</strong>
        <span class="step-note">求单调区间、极值、最值，<span class="mark">第一步必须先写定义域</span>。漏写扣 1 分。</span>
      </li>
      <li>
        <strong>求导 $f'(x)$</strong><br>
        基本公式 + 四则运算 + 复合函数求导。<br>
        <span class="mark">求导对了就有 1-2 分。</span>
        <span class="step-note">分式求导最容易错：分子是"前导后不导 减 前不导后导"，分母是原分母的平方。</span>
      </li>
      <li>
        <strong>解 $f'(x)=0$</strong><br>
        令导函数等于零，解出临界点 $x_1,x_2,\\dots$。<br>
        含参时要分类讨论：参数 $>0$、$=0$、$<0$ 三种情况。
        <span class="step-note">分类讨论时，<span class="mark">每讨论一种情况就有 1 分</span>。三类全讨论完，即使结论不对也有 3 分。</span>
      </li>
      <li>
        <strong>列表判正负</strong><br>
        画出 $x$、$f'(x)$、$f(x)$ 的变化表，标清单调区间和极值点。<br>
        <span class="mark">列表是得分利器</span>，即使文字描述不清楚，表格一目了然。
        <span class="step-note">$f'(x)>0$ 对应增区间，$f'(x)<0$ 对应减区间。临界点处可能是极大/极小值。</span>
      </li>
      <li>
        <strong>下结论</strong><br>
        "综上，$f(x)$ 在 $(a,b)$ 上单调递增，在 $(b,c)$ 上单调递减，极大值为 $f(b)=\\dots$"
        <span class="step-note">结论写清楚，不要省略。"综上所述"四个字值 1 分。</span>
      </li>
    </ol>
  </section>

  <section class="card">
    <h3 class="card-title">三类高频第二问</h3>

    <div class="formula-block">
      <div class="formula-name">题型 A · 切线方程（第一问常见）<span class="formula-tag">送分</span></div>
      过曲线上一点 $(x_0,f(x_0))$ 的切线：$y-f(x_0)=f'(x_0)(x-x_0)$。<br>
      <span class="mark">"在"点 = 该点就是切点；"过"点 = 该点不一定是切点，要先设切点再列方程。</span>
    </div>

    <div class="formula-block">
      <div class="formula-name">题型 B · 证不等式 $f(x)\\ge g(x)$<span class="formula-tag">中档</span></div>
      <strong>套路：</strong>构造函数 $h(x)=f(x)-g(x)$ → 求 $h'(x)$ → 求 $h(x)_{\\min}$ → 证 $h(x)_{\\min}\\ge 0$。<br>
      <span class="mark">核心思路：把不等式问题转化为最值问题。</span>
    </div>

    <div class="formula-block">
      <div class="formula-name">题型 C · 含参讨论（第二问压轴）<span class="formula-tag">难点</span></div>
      按参数分类：$a>0$、$a=0$、$a<0$ 逐类画图/列表。<br>
      <span class="mark">分类标准从导函数的零点入手</span>：$f'(x)=0$ 有几个根？根是否在定义域内？根的大小关系？
    </div>
  </section>

  <section class="card">
    <h3 class="card-title">真题示范 · 2023 新高考 I 卷 22 题（节选）</h3>

    <div class="example">
      <span class="example-tag">2023 · 新高考I卷</span>
      <div class="example-q">
        已知函数 $f(x)=a(e^x+a)-x$。<br>
        (1) 讨论 $f(x)$ 的单调性；<br>
        (2) 证明：当 $a>0$ 时，$f(x)>2\\ln a+\\dfrac{3}{2}$。
      </div>
      <div class="example-a">
        <strong class="note-red">第（1）问 · 套路：定义域 → 求导 → 分类讨论</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>定义域：$x\\in\\mathbb{R}$</li>
          <li>$f'(x)=ae^x-1$</li>
          <li>令 $f'(x)=0$，得 $x=-\\ln a$（$a>0$ 时）</li>
          <li>当 $a\\le 0$ 时，$f'(x)=ae^x-1<0$，$f(x)$ 在 $\\mathbb{R}$ 上单调递减</li>
          <li>当 $a>0$ 时：$x<-\\ln a$ 时 $f'(x)<0$，$f(x)$ 递减；$x>-\\ln a$ 时 $f'(x)>0$，$f(x)$ 递增</li>
        </ol>

        <strong class="note-red" style="display:block; margin-top:14px;">第（2）问 · 套路：构造函数证最值</strong>
        <ol class="steps" style="margin-top:8px;">
          <li>由（1）知 $a>0$ 时 $f(x)$ 在 $x=-\\ln a$ 处取最小值</li>
          <li>$f(-\\ln a)=a(e^{-\\ln a}+a)+\\ln a=a\\left(\\dfrac{1}{a}+a\\right)+\\ln a=1+a^2+\\ln a$</li>
          <li>设 $g(a)=1+a^2+\\ln a-2\\ln a-\\dfrac{3}{2}=a^2-\\ln a-\\dfrac{1}{2}$（$a>0$）</li>
          <li>$g'(a)=2a-\\dfrac{1}{a}=\\dfrac{2a^2-1}{a}$，令 $g'(a)=0$ 得 $a=\\dfrac{\\sqrt{2}}{2}$</li>
          <li>$g(a)$ 在 $\\left(0,\\dfrac{\\sqrt{2}}{2}\\right)$ 递减，在 $\\left(\\dfrac{\\sqrt{2}}{2},+\\infty\\right)$ 递增</li>
          <li>$g(a)_{\\min}=g\\left(\\dfrac{\\sqrt{2}}{2}\\right)=\\dfrac{1}{2}-\\ln\\dfrac{\\sqrt{2}}{2}-\\dfrac{1}{2}=-\\ln\\dfrac{\\sqrt{2}}{2}=\\ln\\sqrt{2}>0$</li>
          <li>所以 $g(a)>0$，即 $f(x)_{\\min}>2\\ln a+\\dfrac{3}{2}$，得证</li>
        </ol>
      </div>
    </div>

    <p class="note-red" style="font-size:0.88rem; margin-top:14px;">
      ※ 第（1）问写出定义域、求导、分类讨论三步，<span class="mark">就有 4 分</span>。第（2）问把"求最小值 → 构造函数 → 求导"的框架写出来，<span class="mark">就有 4-6 分</span>。导数大题是"写就有分"的典型。
    </p>
  </section>'''

for i, (old, new) in enumerate([(old1,new1),(old2,new2),(old3,new3),(old4,new4),(old5,new5)], 1):
    if old in content:
        content = content.replace(old, new)
        print(f'Replaced {i}/5')
    else:
        print(f'ERROR: {i}/5 not found')

with open('templates.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
