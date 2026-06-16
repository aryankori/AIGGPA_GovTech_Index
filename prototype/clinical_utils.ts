/**
 * AETHER-CLINICAL // Secure Clinical Research Utilities
 * Helper functions for de-identification, psychometric scoring, and research exports.
 */

/**
 * 1. Cryptographic Anonymization Hashing Function
 * Generates an irreversible SHA-256 hash of a patient identifier combined with a local secure salt.
 * This ensures that identical participant IDs yield unique hashes across separate research sites.
 * Uses the WebCrypto API (available in standard browser contexts).
 */
export async function generateParticipantHash(patientId: string, siteSalt: string): Promise<string> {
  const encoder = new TextEncoder();
  // Combine the site-specific salt with the raw identifier to prevent dictionary attacks
  const data = encoder.encode(`${siteSalt}:${patientId.trim().toLowerCase()}`);
  
  // Calculate SHA-256 hash
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  
  // Convert ArrayBuffer to Hex String
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

/**
 * 2. PHQ-9 Clinical Scoring Utility
 * PHQ-9 consists of 9 items scored 0-3.
 * Total score ranges from 0 to 27.
 */
export type PHQ9Severity = 'Minimal' | 'Mild' | 'Moderate' | 'Moderately Severe' | 'Severe';

export interface PHQ9Result {
  score: number;
  severity: PHQ9Severity;
  colorCode: string; // CSS variables matching the design system
}

export function scorePHQ9(answers: number[]): PHQ9Result {
  if (answers.length !== 9) {
    throw new Error('PHQ-9 assessment requires exactly 9 responses.');
  }

  const score = answers.reduce((sum, current) => sum + Math.max(0, Math.min(3, current)), 0);
  
  let severity: PHQ9Severity = 'Minimal';
  let colorCode = 'var(--success)'; // Green

  if (score >= 20) {
    severity = 'Severe';
    colorCode = 'var(--danger)'; // Red
  } else if (score >= 15) {
    severity = 'Moderately Severe';
    colorCode = 'var(--danger)'; // Red-orange
  } else if (score >= 10) {
    severity = 'Moderate';
    colorCode = 'var(--accent)'; // Gold/Yellow
  } else if (score >= 5) {
    severity = 'Mild';
    colorCode = 'var(--primary)'; // Violet
  }

  return { score, severity, colorCode };
}

/**
 * 3. GAD-7 Clinical Scoring Utility
 * GAD-7 consists of 7 items scored 0-3.
 * Total score ranges from 0 to 21.
 */
export type GAD7Severity = 'Minimal' | 'Mild' | 'Moderate' | 'Severe';

export interface GAD7Result {
  score: number;
  severity: GAD7Severity;
  colorCode: string;
}

export function scoreGAD7(answers: number[]): GAD7Result {
  if (answers.length !== 7) {
    throw new Error('GAD-7 assessment requires exactly 7 responses.');
  }

  const score = answers.reduce((sum, current) => sum + Math.max(0, Math.min(3, current)), 0);
  
  let severity: GAD7Severity = 'Minimal';
  let colorCode = 'var(--success)';

  if (score >= 15) {
    severity = 'Severe';
    colorCode = 'var(--danger)';
  } else if (score >= 10) {
    severity = 'Moderate';
    colorCode = 'var(--accent)';
  } else if (score >= 5) {
    severity = 'Mild';
    colorCode = 'var(--primary)';
  }

  return { score, severity, colorCode };
}

/**
 * 4. Anonymous Clinical Research CSV Exporter
 * Converts an array of anonymized participant records into a clean CSV string
 * suitable for SPSS, R (read.csv), or Python (pandas.read_csv).
 * Removes any potential demographic leakage indicators.
 */
export interface AnonymizedExportRecord {
  participantHash: string;
  ageCohort: string;
  studyCohort: string;
  baselinePHQ9: number;
  baselineGAD7: number;
  activePHQ9: number;
  activeGAD7: number;
  adherencePercentage: number;
  sleepAverageHours: number;
}

export function exportClinicalCSV(records: AnonymizedExportRecord[]): string {
  const headers = [
    'participant_hash',
    'age_cohort',
    'study_cohort',
    'baseline_phq9',
    'baseline_gad7',
    'active_phq9',
    'active_gad7',
    'adherence_rate',
    'sleep_avg_hours'
  ];

  const csvRows = [headers.join(',')];

  for (const record of records) {
    const row = [
      `"${record.participantHash}"`,
      `"${record.ageCohort.replace(/"/g, '""')}"`,
      `"${record.studyCohort.replace(/"/g, '""')}"`,
      record.baselinePHQ9,
      record.baselineGAD7,
      record.activePHQ9,
      record.activeGAD7,
      record.adherencePercentage,
      record.sleepAverageHours
    ];
    csvRows.push(row.join(','));
  }

  return csvRows.join('\n');
}
