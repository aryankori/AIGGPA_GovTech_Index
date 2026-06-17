# Primary-Secondary E-Governance Integration Database

This database compiles primary survey findings (N=140) across three government departments in Madhya Pradesh (MP) - Forest (N=80), Rural Development (N=40), and Revenue (N=20) - and integrates them with secondary research findings covering e-governance infrastructure, capacity building, and department-specific platforms.

---

## 1. Executive Triangulation Matrix

The following matrix compares primary survey findings against verified secondary data sources, providing a cross-methodology view of digital adoption hurdles:

| Analytical Dimension | Survey Variable / Metric (N=140) | Secondary Source / Context | Integrated Policy Implication |
| :--- | :--- | :--- | :--- |
| **Connectivity & Network** | Internet Quality Mean: **3.21** / 5.0 (Reliability Alpha: **0.581**) | [Testbook Policy Report](https://testbook.com) highlights severe rural infrastructure gaps, forcing citizens to rely on private kiosk networks. | Rural block offices face a double burden: poor local connectivity combined with strict digital entry mandates. |
| **Capacity Building** | Training Quality Mean: **1.96** / 5.0 (Effectiveness Alpha: **0.787**) | [NeGD e-Daksha Directory](https://negd.gov.in) confirms IT training centers are centralized at district headquarters. | Access disparities exist; frontline staff in remote areas cannot easily travel to district centers for hands-on training. |
| **System Usability** | UI Friendliness Mean: **2.64** / 5.0 (Effort Expectancy Alpha: **0.896**) | [RCMS Support Logs](http://rcms.mp.gov.in) list frequent query timeout errors and portal downtime issues. | Frontline workers face a dual-documentation burden, maintaining physical registers to protect against system crashes. |

---

## 2. Quantitative Construct Reliability (Cronbach's Alpha)

Reliability testing establishes the internal consistency of the TAM and UTAUT constructs measured in the survey. Scores above 0.70 are considered acceptable:

| Construct | Master (N=140) | Forest (N=80) | Rural Development (N=40) | Revenue (N=20) |
| :--- | :---: | :---: | :---: | :---: |
| **Performance Expectancy (PE)** | **0.873** | **0.862** | **0.856** | **0.867** |
| **Effort Expectancy (EE)** | **0.896** | **0.904** | **0.849** | **0.902** |
| **Social Influence (SI)** | **0.856** | **0.857** | **0.882** | **0.752** |
| **Facilitating Conditions (FC)** | **0.581** | **0.571** | **0.621** | **0.403** |
| **Organisational Support** | **0.793** | **0.787** | **0.789** | **0.826** |
| **Training Effectiveness** | **0.787** | **0.791** | **0.8** | **0.651** |

---

## 3. Cadre-Wise Digital Divide Profile

Survey metrics show a distinct gap between high-level management (Class I & II) and frontline operational staff (Class III & IV) across the master cohort:

| Cadre Group | Sample Size (N) | Perceived Usefulness (PU) | Internet Score (FC) | Confidence (EE) | Difficulty Mean | Training Rate (%) | UI Satisfaction (EE) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Class I (Senior)** | 13 | 4.42 | 4.46 | 4.85 | 1.08 | 92% | 4 |
| **Class II (Mid-Level)** | 30 | 3.78 | 3.77 | 4.13 | 1.87 | 73% | 3.57 |
| **Class III (Field/Ops)** | 55 | 3.18 | 3.4 | 3.09 | 3.02 | 44% | 2.64 |
| **Class IV (Frontline)** | 42 | 2.07 | 2.17 | 1.57 | 4.52 | 7% | 1.55 |

---

## 4. Departmental Portals & Secondary Synthesis

### Revenue Department (N=20)
*   **Primary Findings:**
    *   MP Bhulekh/WebGIS Usability Mean: **2.8** / 5.0
    *   RCMS Usability Mean: **2.7** / 5.0
    *   SAMPADA 2.0 Usability Mean: **2.45** / 5.0
    *   Citizens Expect Digital Updates Mean: **3.25** / 5.0
*   **Secondary Synthesis:**
    *   Technical logs on the [RCMS Portal](http://rcms.mp.gov.in) point to frequent timeout errors during peak hours (11:00 AM to 3:00 PM), when revenue courts upload order sheets.
    *   The [MP Bhulekh](https://mpbhulekh.gov.in) land records portal requires multiple authentications for land mutation, which increases transaction times for Patwaris in District Offices.
    *   **State-Level Usability Comparison:** While MP Bhulekh remains an informational repository, Telangana's transition from the highly integrated but complex Dharani portal (33 modules) to the simplified, decentralized Bhu Bharati system (6 modules) shows that reducing module complexity and restoring local Tahsildar authority reduces backlogs.
    *   To resolve transaction failures, the state has established dedicated helpline and email support (help.rcms@gmail.com), though response latency remains a major administrative bottleneck.

### Rural Development Department (N=40)
*   **Primary Findings:**
    *   Multi-Portal Data Entry Burden Mean: **3.83** / 5.0
    *   Block/Gram Panchayat Internet Quality Mean: **2.83** / 5.0
    *   NMMS App Usability Mean: **2.3** / 5.0
*   **Secondary Synthesis:**
    *   The National Mobile Monitoring System (NMMS) requires twice-daily geotagged attendance of MGNREGA workers. Poor connectivity in remote Gram Panchayats blocks upload cycles, forcing frontline Panchayat Secretaries and Gram Rozgar Sahayaks (GRS) to travel to block headquarters simply to sync attendance records.
    *   Multi-portal entry requirements (e-Gram Swaraj, NREGASoft, PFMS) cause duplicate data entry, reducing administrative efficiency.

### Forest Department (N=80)
*   **Primary Findings:**
    *   AI-Based Forest Alert System Usability Mean: **3.21** / 5.0
    *   GIS / Remote Sensing Difficulty Mean: **2.79** / 5.0
*   **Secondary Synthesis:**
    *   Under the State Spatial Data Infrastructure (SSDI) managed by [MAP_IT](https://www.mapit.gov.in), GIS data layers are mapped for forest boundary verification. While Class I/II officers use these layers for planning, Class III/IV staff (e.g. Forest Guards) report high difficulty operating hand-held GPS units in dense canopy environments where satellite signals are weak.
    *   AI-based forest alert systems send notifications regarding fire spots and illegal logging, but field staff lack mobile data connectivity to respond to these alerts in real time.

### Health Department (Secondary-Only Policy Benchmark)
*   **Secondary Synthesis:**
    *   The digital ecosystem in health is led by **ANMOL MP** (ANM Online), which digitizes maternal and child health tracking.
    *   **Frontline Troubleshooting Friction:** Auxiliary Nurse Midwives (ANMs) face chronic synchronization errors, internet connectivity failure messages, and "Data Not Found" errors on tablets. Technical issues like "Village Not Mapped" require administrative backend changes by Block Officers, leaving field staff stranded without local troubleshooting options (official support contact: anmol.feedbackmp@gmail.com).
    *   Secondary research from the [National e-Governance Division](https://negd.gov.in) shows that ANMs face a dual-documentation burden. They must log data in physical registers during village visits, then re-enter the same records on tablets, leading to high administrative fatigue.
    *   Vaccine distribution is managed via the **eVIN** (Electronic Vaccine Intelligence Network) cold chain system. While eVIN has improved vaccine availability, sub-health centers in remote tribal blocks struggle with power outages and data-sync delays.

---

## 5. Capacity Building & Training Deficits
*   **Centralized Training Infrastructure:** Although regional training centers exist across district headquarters under the state's **e-Daksha** program, remote field staff (Class III/IV) report low training frequency.
*   **Curriculum Alignment & Best Practices:** e-Daksha programs primarily focus on emerging technologies (AR-VR, Cyber Security). According to public sector training studies by [Infosys Public Services](https://infosyspublicservices.com), the most effective frameworks rely on a **blended learning architecture** (combining instructor-led feedback with self-paced eLearning) and **microlearning** (5-10 minute video snippets and quick-reference guides) rather than generic computer literacy courses.
*   **Recommendations for Policy Action:**
    1.  *Decentralize training delivery:* Launch mobile IT training vans that visit block and tehsil offices, minimizing travel barriers for frontline staff.
    2.  *Reduce duplicate workflows:* Issue formal circulars to eliminate physical register backups once a digital portal is confirmed active.
    3.  *Establish local peer-support groups:* Designate and incentivize one digital mentor per block office to provide real-time tech support to colleagues, decreasing dependency on external helpdesks.
