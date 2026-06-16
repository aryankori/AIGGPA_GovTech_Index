import React, { useState } from 'react';
import './ResearchDashboard.css';

const ResearchDashboard = () => {
  const [activeTab, setActiveTab] = useState('summary');

  const logFrameData = [
    { level: 'Goal', content: 'Institutional efficiency gains in MP through total digital adoption.', indicator: '>15% reduction in file time.' },
    { level: 'Purpose', content: 'Diagnose specific human/tech gaps in digital workflow adoption.', indicator: 'Approved roadmap for policy.' },
    { level: 'Outputs', content: 'Narrative datasets, Barrier frameworks, and Policy roadmap.', indicator: '45-60 balanced interviews.' },
    { level: 'Activities', content: 'Field visits, Semi-structured interviews, and Thematic Analysis.', indicator: '4-week schedule met.' },
  ];

  const insights = [
    { title: 'Delegated Digitization', text: 'Senior staff often outsource tech use to juniors, losing direct fluency.' },
    { title: 'The Transparency Fear', text: 'Digital trails reduce discretionary power, leading to subtle resistance.' },
    { title: 'Design-Reality Gap', text: 'HQ-designed software fails in rural block offices due to operational latency.' },
  ];

  return (
    <div className="dashboard-container">
      <nav className="side-nav">
        <div className="logo-section">
          <div className="logo-icon">A</div>
          <h1>AIGGPA</h1>
        </div>
        <button className={activeTab === 'summary' ? 'active' : ''} onClick={() => setActiveTab('summary')}>Summary</button>
        <button className={activeTab === 'logframe' ? 'active' : ''} onClick={() => setActiveTab('logframe')}>LogFrame</button>
        <button className={activeTab === 'insights' ? 'active' : ''} onClick={() => setActiveTab('insights')}>Insights</button>
        <button className="pitch-btn" onClick={() => setActiveTab('pitch')}>Pitch Mode</button>
      </nav>

      <main className="content-area">
        {activeTab === 'summary' && (
          <section className="fade-in">
            <header className="header">
              <h2>Project Overview</h2>
              <p>Digital Assessment of Government Employees in Madhya Pradesh</p>
            </header>
            <div className="stats-grid">
              <div className="stat-card">
                <h3>94%</h3>
                <p>Top-level Digitization</p>
              </div>
              <div className="stat-card gold">
                <h3>61%</h3>
                <p>Block-level Delay Risk</p>
              </div>
              <div className="stat-card">
                <h3>60</h3>
                <p>Target Participants</p>
              </div>
            </div>
            <div className="info-box">
              <h3>The Core Paradox</h3>
              <p>"Digitizing a bad process only makes it a faster bad process. We fix the process through the human user."</p>
            </div>
          </section>
        )}

        {activeTab === 'logframe' && (
          <section className="fade-in">
            <h2>The Logic Ladder</h2>
            <div className="ladder">
              {logFrameData.map((item, i) => (
                <div key={i} className="step">
                  <div className="step-count">{item.level}</div>
                  <div className="step-content">
                    <h4>{item.content}</h4>
                    <small>Metric: {item.indicator}</small>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {activeTab === 'insights' && (
          <section className="fade-in">
            <h2>Research Insights</h2>
            <div className="insights-grid">
              {insights.map((insight, i) => (
                <div key={i} className="insight-card">
                  <h4>{insight.title}</h4>
                  <p>{insight.text}</p>
                </div>
              ))}
            </div>
          </section>
        )}

        {activeTab === 'pitch' && (
          <section className="pitch-overlay h-full flex flex-col justify-center">
            <div className="pitch-content">
              <h1 className="giant-text">"Moving from <span className="highlight">Guesswork</span> to <span className="highlight">Framework</span>"</h1>
              <p className="sub-text">We aren't just looking at the computers; we are looking at the <strong>fingers on the keyboard</strong>.</p>
              <ul className="pitch-list">
                <li>Identify the "Shadow Work" (Paper backups)</li>
                <li>Fix the "Design-Reality Gap" (Rural vs HQ)</li>
                <li>Ensure the "1-Second Digital File" doesn't wait for a "10-Day Human Click"</li>
              </ul>
            </div>
          </section>
        )}
      </main>
    </div>
  );
};

export default ResearchDashboard;
