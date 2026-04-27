// ===== 高考倒计时 =====
const GAOKAO = new Date('2026-06-07T09:00:00+08:00');

// ===== 7 日循环任务表 =====
// 周一三角 / 周二数列 / 周三立体几何 / 周四概率 / 周五圆锥 / 周六导数 / 周日选填限时
const WEEK_PLAN = {
  1: { topic: '三角函数日', link: 'modules/trig.html',
    tasks: [
      { title: '背诱导公式 + 辅助角公式', desc: '10 分钟，记不住就背口诀「奇变偶不变，符号看象限」' },
      { title: '刷 5 道选填限时题', desc: '每道 3 分钟，超时直接看答案不死磕' },
      { title: '看一遍三角函数大题模板', desc: '不抄不写，过一遍流程就行' },
    ]},
  2: { topic: '数列日', link: 'modules/sequence.html',
    tasks: [
      { title: '背等差/等比通项 + 求和公式', desc: '加上错位相减、裂项相消的形式' },
      { title: '刷 3 道数列大题第一问', desc: '只做求通项的部分，求和那一问可以先不做' },
      { title: '过一遍「已知 Sₙ 求 aₙ」标准三步', desc: '看模板页就行' },
    ]},
  3: { topic: '立体几何日', link: 'modules/solid.html',
    tasks: [
      { title: '背线面平行/垂直判定定理', desc: '一句话能说清就行，不用一字不差' },
      { title: '练 1 道建系题', desc: '重点是建系四步：找原点、定轴、求点、求向量' },
      { title: '看一遍二面角法向量公式', desc: 'cos 值要不要取相反数，别再纠结了——看图就好' },
    ]},
  4: { topic: '概率统计日', link: 'modules/prob.html',
    tasks: [
      { title: '区分古典概型/二项分布/超几何', desc: '一眼能认出来题型最重要' },
      { title: '写 1 道分布列三步法', desc: '设 X、列分布、求 E(X)，三步一步不能少' },
      { title: '背二项分布期望方差公式', desc: 'E(X)=np, D(X)=np(1-p)' },
    ]},
  5: { topic: '圆锥曲线日', link: 'modules/conic.html',
    tasks: [
      { title: '背椭圆/抛物线标准方程 + 焦点公式', desc: 'a²=b²+c² 别背反了' },
      { title: '过一遍联立方程「五步法」', desc: '设 → 立 → 判 → 韦达 → 代' },
      { title: '试做 1 道大题前两步', desc: '设直线、联立、写韦达定理——不算到底也有 6 分' },
    ]},
  6: { topic: '导数日', link: 'modules/derivative.html',
    tasks: [
      { title: '背基本求导公式表', desc: '幂、指、对、三角，一个不能漏' },
      { title: '练 1 道求单调区间', desc: '记住四步：定义域 → 求导 → 解 f\'=0 → 列表判正负' },
      { title: '看一遍切线方程模板', desc: '知道斜率怎么求、点在不在曲线上' },
    ]},
  0: { topic: '选填限时训练日', link: 'templates.html',
    tasks: [
      { title: '限时刷 8 道选择题', desc: '每道 90 秒，超时直接选 B 或 C，标记题号晚上看解析' },
      { title: '限时刷 4 道填空题', desc: '每道 2 分钟，特殊值法、排除法都用上' },
      { title: '复盘本周错题', desc: '哪天的题型错最多，下周该日多花 10 分钟' },
    ]},
};

function updateCountdown() {
  const el = document.getElementById('countdown-num');
  if (!el) return;
  const now = new Date();
  const diff = GAOKAO - now;
  const days = Math.max(0, Math.ceil(diff / (1000 * 60 * 60 * 24)));
  el.textContent = days;
}

// 渲染今日任务（基于真实日期）
function renderTodayTasks() {
  const wrap = document.getElementById('today-tasks');
  if (!wrap) return;

  const now = new Date();
  const dow = now.getDay(); // 0=Sun, 1=Mon, ..., 6=Sat
  const plan = WEEK_PLAN[dow];

  // D-X
  const diffDays = Math.max(0, Math.ceil((GAOKAO - now) / (1000 * 60 * 60 * 24)));
  const dLabel = `D-${diffDays}`;

  // 今日主题
  const titleEl = document.getElementById('today-title');
  if (titleEl) titleEl.textContent = `今日任务（${dLabel} · ${plan.topic}）`;

  const todayKey = now.toISOString().slice(0, 10);
  const html = plan.tasks.map((t, i) => {
    const key = `task-${todayKey}-${i}`;
    const done = localStorage.getItem(key) === '1';
    return `
      <div class="task-item">
        <span class="task-check ${done ? 'done' : ''}" data-key="${key}"></span>
        <div class="task-content">
          <div class="task-title">${t.title}</div>
          <div class="task-desc">${t.desc}</div>
        </div>
      </div>`;
  }).join('');

  wrap.innerHTML = html + `
    <p class="note-red" style="margin-top:14px; font-size:0.88rem;">
      ※ 任务勾选保存在这台设备，每天自动重置。
      <a href="${plan.link}" style="color:var(--ochre); margin-left:8px;">→ 直达今日模块</a>
    </p>`;

  wrap.querySelectorAll('.task-check').forEach(el => {
    el.addEventListener('click', () => {
      el.classList.toggle('done');
      localStorage.setItem(el.dataset.key, el.classList.contains('done') ? '1' : '0');
    });
  });
}

// 鸡汤句（倒计时下方）
const QUOTES = [
  '撑住，最后一个月。',
  '你已经走了很远，剩下的路也走得到。',
  '不慌，一题一题来。',
  '现在累的每一分钟，六月都会还给你。',
  '比起聪明，坚持更重要。',
  '题目会做完，焦虑也会过去。',
  '今天比昨天多会一点点，就够了。',
  '考场上你不是一个人，我们都在。',
  '数学不是你的敌人，时间才是——所以慢慢来反而最快。',
  '把会的拿稳，比追难题划算。',
];
function setQuote() {
  const el = document.getElementById('quote');
  if (!el) return;
  el.textContent = QUOTES[Math.floor(Math.random() * QUOTES.length)];
}

document.addEventListener('DOMContentLoaded', () => {
  updateCountdown();
  setQuote();
  renderTodayTasks();
  setInterval(updateCountdown, 60000);
});
