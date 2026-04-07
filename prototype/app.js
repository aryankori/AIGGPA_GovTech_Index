/* ============================================================
   GovTech Adoption Index — Application Logic
   AIGGPA Bhopal | Prototype
   ============================================================ */

// ==================== CONSTANTS ====================
const STORAGE_KEY = 'govtech_adoption_responses';
const DEPARTMENTS = ['Revenue', 'PWD', 'Health', 'Education'];
const DEPT_COLORS = {
    Revenue: { bg: 'rgba(27,59,111,0.7)', border: '#1B3B6F' },
    PWD: { bg: 'rgba(255,193,7,0.7)', border: '#FFC107' },
    Health: { bg: 'rgba(231,76,60,0.7)', border: '#E74C3C' },
    Education: { bg: 'rgba(142,68,173,0.7)', border: '#8E44AD' }
};

const CHART_CONFIG = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
        legend: {
            labels: { color: '#8899AB', font: { family: 'Inter', size: 11 }, padding: 16 }
        }
    },
    scales: {
        x: {
            ticks: { color: '#8899AB', font: { family: 'Inter', size: 11 } },
            grid: { color: 'rgba(30,48,80,0.5)' }
        },
        y: {
            ticks: { color: '#8899AB', font: { family: 'Inter', size: 11 } },
            grid: { color: 'rgba(30,48,80,0.5)' }
        }
    }
};

let charts = {};

// ==================== DATA MANAGEMENT ====================
function getResponses() {
    try {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    } catch { return []; }
}

function saveResponse(response) {
    const responses = getResponses();
    response.id = Date.now();
    response.timestamp = new Date().toISOString();
    response.tier = computeTier(response);
    response.adoptionIndex = computeAdoptionIndex(response);
    responses.push(response);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(responses));
    return response;
}

function clearAllData() {
    if (!confirm('Delete all collected data? This cannot be undone.')) return;
    localStorage.removeItem(STORAGE_KEY);
    refreshAll();
}

// ==================== INDEX COMPUTATION ====================
function computeAdoptionIndex(r) {
    // Weights (sum to 1.0)
    const w = { dp: 0.20, lf: 0.15, cs: 0.20, ai: 0.15, hr: 0.15, fs: 0.15 };

    const dp = (r.digitalPenetration || 0) / 100;
    const lf = Math.min((r.loginFrequency || 0) / 60, 1); // normalize to 60 logins/month max
    const cs = ((r.confidence || 3) - 1) / 4; // 1-5 -> 0-1
    const ai = (r.awarenessCount || 0) / 10;
    const hr = (r.hardwareRatio || 0) / 100;
    const fs = ((r.frustration || 3) - 1) / 4; // reverse — higher frustration = lower score

    const raw = w.dp * dp + w.lf * lf + w.cs * cs + w.ai * ai + w.hr * hr - w.fs * fs;
    return Math.round(Math.max(0, Math.min(100, raw * 100)));
}

function computeTier(r) {
    const idx = r.adoptionIndex || computeAdoptionIndex(r);
    if (idx >= 55) return 'Tier 1';
    if (idx >= 30) return 'Tier 2';
    return 'Tier 3';
}

