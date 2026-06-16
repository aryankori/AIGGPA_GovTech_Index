import React, { useState } from 'react';
import './ClinicalDashboard.css';

// Crypto Mock Anonymized SHA-256 Hashed Patient Profiles
const mockParticipants = [
  { hash: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', age: '18-24', cohort: 'Intervention A', phq9: 8, gad7: 6, status: 'Mild', adherence: '98%', sleep: '7.8h' },
  { hash: '87b8b21c432d16790a1c1d9f8e7f6e5a4d3c2b1a0987654321abcdef01234567', age: '25-34', cohort: 'Intervention A', phq9: 14, gad7: 12, status: 'Moderate', adherence: '94%', sleep: '6.4h' },
  { hash: 'f6e5d4c3b2a10987654321fedcba09876543210fedcba9876543210abcdef012', age: '18-24', cohort: 'Control', phq9: 19, gad7: 15, status: 'Severe', adherence: '88%', sleep: '5.2h' },
  { hash: 'a1b2c3d4e5f60718293041526374859607182930415263748596071829304152', age: '35-44', cohort: 'Intervention A', phq9: 5, GAD7: 4, status: 'None', adherence: '100%', sleep: '8.1h' },
  { hash: 'c7d8e9f0a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4', age: '25-34', cohort: 'Control', phq9: 11, gad7: 9, status: 'Moderate', adherence: '91%', sleep: '6.9h' },
  { hash: '0987654321abcdef0987654321abcdef0987654321abcdef0987654321abcdef', age: '45-54', cohort: 'Intervention A', phq9: 7, gad7: 5, status: 'Mild', adherence: '96%', sleep: '7.2h' },
  { hash: '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', age: '18-24', cohort: 'Control', phq9: 16, gad7: 14, status: 'Severe', adherence: '85%', sleep: '4.8h' },
  { hash: 'fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210', age: '25-34', cohort: 'Intervention A', phq9: 12, gad7: 10, status: 'Moderate', adherence: '95%', sleep: '7.0h' }
];

const auditTrail = [
  { timestamp: '2026-05-30T21:30:15Z', event: 'AES-256 Key Handshake Successful', node: 'Node-Client_04', status: 'VERIFIED' },
  { timestamp: '2026-05-30T21:15:42Z', event: 'Cohort Demographics De-identified via PBKDF2 salt', node: 'Anonymizer_G3', status: 'SECURED' },
  { timestamp: '2026-05-30T19:44:09Z', event: 'Aggregated PHQ-9 Clinical Export Generated', node: 'Node-Client_01', status: 'EXPORTED' },
  { timestamp: '2026-05-30T18:22:11Z', event: 'WebCrypto Local Decryption Routine Checked', node: 'Security-Core', status: 'ACTIVE' }
];

const ClinicalDashboard = () => {
  const [activeTab, setActiveTab] = useState('summary');
  const [selectedCohort, setSelectedCohort] = useState('all');

  // Dynamic Metrics computing based on cohort selection
  const getCohortMetrics = () => {
    switch (selectedCohort) {
      case 'intervention':
        return {
          total: 62,
          adherence: '96.2%',
          moderateSeverePHQ: '24.1%',
          circadianRating: 'Optimal (7.5h avg)',
          phq9Trend: [75, 62, 48, 35, 22, 18],
          gad7Trend: [68, 55, 41, 30, 19, 14]
        };
      case 'control':
        return {
          total: 58,
          adherence: '87.6%',
          moderateSeverePHQ: '51.7%',
          circadianRating: 'Sub-optimal (5.9h avg)',
          phq9Trend: [76, 73, 71, 68, 67, 65],
          gad7Trend: [69, 68, 66, 64, 63, 62]
        };
      default:
        return {
          total: 120,
          adherence: '92.1%',
          moderateSeverePHQ: '37.5%',
          circadianRating: 'Nominal (6.7h avg)',
          phq9Trend: [75, 68, 60, 51, 44, 41],
          gad7Trend: [68, 61, 53, 47, 41, 38]
        };
    }
  };

  const metrics = getCohortMetrics();

  const handleTabChange = (tab: string) => {
    setActiveTab(tab);
  };

  const handleCohortChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedCohort(e.target.value);
  };

  return (
    <div className="clinical-container">
      {/* Sidebar Navigation */}
      <aside className="clinical-sidebar">
        <div className="clinical-logo">
          <div className="clinical-logo-icon">Ψ</div>
          <h1>AETHER_CLINICAL</h1>
        </div>

        <nav className="clinical-sidebar-nav">
          <button 
            className={`clinical-nav-btn ${activeTab === 'summary' ? 'active' : ''}`}
            onClick={() => handleTabChange('summary')}
          >
            <span>📊</span> Cohort Summary
          </button>
          <button 
            className={`clinical-nav-btn ${activeTab === 'psychometrics' ? 'active' : ''}`}
            onClick={() => handleTabChange('psychometrics')}
          >
            <span>🧠</span> Psychometric Profiler
          </button>
          <button 
            className={`clinical-nav-btn ${activeTab === 'registry' ? 'active' : ''}`}
            onClick={() => handleTabChange('registry')}
          >
            <span>🔒</span> Secure Registry
          </button>
          <button 
            className={`clinical-nav-btn ${activeTab === 'audit' ? 'active' : ''}`}
            onClick={() => handleTabChange('audit')}
          >
            <span>📜</span> Security Audit Trail
          </button>
        </nav>

        {/* Security Badge */}
        <div className="security-badge-container">
          <div className="security-badge-header">
            <span>🛡️</span> Zero PHI Protocol
          </div>
          <p className="security-badge-text">
            AES-256-GCM LOCAL CLIENT ENCRYPTION ENFORCED.<br />
            NO DEMOGRAPHICS READ AT REST.
          </p>
        </div>
      </aside>

      {/* Main Workspace */}
      <main className="clinical-main">
        {/* Header Section */}
        <header className="clinical-header">
          <div className="clinical-header-title">
            <h2>Institutional Clinical Dashboard</h2>
            <p>Evaluating cognitive and psychometric treatment responses under zero-knowledge encryption</p>
          </div>
          <select 
            className="cohort-selector" 
            value={selectedCohort}
            onChange={handleCohortChange}
          >
            <option value="all">COHORT: ALL PARTICIPANTS (N=120)</option>
            <option value="intervention">COHORT: INTERVENTION ALPHA (N=62)</option>
            <option value="control">COHORT: CONTROL ACTIVE (N=58)</option>
          </select>
        </header>

        {/* Key Stats Row */}
        <div className="clinical-stats-grid">
          <div className="clinical-stat-card primary">
            <p className="stat-label">Active Research Cohort</p>
            <div className="stat-value">{metrics.total}</div>
            <p className="stat-indicator gold">Participants Anonymized</p>
          </div>
          <div className="clinical-stat-card success">
            <p className="stat-label">Protocol Adherence Rate</p>
            <div className="stat-value">{metrics.adherence}</div>
            <p className="stat-indicator green">↑ 1.2% Compliance Trend</p>
          </div>
          <div className="clinical-stat-card secondary">
            <p className="stat-label">Circadian Correlation</p>
            <div className="stat-value">6.8h</div>
            <p className="stat-indicator green">{metrics.circadianRating}</p>
          </div>
          <div className="clinical-stat-card accent">
            <p className="stat-label">Severe Symptom Ratio</p>
            <div className="stat-value">{metrics.moderateSeverePHQ}</div>
            <p className="stat-indicator red">PHQ-9 / GAD-7 Scale</p>
          </div>
        </div>

        {/* Dynamic Panels */}
        {activeTab === 'summary' && (
          <div className="clinical-bento-grid fade-in">
            {/* Longitudinal Symptom Decline Chart */}
            <div className="clinical-panel">
              <div className="panel-header">
                <h3>8-Week Longitudinal Treatment Outcomes</h3>
                <span className="panel-header-action">Aggregated Indicators</span>
              </div>
              <p className="security-badge-text" style={{ color: 'var(--text-secondary)' }}>
                Comparing PHQ-9 (Depression Indicator) vs. GAD-7 (Anxiety Baseline) average scores across the cohort.
              </p>
              
              <div className="chart-canvas">
                {metrics.phq9Trend.map((score, idx) => (
                  <div key={`phq-${idx}`} className="bar-col">
                    <span className="bar-val">{Math.round(score / 5)}</span>
                    <div className="bar-fill-container">
                      <div 
                        className="bar-fill" 
                        style={{ height: `${score}%` }}
                      ></div>
                    </div>
                    <span className="bar-label">Wk {idx + 1}</span>
                  </div>
                ))}
              </div>
              <div style={{ display: 'flex', gap: '1.5rem', justifyContent: 'center', fontSize: '0.8rem', fontFamily: 'var(--font-mono)' }}>
                <span style={{ color: 'var(--primary)' }}>■ PHQ-9 Symptom Index</span>
                <span style={{ color: 'var(--secondary)' }}>■ GAD-7 Anxiety Scale</span>
              </div>
            </div>

            {/* Cohort Profile Trait Balance */}
            <div className="clinical-panel">
              <div className="panel-header">
                <h3>Cohort OCEAN Baselines</h3>
                <span className="panel-header-action">Mean Value</span>
              </div>
              <div className="radar-bars-list">
                <div className="trait-bar-item">
                  <div className="trait-bar-header">
                    <span className="trait-name">Openness (Aesthetic / Cognitive)</span>
                    <span className="trait-value">85%</span>
                  </div>
                  <div className="trait-track">
                    <div className="trait-fill" style={{ width: '85%' }}></div>
                  </div>
                </div>
                <div className="trait-bar-item">
                  <div className="trait-bar-header">
                    <span className="trait-name">Conscientiousness (Meticulousness)</span>
                    <span className="trait-value">78%</span>
                  </div>
                  <div className="trait-track">
                    <div className="trait-fill" style={{ width: '78%' }}></div>
                  </div>
                </div>
                <div className="trait-bar-item">
                  <div className="trait-bar-header">
                    <span className="trait-name">Extraversion (Selective Output)</span>
                    <span className="trait-value">65%</span>
                  </div>
                  <div className="trait-track">
                    <div className="trait-fill" style={{ width: '65%' }}></div>
                  </div>
                </div>
                <div className="trait-bar-item">
                  <div className="trait-bar-header">
                    <span className="trait-name">Agreeableness (Relational Res.)</span>
                    <span className="trait-value">80%</span>
                  </div>
                  <div className="trait-track">
                    <div className="trait-fill" style={{ width: '80%' }}></div>
                  </div>
                </div>
                <div className="trait-bar-item">
                  <div className="trait-bar-header">
                    <span className="trait-name">Neuroticism (Somatic Vulnerability)</span>
                    <span className="trait-value">75%</span>
                  </div>
                  <div className="trait-track">
                    <div className="trait-fill" style={{ width: '75%' }}></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'psychometrics' && (
          <div className="clinical-panel fade-in">
            <div className="panel-header">
              <h3>Psychometric Correlates Matrix</h3>
              <span className="panel-header-action">Standard Assessment Correlation</span>
            </div>
            <p className="security-badge-text" style={{ color: 'var(--text-secondary)', marginBottom: '1rem' }}>
              Standardized variables illustrating environmental and circadian connections. 
              Higher circadian sleep alignment is correlated with reduced Neuroticism and Agreeableness stabilization.
            </p>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
              <div className="clinical-panel" style={{ background: 'rgba(0,0,0,0.1)', border: '1px solid rgba(255,255,255,0.03)' }}>
                <h4>Circadian Sunlight Exposure (Mean: 6.8h)</h4>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  Intervention Alpha participants with circadian daylight ratios &gt; 0.65 show a <strong>34% higher</strong> rate of positive GAD-7 anxiety decline.
                </p>
                <div className="chart-canvas" style={{ height: '140px' }}>
                  {/* Mock Circadian chart */}
                  <div className="bar-col"><div className="bar-fill-container" style={{ height: '80px' }}><div className="bar-fill" style={{ height: '30%' }}></div></div><span className="bar-label">&lt;4h</span></div>
                  <div className="bar-col"><div className="bar-fill-container" style={{ height: '80px' }}><div className="bar-fill" style={{ height: '60%' }}></div></div><span className="bar-label">4-6h</span></div>
                  <div className="bar-col"><div className="bar-fill-container" style={{ height: '80px' }}><div className="bar-fill" style={{ height: '90%' }}></div></div><span className="bar-label">6-8h</span></div>
                  <div className="bar-col"><div className="bar-fill-container" style={{ height: '80px' }}><div className="bar-fill" style={{ height: '40%' }}></div></div><span className="bar-label">&gt;8h</span></div>
                </div>
              </div>
              <div className="clinical-panel" style={{ background: 'rgba(0,0,0,0.1)', border: '1px solid rgba(255,255,255,0.03)' }}>
                <h4>Somatic Vulnerability Index (Mean Baseline: 75/100)</h4>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  High Neuroticism indicators are significantly buffered by tactile environmental reassurances and highly consistent sleep loops.
                </p>
                <div className="chart-canvas" style={{ height: '140px' }}>
                  {/* Mock Somatic chart */}
                  <div className="bar-col"><div className="bar-fill-container" style={{ height: '80px' }}><div className="bar-fill control" style={{ height: '85%' }}></div></div><span className="bar-label">Control</span></div>
                  <div className="bar-col"><div className="bar-fill-container" style={{ height: '80px' }}><div className="bar-fill" style={{ height: '45%' }}></div></div><span className="bar-label">Interv.</span></div>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'registry' && (
          <div className="clinical-panel fade-in">
            <div className="panel-header">
              <h3>Secure Anonymized Participant Registry</h3>
              <span className="panel-header-action" onClick={() => alert('Anonymized clinical data exported to CSV!')}>Export Anonymized CSV</span>
            </div>
            
            <div className="registry-table-container">
              <table className="registry-table">
                <thead>
                  <tr>
                    <th>Participant Hash (SHA-256)</th>
                    <th>Age</th>
                    <th>Cohort</th>
                    <th>PHQ-9</th>
                    <th>GAD-7</th>
                    <th>Symptom Severity</th>
                    <th>Adherence</th>
                    <th>Sleep</th>
                  </tr>
                </thead>
                <tbody>
                  {mockParticipants.map((patient, idx) => (
                    <tr key={idx}>
                      <td className="hash-cell" title={patient.hash}>
                        {patient.hash.substring(0, 16)}...
                      </td>
                      <td>{patient.age}</td>
                      <td>
                        <span className={`cohort-badge ${patient.cohort === 'Intervention A' ? 'intervention' : 'control'}`}>
                          {patient.cohort}
                        </span>
                      </td>
                      <td style={{ fontWeight: 600 }}>{patient.phq9}</td>
                      <td style={{ fontWeight: 600 }}>{patient.gad7}</td>
                      <td>
                        <span className="severity-indicator">
                          <span className={`dot ${patient.status === 'Severe' ? 'red' : patient.status === 'Moderate' ? 'gold' : 'green'}`}></span>
                          {patient.status}
                        </span>
                      </td>
                      <td>{patient.adherence}</td>
                      <td>{patient.sleep}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {activeTab === 'audit' && (
          <div className="clinical-panel fade-in">
            <div className="panel-header">
              <h3>WebCrypto Secure Log Ledger</h3>
              <span className="panel-header-action">Live System Logs</span>
            </div>
            
            <div className="registry-table-container">
              <table className="registry-table">
                <thead>
                  <tr>
                    <th>Timestamp</th>
                    <th>Audit Operation Event</th>
                    <th>Node Component</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {auditTrail.map((log, idx) => (
                    <tr key={idx}>
                      <td style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem' }}>{log.timestamp}</td>
                      <td style={{ fontFamily: 'var(--font-sans)', fontWeight: 500 }}>{log.event}</td>
                      <td style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>{log.node}</td>
                      <td>
                        <span className="severity-indicator" style={{ color: 'var(--success)' }}>
                          <span className="dot green"></span> {log.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default ClinicalDashboard;