// ==================== MOCK DATA ====================
function loadMockData() {
    if (getResponses().length > 0) {
        if (!confirm('This will add 120 demo records. Continue?')) return;
    }

    const firstNames = ['Rajesh', 'Priya', 'Amit', 'Sunita', 'Vikram', 'Neha', 'Deepak', 'Kavita', 'Suresh', 'Meena',
        'Arjun', 'Pooja', 'Sanjay', 'Anita', 'Ramesh', 'Rekha', 'Manoj', 'Shweta', 'Vijay', 'Geeta',
        'Anil', 'Parveen', 'Rohit', 'Sapna', 'Ashok', 'Nisha', 'Rahul', 'Mamta', 'Prakash', 'Seema'];
    const lastNames = ['Sharma', 'Verma', 'Singh', 'Patel', 'Gupta', 'Jain', 'Thakur', 'Yadav', 'Mishra', 'Tiwari',
        'Chauhan', 'Dubey', 'Pandey', 'Shukla', 'Agrawal', 'Rajput', 'Chouhan', 'Bhatia', 'Saxena', 'Dwivedi'];

    const profiles = {
        Revenue: {
            dpRange: [45, 90], lfRange: [10, 50], hwRange: [60, 95], connRange: [70, 98],
            confBias: 0.6, frusBias: 0.3, gradeWeights: { 'Group A': 0.15, 'Group B': 0.35, 'Group C': 0.50 }
        },
        PWD: {
            dpRange: [25, 70], lfRange: [5, 35], hwRange: [40, 80], connRange: [50, 85],
            confBias: 0.4, frusBias: 0.45, gradeWeights: { 'Group A': 0.15, 'Group B': 0.30, 'Group C': 0.55 }
        },
        Health: {
            dpRange: [15, 55], lfRange: [3, 25], hwRange: [25, 65], connRange: [35, 75],
            confBias: 0.3, frusBias: 0.55, gradeWeights: { 'Group A': 0.10, 'Group B': 0.30, 'Group C': 0.60 }
        },
        Education: {
            dpRange: [10, 45], lfRange: [2, 20], hwRange: [20, 55], connRange: [25, 65],
            confBias: 0.25, frusBias: 0.6, gradeWeights: { 'Group A': 0.10, 'Group B': 0.25, 'Group C': 0.65 }
        }
    };

    const genders = ['Male', 'Female'];
    const ages = ['<30', '30-40', '41-50', '50+'];
    const educations = ['12th/Diploma', 'Graduate', 'Post-Graduate', 'Professional'];
    const locations = ['State Capital', 'District HQ', 'Tehsil/Block', 'Field/Mobile'];
    const serviceYears = ['0-5', '6-15', '16-25', '25+'];
    const barriers = ['No Hardware', 'No Training', 'No Internet', 'No Need', 'Fear/Discomfort'];
    const platforms = ['e-Office', 'e-HRMS', 'iGOT', 'SPARROW', 'GeM', 'PFMS', 'CPGRAMS', 'Parichay', 'AEBAS', 'DSC'];

    function rand(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
    function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
    function weightedPick(weights) {
        const r = Math.random();
        let sum = 0;
        for (const [k, w] of Object.entries(weights)) { sum += w; if (r < sum) return k; }
        return Object.keys(weights).pop();
    }
    function likert(bias) {
        // bias 0-1: 0=low scores, 1=high scores
        const r = Math.random();
        if (r < bias * 0.4) return 5;
        if (r < bias * 0.7) return 4;
        if (r < bias * 0.85 + 0.15) return 3;
        if (r < bias * 0.9 + 0.3) return 2;
        return 1;
    }

    const records = [];
    for (const dept of DEPARTMENTS) {
        const p = profiles[dept];
        for (let i = 0; i < 30; i++) {
            const grade = weightedPick(p.gradeWeights);
            const ageGroup = pick(ages);

            // Older age = lower digital penetration modifier
            let ageMod = ageGroup === '<30' ? 1.15 : ageGroup === '30-40' ? 1.0 : ageGroup === '41-50' ? 0.85 : 0.65;
            // Higher grade = higher digital penetration modifier
            let gradeMod = grade === 'Group A' ? 1.2 : grade === 'Group B' ? 1.0 : 0.8;

            const dp = Math.min(100, Math.max(0, rand(p.dpRange[0], p.dpRange[1]) * ageMod * gradeMod));
            const lf = Math.min(100, Math.max(0, rand(p.lfRange[0], p.lfRange[1]) * ageMod * gradeMod));

            const awarenessBase = Math.round(dp / 10);
            const awareness = [];
            const shuffled = [...platforms].sort(() => Math.random() - 0.5);
            for (let j = 0; j < Math.min(awarenessBase + rand(0, 2), 10); j++) {
                awareness.push(shuffled[j]);
            }

            const record = {
                respondentName: pick(firstNames) + ' ' + pick(lastNames),
                department: dept,
                gender: Math.random() < 0.35 ? 'Female' : 'Male',
                ageGroup: ageGroup,
                grade: grade,
                education: pick(educations),
                location: pick(locations),
                serviceYears: pick(serviceYears),
                digitalPenetration: Math.round(dp),
                loginFrequency: Math.round(lf),
                igotCompletion: rand(Math.round(p.dpRange[0] * 0.5), Math.round(p.dpRange[1] * 0.8)),
                hardwareRatio: rand(p.hwRange[0], p.hwRange[1]),
                connectivityUptime: rand(p.connRange[0], p.connRange[1]),
                confidence: likert(p.confBias * ageMod),
                frustration: likert(p.frusBias / ageMod),
                willingness: likert(0.65),
                supervisorMandate: likert(p.confBias * 0.8),
                peerInfluence: likert(0.5),
                awarenessItems: awareness,
                awarenessCount: awareness.length,
                paperDependency: likert(p.frusBias / ageMod),
                primaryBarrier: pick(barriers)
            };

            record.adoptionIndex = computeAdoptionIndex(record);
            record.tier = computeTier(record);
            records.push(record);
        }
    }

    // Save to localStorage
    const existing = getResponses();
    records.forEach(r => {
        r.id = Date.now() + Math.random();
        r.timestamp = new Date().toISOString();
    });
    localStorage.setItem(STORAGE_KEY, JSON.stringify([...existing, ...records]));
    refreshAll();
    showToast();
}

// ==================== UI UPDATES ====================
function refreshAll() {
    updateKPIs();
    updateTierPercents();
    updateResponseCount();
    updateStorageInfo();
    renderDataTable();
    renderCharts();
}

function updateKPIs() {
    const data = getResponses();
    document.getElementById('kpi-responses').textContent = data.length;

    if (data.length === 0) {
        document.getElementById('kpi-avgindex').textContent = '—';
        document.getElementById('kpi-tier1').textContent = '—';
        return;
    }

    const avg = Math.round(data.reduce((s, r) => s + (r.adoptionIndex || 0), 0) / data.length);
    document.getElementById('kpi-avgindex').textContent = avg + '/100';

    const tier1 = data.filter(r => r.tier === 'Tier 1').length;
    document.getElementById('kpi-tier1').textContent = Math.round(tier1 / data.length * 100) + '%';
}

function updateTierPercents() {
    const data = getResponses();
    if (data.length === 0) {
        ['tier1-pct', 'tier2-pct', 'tier3-pct'].forEach(id => document.getElementById(id).textContent = '—');
        return;
    }
    const t1 = data.filter(r => r.tier === 'Tier 1').length;
    const t2 = data.filter(r => r.tier === 'Tier 2').length;
    const t3 = data.filter(r => r.tier === 'Tier 3').length;
    document.getElementById('tier1-pct').textContent = Math.round(t1 / data.length * 100) + '%';
    document.getElementById('tier2-pct').textContent = Math.round(t2 / data.length * 100) + '%';
    document.getElementById('tier3-pct').textContent = Math.round(t3 / data.length * 100) + '%';
}

function updateResponseCount() {
    document.getElementById('responseCount').textContent = getResponses().length;
}

function updateStorageInfo() {
    const data = getResponses();
    document.getElementById('storageCount').textContent = data.length;
    const raw = localStorage.getItem(STORAGE_KEY) || '';
    const kb = (new Blob([raw]).size / 1024).toFixed(1);
    document.getElementById('storageSize').textContent = kb + ' KB';
    if (data.length > 0) {
        const last = data[data.length - 1].timestamp;
        document.getElementById('storageLastUpdate').textContent = new Date(last).toLocaleDateString('en-IN', {
            day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit'
        });
    } else {
        document.getElementById('storageLastUpdate').textContent = '—';
    }
}

// ==================== DATA TABLE ====================
function renderDataTable() {
    const data = getResponses();
    const deptFilter = document.getElementById('filterDept').value;
    const gradeFilter = document.getElementById('filterGrade').value;

    let filtered = data;
    if (deptFilter !== 'all') filtered = filtered.filter(r => r.department === deptFilter);
    if (gradeFilter !== 'all') filtered = filtered.filter(r => r.grade === gradeFilter);

    const tbody = document.getElementById('dataTableBody');
    const empty = document.getElementById('dataEmpty');
    const table = document.getElementById('dataTable');

    if (filtered.length === 0) {
        tbody.innerHTML = '';
        table.style.display = 'none';
        empty.style.display = 'block';
        return;
    }

    table.style.display = 'table';
    empty.style.display = 'none';

    tbody.innerHTML = filtered.map((r, i) => {
        const tierClass = r.tier === 'Tier 1' ? 't1' : r.tier === 'Tier 2' ? 't2' : 't3';
        const indexColor = r.adoptionIndex >= 55 ? '#27AE60' : r.adoptionIndex >= 30 ? '#E67E22' : '#E74C3C';
        return `<tr>
            <td>${i + 1}</td>
            <td>${r.respondentName || '—'}</td>
            <td>${r.department}</td>
            <td>${r.grade}</td>
            <td>${r.gender}</td>
            <td>${r.ageGroup}</td>
            <td>${r.location}</td>
            <td>${r.digitalPenetration}%</td>
            <td>${r.confidence}/5</td>
            <td>${r.serviceYears}</td>
            <td>${r.awarenessCount}/10</td>
            <td><span class="tier-tag ${tierClass}">${r.tier}</span></td>
            <td class="index-score" style="color:${indexColor}">${r.adoptionIndex}</td>
        </tr>`;
    }).join('');
}

// ==================== CSV EXPORT ====================
function exportCSV() {
    const data = getResponses();
    if (data.length === 0) { alert('No data to export.'); return; }

    const headers = ['ID', 'Name', 'Department', 'Gender', 'Age Group', 'Grade', 'Education', 'Location',
        'Service Years', 'Digital Penetration %', 'Login Frequency', 'iGOT Completion %', 'Hardware Ratio %',
        'Connectivity Uptime %', 'Confidence', 'Frustration', 'Willingness', 'Supervisor Mandate',
        'Peer Influence', 'Awareness Count', 'Paper Dependency', 'Primary Barrier', 'Tier', 'Adoption Index', 'Timestamp'];

    const rows = data.map(r => [
        r.id, r.respondentName, r.department, r.gender, r.ageGroup, r.grade, r.education, r.location,
        r.serviceYears, r.digitalPenetration, r.loginFrequency, r.igotCompletion, r.hardwareRatio,
        r.connectivityUptime, r.confidence, r.frustration, r.willingness, r.supervisorMandate,
        r.peerInfluence, r.awarenessCount, r.paperDependency, r.primaryBarrier, r.tier, r.adoptionIndex, r.timestamp
    ]);

    const csv = [headers.join(','), ...rows.map(r => r.map(v => `"${v}"`).join(','))].join('\n');
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `govtech_adoption_data_${new Date().toISOString().slice(0,10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
}

// ==================== CHARTS ====================
function renderCharts() {
    const data = getResponses();
    const grid = document.getElementById('analyticsGrid');
    const empty = document.getElementById('analyticsEmpty');

    if (data.length === 0) {
        grid.style.display = 'none';
        empty.style.display = 'block';
        return;
    }

    grid.style.display = 'grid';
    empty.style.display = 'none';

    // Destroy existing charts
    Object.values(charts).forEach(c => c.destroy());
    charts = {};

    renderAdoptionIndexChart(data);
    renderTierDistChart(data);
    renderGenderChart(data);
    renderAgeChart(data);
    renderBarriersChart(data);
    renderPerceptionsChart(data);
    renderGradeAdoptionChart(data);
}

function renderAdoptionIndexChart(data) {
    const avgByDept = {};
    DEPARTMENTS.forEach(d => {
        const deptData = data.filter(r => r.department === d);
        avgByDept[d] = deptData.length ? Math.round(deptData.reduce((s, r) => s + r.adoptionIndex, 0) / deptData.length) : 0;
    });

    charts.adoptionIndex = new Chart(document.getElementById('chartAdoptionIndex'), {
        type: 'bar',
        data: {
            labels: DEPARTMENTS.map(d => d === 'Education' ? 'Education' : d),
            datasets: [{
                label: 'Adoption Index',
                data: DEPARTMENTS.map(d => avgByDept[d]),
                backgroundColor: DEPARTMENTS.map(d => DEPT_COLORS[d].bg),
                borderColor: DEPARTMENTS.map(d => DEPT_COLORS[d].border),
                borderWidth: 2,
                borderRadius: 8,
                barPercentage: 0.6
            }]
        },
        options: {
            ...CHART_CONFIG,
            plugins: {
                ...CHART_CONFIG.plugins,
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: ctx => `Adoption Index: ${ctx.parsed.y}/100`
                    }
                }
            },
            scales: {
                ...CHART_CONFIG.scales,
                y: { ...CHART_CONFIG.scales.y, min: 0, max: 100, title: { display: true, text: 'Index Score (0-100)', color: '#8899AB' } }
            }
        }
    });
}

function renderTierDistChart(data) {
    const tierByDept = {};
    DEPARTMENTS.forEach(d => {
        const dd = data.filter(r => r.department === d);
        tierByDept[d] = {
            t1: dd.filter(r => r.tier === 'Tier 1').length,
            t2: dd.filter(r => r.tier === 'Tier 2').length,
            t3: dd.filter(r => r.tier === 'Tier 3').length
        };
    });

    charts.tierDist = new Chart(document.getElementById('chartTierDist'), {
        type: 'bar',
        data: {
            labels: DEPARTMENTS,
            datasets: [
                {
                    label: 'Tier 1 (Active)',
                    data: DEPARTMENTS.map(d => tierByDept[d].t1),
                    backgroundColor: 'rgba(39,174,96,0.7)',
                    borderRadius: 4
                },
                {
                    label: 'Tier 2 (Hesitant)',
                    data: DEPARTMENTS.map(d => tierByDept[d].t2),
                    backgroundColor: 'rgba(230,126,34,0.7)',
                    borderRadius: 4
                },
                {
                    label: 'Tier 3 (Unaware)',
                    data: DEPARTMENTS.map(d => tierByDept[d].t3),
                    backgroundColor: 'rgba(231,76,60,0.7)',
                    borderRadius: 4
                }
            ]
        },
        options: {
            ...CHART_CONFIG,
            plugins: { ...CHART_CONFIG.plugins },
            scales: {
                x: { ...CHART_CONFIG.scales.x, stacked: true },
                y: { ...CHART_CONFIG.scales.y, stacked: true }
            }
        }
    });
}

function renderGenderChart(data) {
    const counts = {};
    data.forEach(r => { counts[r.gender] = (counts[r.gender] || 0) + 1; });

    charts.gender = new Chart(document.getElementById('chartGender'), {
        type: 'doughnut',
        data: {
            labels: Object.keys(counts),
            datasets: [{
                data: Object.values(counts),
                backgroundColor: ['rgba(46,134,193,0.7)', 'rgba(193,154,62,0.7)', 'rgba(142,68,173,0.5)'],
                borderColor: ['#2E86C1', '#C19A3E', '#8E44AD'],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { position: 'bottom', labels: { color: '#8899AB', font: { family: 'Inter', size: 11 }, padding: 12 } }
            }
        }
    });
}

function renderAgeChart(data) {
    const ages = ['<30', '30-40', '41-50', '50+'];
    const counts = {};
    ages.forEach(a => counts[a] = 0);
    data.forEach(r => { if (counts[r.ageGroup] !== undefined) counts[r.ageGroup]++; });

    charts.age = new Chart(document.getElementById('chartAge'), {
        type: 'bar',
        data: {
            labels: ages.map(a => a === '<30' ? 'Below 30' : a === '50+' ? '50+' : a),
            datasets: [{
                label: 'Respondents',
                data: ages.map(a => counts[a]),
                backgroundColor: ['rgba(46,134,193,0.6)', 'rgba(39,174,96,0.6)', 'rgba(230,126,34,0.6)', 'rgba(231,76,60,0.6)'],
                borderRadius: 6,
                barPercentage: 0.7
            }]
        },
        options: {
            ...CHART_CONFIG,
            plugins: { ...CHART_CONFIG.plugins, legend: { display: false } }
        }
    });
}

function renderBarriersChart(data) {
    const barriers = ['No Hardware', 'No Training', 'No Internet', 'No Need', 'Fear/Discomfort'];
    const counts = {};
    barriers.forEach(b => counts[b] = 0);
    data.forEach(r => { if (r.primaryBarrier && counts[r.primaryBarrier] !== undefined) counts[r.primaryBarrier]++; });

    charts.barriers = new Chart(document.getElementById('chartBarriers'), {
        type: 'doughnut',
        data: {
            labels: barriers,
            datasets: [{
                data: barriers.map(b => counts[b]),
                backgroundColor: [
                    'rgba(231,76,60,0.7)', 'rgba(230,126,34,0.7)', 'rgba(46,134,193,0.7)',
                    'rgba(142,68,173,0.7)', 'rgba(193,154,62,0.7)'
                ],
                borderWidth: 2,
                borderColor: '#152238'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { position: 'bottom', labels: { color: '#8899AB', font: { family: 'Inter', size: 10 }, padding: 10 } }
            }
        }
    });
}

function renderPerceptionsChart(data) {
    const metrics = ['confidence', 'frustration', 'willingness', 'supervisorMandate', 'peerInfluence'];
    const metricLabels = ['Confidence', 'Frustration', 'Willingness', 'Supervisor Support', 'Peer Influence'];

    const datasets = DEPARTMENTS.map(dept => {
        const dd = data.filter(r => r.department === dept);
        return {
            label: dept,
            data: metrics.map(m => dd.length ? +(dd.reduce((s, r) => s + (r[m] || 3), 0) / dd.length).toFixed(1) : 0),
            borderColor: DEPT_COLORS[dept].border,
            backgroundColor: DEPT_COLORS[dept].bg.replace('0.7', '0.15'),
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: DEPT_COLORS[dept].border
        };
    });

    charts.perceptions = new Chart(document.getElementById('chartPerceptions'), {
        type: 'radar',
        data: { labels: metricLabels, datasets },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                r: {
                    min: 1, max: 5,
                    ticks: { stepSize: 1, color: '#5A6E82', backdropColor: 'transparent' },
                    grid: { color: 'rgba(30,48,80,0.5)' },
                    angleLines: { color: 'rgba(30,48,80,0.5)' },
                    pointLabels: { color: '#8899AB', font: { family: 'Inter', size: 11 } }
                }
            },
            plugins: {
                legend: { position: 'bottom', labels: { color: '#8899AB', font: { family: 'Inter', size: 11 }, padding: 14 } }
            }
        }
    });
}

function renderGradeAdoptionChart(data) {
    const grades = ['Group A', 'Group B', 'Group C'];
    const avgByGrade = {};
    grades.forEach(g => {
        const gd = data.filter(r => r.grade === g);
        avgByGrade[g] = gd.length ? Math.round(gd.reduce((s, r) => s + r.adoptionIndex, 0) / gd.length) : 0;
    });

    charts.gradeAdoption = new Chart(document.getElementById('chartGradeAdoption'), {
        type: 'bar',
        data: {
            labels: ['Class I / Group A', 'Class II / Group B', 'Class III / Group C'],
            datasets: [{
                label: 'Avg. Adoption Index',
                data: grades.map(g => avgByGrade[g]),
                backgroundColor: ['rgba(46,134,193,0.7)', 'rgba(193,154,62,0.7)', 'rgba(142,68,173,0.7)'],
                borderColor: ['#2E86C1', '#C19A3E', '#8E44AD'],
                borderWidth: 2,
                borderRadius: 8,
                barPercentage: 0.5
            }]
        },
        options: {
            ...CHART_CONFIG,
            indexAxis: 'y',
            plugins: { ...CHART_CONFIG.plugins, legend: { display: false } },
            scales: {
                x: { ...CHART_CONFIG.scales.x, min: 0, max: 100, title: { display: true, text: 'Adoption Index', color: '#8899AB' } },
                y: { ...CHART_CONFIG.scales.y }
            }
        }
    });
}

// ==================== TOAST ====================
function showToast() {
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
}

// ==================== FORM SUBMISSION ====================
document.getElementById('surveyForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const awarenessChecks = document.querySelectorAll('input[name="awareness"]:checked');
    const awarenessItems = Array.from(awarenessChecks).map(c => c.value);

    const response = {
        respondentName: document.getElementById('respondentName').value,
        department: document.getElementById('department').value,
        gender: document.getElementById('gender').value,
        ageGroup: document.getElementById('ageGroup').value,
        grade: document.getElementById('grade').value,
        education: document.getElementById('education').value,
        location: document.getElementById('location').value,
        serviceYears: document.getElementById('serviceYears').value,
        digitalPenetration: parseInt(document.getElementById('digitalPenetration').value) || 0,
        loginFrequency: parseInt(document.getElementById('loginFrequency').value) || 0,
        igotCompletion: parseInt(document.getElementById('igotCompletion').value) || 0,
        hardwareRatio: parseInt(document.getElementById('hardwareRatio').value) || 0,
        connectivityUptime: parseInt(document.getElementById('connectivityUptime').value) || 0,
        confidence: parseInt(document.querySelector('input[name="confidence"]:checked')?.value) || 3,
        frustration: parseInt(document.querySelector('input[name="frustration"]:checked')?.value) || 3,
        willingness: parseInt(document.querySelector('input[name="willingness"]:checked')?.value) || 3,
        supervisorMandate: parseInt(document.querySelector('input[name="supervisorMandate"]:checked')?.value) || 3,
        peerInfluence: parseInt(document.querySelector('input[name="peerInfluence"]:checked')?.value) || 3,
        awarenessItems: awarenessItems,
        awarenessCount: awarenessItems.length,
        paperDependency: parseInt(document.getElementById('paperDependency').value) || 3,
        primaryBarrier: document.getElementById('primaryBarrier').value
    };

    saveResponse(response);
    this.reset();
    refreshAll();
    showToast();
});

// ==================== NAVIGATION ====================
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        const page = this.dataset.page;

        // Update nav
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        this.classList.add('active');

        // Update pages
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.getElementById('page-' + page).classList.add('active');

        // Close mobile sidebar
        document.getElementById('sidebar').classList.remove('open');

        // Refresh charts when switching to analytics
        if (page === 'analytics') renderCharts();
        if (page === 'data') { renderDataTable(); updateStorageInfo(); }
    });
});

// Mobile hamburger
document.getElementById('hamburger').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('open');
});

// ==================== INIT ====================
document.addEventListener('DOMContentLoaded', refreshAll);
