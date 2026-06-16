// ============================================================
// Tactile Workflows Sandbox — JS Logic
// AIGGPA Bhopal | Government Fieldwork Prototype
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    
    // --- State Variables ---
    let activeFileIndex = 0;
    let signatureDrawn = false;
    let canvas, ctx, isDrawing = false;
    let queueJobsCount = 0;
    
    // --- Mock Data ---
    const mockFiles = [
        {
            id: 'rev-0491',
            dept: 'Revenue',
            deptClass: 'revenue',
            title: 'File Rev/2026/0491 - Land Allocation Bhopal Bypass',
            reference: 'Ref: MP-BHU-2026-992-A',
            body: `
                <h3>REVENUE DEPARTMENT STATEMENT</h3>
                <p><strong>Subject:</strong> Allocation of 4.5 hectares of government revenue land for District Bypass Widening Project, Tehsil Huzur, Bhopal.</p>
                <p>Under Section 24A of the MP Land Revenue Code 1959, the land parcels listed below are proposed to be diverted from forest-buffer to infrastructure usage:</p>
                <ul>
                    <li>Khasra No. 122/4 — Area 1.2 Ha (Tehsil Huzur)</li>
                    <li>Khasra No. 125/1 — Area 3.3 Ha (Tehsil Huzur)</li>
                </ul>
                <p>The compensation evaluation of ₹14,200,000 has been verified by the Sub-Divisional Magistrate (SDM) and deposited in the treasury registry.</p>
                <p><strong>Action Requested:</strong> Approval of transfer deed and signing of authorization form.</p>
            `,
            audit: `
                <div class="audit-card pass">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                        Budget Verified
                    </div>
                    <p>Treasury verification code matches SDM record #TR-9982-A.</p>
                </div>
                <div class="audit-card pass">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                        Land Registry Clear
                    </div>
                    <p>No active disputes or claims on Khasra 122/4 or 125/1.</p>
                </div>
            `,
            signed: false
        },
        {
            id: 'rd-0088',
            dept: 'Development',
            deptClass: 'development',
            title: 'File RD/Panch/2026/088 - MGNREGA Road Sanction Betul',
            reference: 'Ref: PMAYG-BETUL-882',
            body: `
                <h3>PANCHAYAT & RURAL DEVELOPMENT</h3>
                <p><strong>Subject:</strong> Administrative approval for gravel road construction linking village Pathai to NH-47, District Betul.</p>
                <p>The project estimate totals ₹4,500,000 under MGNREGA scheme. Labor-material ratio is estimated at 60:40 in compliance with central guidelines.</p>
                <p>The Gram Sabha approved this resolution on March 14, 2026. The technical sanction was verified by Executive Engineer (EE).</p>
                <p><strong>Action Requested:</strong> Issuance of administrative sanction certificate.</p>
            `,
            audit: `
                <div class="audit-card pass">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                        Labor-Material Ratio Approved
                    </div>
                    <p>Ratio is 61.2:38.8, compliant with MGNREGA >=60% labor rules.</p>
                </div>
                <div class="audit-card warning">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/></svg>
                        Non-Standard Material Rates
                    </div>
                    <p>Cement rate quoted is 8.5% higher than district schedule of rates. This is flagged for review, but within Collector's emergency sanction authority.</p>
                </div>
            `,
            signed: false
        },
        {
            id: 'for-1102',
            dept: 'Forest',
            deptClass: 'forest',
            title: 'File For/CAMPA/2026/12 - Ranger Patrol Device Procurement',
            reference: 'Ref: FOR-CAMPA-1102',
            body: `
                <h3>FOREST DEPARTMENT MIS</h3>
                <p><strong>Subject:</strong> Technical sanction for procurement of 150 GPS-enabled smart patrol devices for Forest Guards under CAMPA funding.</p>
                <p>The technical committee recommended the ruggedized handheld systems with offline GIS support. Total procurement cost: ₹2,400,000.</p>
                <p>The devices will be deployed in Hoshangabad Division to track patrol paths and logs.</p>
                <p><strong>Action Requested:</strong> Procurement approval and financial release sign-off.</p>
            `,
            audit: `
                <div class="audit-card pass">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                        Funds Available
                    </div>
                    <p>CAMPA project code FOR-CMP-2026-BHOP has ₹5,200,000 unused allocation.</p>
                </div>
                <div class="audit-card pass">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                        Offline GIS Support Approved
                    </div>
                    <p>Complies with Forest IT policy section 8.4 regarding offline forest maps.</p>
                </div>
            `,
            signed: false
        },
        {
            id: 'hea-0331',
            dept: 'Health',
            deptClass: 'health',
            title: 'File Hea/HMIS/2026/331 - Vaccine Cold Chain Logistics',
            reference: 'Ref: HEA-eVIN-331',
            body: `
                <h3>PUBLIC HEALTH & FAMILY WELFARE</h3>
                <p><strong>Subject:</strong> Mobilisation approval for eVIN vaccine distribution vehicles, Bhopal Division.</p>
                <p>Allocation of ₹1,800,000 for emergency fuel and temperature-controlled logistics for immunization drives.</p>
                <p>Logistical plans have been reviewed by the Chief Medical & Health Officer (CMHO).</p>
                <p><strong>Action Requested:</strong> Emergency fund release signature.</p>
            `,
            audit: `
                <div class="audit-card pass">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                        Logistic Protocol Validated
                    </div>
                    <p>Cold chain logistics comply with WHO/UNICEF temperature monitoring guidelines.</p>
                </div>
                <div class="audit-card warning">
                    <div class="audit-card-title">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/></svg>
                        Fuel Cost Adjustment
                    </div>
                    <p>Proposed fuel rate exceeds regional average by ₹2.5/L due to special logistics surcharge. CMHO recommends approval to avoid delay.</p>
                </div>
            `,
            signed: false
        }
    ];

    // --- Dom Elements ---
    const tabBtns = document.querySelectorAll('.tab-btn');
    const panes = document.querySelectorAll('.sandbox-pane');
    
    // Tab switching
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            panes.forEach(p => p.classList.remove('active'));
            
            btn.classList.add('active');
            const targetTab = btn.getAttribute('data-tab');
            document.getElementById(`pane-${targetTab}`).classList.add('active');
            
            showToast(`Switched to: ${btn.textContent.trim()}`);
            
            if (targetTab === 'sign-slide') {
                initSignaturePad();
            }
        });
    });

    // ==========================================
    // OFFICER SIGN & SLIDE WORKFLOW LOGIC
    // ==========================================

    function initSignaturePad() {
        canvas = document.getElementById('sig-pad-canvas');
        if (!canvas) return;
        ctx = canvas.getContext('2d');
        ctx.strokeStyle = '#2C3E50';
        ctx.lineWidth = 3;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        
        signatureDrawn = false;
        document.getElementById('canvas-prompt').classList.remove('hidden');
        
        // Clear previous draw
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Drawing event listeners
        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mousemove', draw);
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mouseleave', stopDrawing);
        
        // Touch support
        canvas.addEventListener('touchstart', (e) => {
            const touch = e.touches[0];
            const rect = canvas.getBoundingClientRect();
            startDrawing({ clientX: touch.clientX, clientY: touch.clientY });
            e.preventDefault();
        });
        canvas.addEventListener('touchmove', (e) => {
            const touch = e.touches[0];
            draw({ clientX: touch.clientX, clientY: touch.clientY });
            e.preventDefault();
        });
        canvas.addEventListener('touchend', stopDrawing);
    }

    function startDrawing(e) {
        isDrawing = true;
        document.getElementById('canvas-prompt').classList.add('hidden');
        const coords = getCanvasCoords(e);
        ctx.beginPath();
        ctx.moveTo(coords.x, coords.y);
    }

    function draw(e) {
        if (!isDrawing) return;
        const coords = getCanvasCoords(e);
        ctx.lineTo(coords.x, coords.y);
        ctx.stroke();
        signatureDrawn = true;
    }

    function stopDrawing() {
        isDrawing = false;
    }

    function getCanvasCoords(e) {
        const rect = canvas.getBoundingClientRect();
        // Scale coordinate based on canvas CSS size vs canvas backing store
        const x = (e.clientX - rect.left) * (canvas.width / rect.width);
        const y = (e.clientY - rect.top) * (canvas.height / rect.height);
        return { x, y };
    }

    // Clear signature canvas
    document.getElementById('btn-clear-sig').addEventListener('click', (e) => {
        e.stopPropagation();
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        signatureDrawn = false;
        document.getElementById('canvas-prompt').classList.remove('hidden');
    });

    // Populate Sidebar Document Queue
    function renderQueue() {
        const queueList = document.getElementById('doc-queue-list');
        queueList.innerHTML = '';
        
        let pending = 0;
        mockFiles.forEach((file, index) => {
            if (!file.signed) pending++;
            
            const item = document.createElement('div');
            item.className = `queue-item ${index === activeFileIndex ? 'active' : ''} ${file.signed ? 'signed' : ''}`;
            item.innerHTML = `
                <div class="queue-item-header">
                    <span class="queue-dept">${file.dept}</span>
                    <span class="queue-time">${10 + index} mins ago</span>
                </div>
                <div class="queue-title">${file.title}</div>
                <div class="queue-snippet">Ref ID: ${file.id.toUpperCase()} • Actions pending review</div>
            `;
            
            item.addEventListener('click', () => {
                activeFileIndex = index;
                loadActiveFile();
            });
            
            queueList.appendChild(item);
        });
        
        document.getElementById('pending-count').textContent = `${pending} Pending`;
    }

    // Load Active File
    function loadActiveFile() {
        const file = mockFiles[activeFileIndex];
        if (!file) return;
        
        // Reset Stamp
        const stamp = document.getElementById('digital-seal-stamp');
        stamp.classList.remove('active');
        
        // Update tags and titles
        const deptTag = document.getElementById('active-dept');
        deptTag.className = `department-tag ${file.deptClass}`;
        deptTag.textContent = file.dept;
        
        document.getElementById('active-file-title').textContent = file.title;
        document.getElementById('paper-ref').textContent = file.reference;
        document.getElementById('paper-body-text').innerHTML = file.body;
        document.getElementById('active-audit-content').innerHTML = file.audit;
        
        // Update stamp text
        document.getElementById('seal-officer-name').textContent = "COLLECTOR BHOPAL";
        document.getElementById('seal-timestamp').textContent = new Date().toISOString().split('T')[0];
        
        // If already signed, show stamp
        if (file.signed) {
            stamp.classList.add('active');
        }
        
        // Re-render sidebar queue list highlight
        const items = document.querySelectorAll('.doc-queue .queue-item');
        items.forEach((item, idx) => {
            item.classList.remove('active');
            if (idx === activeFileIndex) item.classList.add('active');
        });
        
        // Reset drawing pad
        initSignaturePad();
    }

    // Trigger Sign Action
    function signCurrentFile() {
        const file = mockFiles[activeFileIndex];
        if (!file || file.signed) return;
        
        // Trigger stamp animation on the paper sheet
        const stamp = document.getElementById('digital-seal-stamp');
        stamp.classList.add('active');
        
        // Mark as signed
        file.signed = true;
        
        // Launch Background Asynchronous Job
        triggerAsyncCryptographicJob(file);
        
        // Re-render sidebar state
        renderQueue();
        
        showToast(`Signed ${file.id.toUpperCase()} successfully.`);
        
        // Slide out sheet and load next file
        setTimeout(() => {
            slideOutAndNext();
        }, 800);
    }

    // Skip current file
    function skipCurrentFile() {
        showToast("Skipped file.");
        slideOutAndNext();
    }

    function slideOutAndNext() {
        const paperSheet = document.getElementById('active-paper-sheet');
        paperSheet.classList.add('slide-out-left');
        
        // Find next unsigned file index (looping back)
        setTimeout(() => {
            let nextIndex = activeFileIndex;
            let found = false;
            
            // Loop through files to find next unsigned
            for (let i = 1; i <= mockFiles.length; i++) {
                let checkIdx = (activeFileIndex + i) % mockFiles.length;
                if (!mockFiles[checkIdx].signed) {
                    nextIndex = checkIdx;
                    found = true;
                    break;
                }
            }
            
            // If all signed, just move to next index anyway
            if (!found) {
                nextIndex = (activeFileIndex + 1) % mockFiles.length;
            }
            
            activeFileIndex = nextIndex;
            
            // Load file content
            loadActiveFile();
            
            // Slide in new document
            paperSheet.classList.remove('slide-out-left');
            paperSheet.classList.add('slide-in-right');
            
            setTimeout(() => {
                paperSheet.classList.remove('slide-in-right');
            }, 600);
            
        }, 500);
    }

    // Asynchronous Cryptographic Job Simulator
    function triggerAsyncCryptographicJob(file) {
        const jobsList = document.getElementById('async-jobs-list');
        
        // Remove empty jobs placeholder
        const emptyPlacer = jobsList.querySelector('.empty-jobs');
        if (emptyPlacer) emptyPlacer.remove();
        
        const jobId = `job-${Math.floor(Math.random() * 10000)}`;
        const jobItem = document.createElement('div');
        jobItem.className = 'job-item';
        jobItem.id = jobId;
        jobItem.innerHTML = `
            <div class="job-info">
                <span class="job-filename">${file.id.toUpperCase()} Approval Ledger</span>
                <span class="job-status hashing">Hashing...</span>
            </div>
            <div class="job-progress-bar">
                <div class="job-progress-fill" style="width: 15%"></div>
            </div>
        `;
        
        // Add to list
        jobsList.insertBefore(jobItem, jobsList.firstChild);
        
        // Toggle Queue status dot to active
        const dot = document.getElementById('queue-status-dot');
        dot.className = 'pulse-dot processing';
        
        // Run progression states
        let progress = 15;
        const fill = jobItem.querySelector('.job-progress-fill');
        const statusSpan = jobItem.querySelector('.job-status');
        
        const interval = setInterval(() => {
            progress += Math.floor(Math.random() * 20) + 10;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
                fill.style.width = '100%';
                fill.classList.add('done');
                statusSpan.textContent = 'NIC Upload Complete';
                statusSpan.className = 'job-status done';
                
                // Show completed toast
                showToast(`Async job completed: PKCS#7 Seal attached to ${file.id.toUpperCase()}`);
                
                // Check if other jobs are active
                setTimeout(() => {
                    const activeJobs = jobsList.querySelectorAll('.job-status:not(.done)');
                    if (activeJobs.length === 0) {
                        dot.className = 'pulse-dot idle';
                    }
                }, 1000);
                
            } else {
                fill.style.width = `${progress}%`;
                if (progress > 75) {
                    statusSpan.textContent = 'Cryptographic Signing...';
                    statusSpan.className = 'job-status signing';
                } else if (progress > 45) {
                    statusSpan.textContent = 'Attaching Certificate...';
                    statusSpan.className = 'job-status signing';
                }
            }
        }, 600);
    }

    // Biometric Button Hold to Sign
    const fpBtn = document.getElementById('btn-biometric-sign');
    let fpTimeout;
    
    fpBtn.addEventListener('mousedown', startBiometricSign);
    fpBtn.addEventListener('touchstart', (e) => {
        startBiometricSign();
        e.preventDefault();
    });
    
    fpBtn.addEventListener('mouseup', cancelBiometricSign);
    fpBtn.addEventListener('mouseleave', cancelBiometricSign);
    fpBtn.addEventListener('touchend', cancelBiometricSign);
    
    function startBiometricSign() {
        const sensorLight = fpBtn.querySelector('.sensor-light');
        sensorLight.style.background = '#FFC107'; // Yellow scanning
        
        fpBtn.style.transform = 'scale(0.97)';
        
        fpTimeout = setTimeout(() => {
            sensorLight.style.background = '#27AE60'; // Green success
            fpBtn.style.transform = '';
            signCurrentFile();
        }, 1000); // 1-second hold
    }
    
    function cancelBiometricSign() {
        clearTimeout(fpTimeout);
        const sensorLight = fpBtn.querySelector('.sensor-light');
        sensorLight.style.background = '#27AE60';
        fpBtn.style.transform = '';
    }

    document.getElementById('btn-skip').addEventListener('click', skipCurrentFile);

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
        // Only trigger if in sign-slide tab
        const activeTab = document.querySelector('.tab-btn.active').getAttribute('data-tab');
        if (activeTab !== 'sign-slide') return;
        
        if (e.key.toLowerCase() === 's') {
            signCurrentFile();
        } else if (e.key.toLowerCase() === 'd') {
            skipCurrentFile();
        }
    });

    // ==========================================
    // ALTMAN TORN NOTE CANVAS LOGIC
    // ==========================================

    const workbench = document.getElementById('canvas-viewport');
    let draggedElement = null;
    let offsetX = 0, offsetY = 0;
    
    // Wire Notebook Sidebar Tear Buttons
    const notebookItems = document.querySelectorAll('.spiral-page-item');
    notebookItems.forEach(item => {
        const tearBtn = item.querySelector('.tear-btn');
        tearBtn.addEventListener('click', () => {
            const noteId = item.getAttribute('data-note-id');
            const title = item.querySelector('.note-title').textContent;
            const text = item.querySelector('.note-snippet').textContent;
            const tag = item.querySelector('.note-tag').textContent;
            const tagClass = item.querySelector('.note-tag').className.split(' ')[1];
            
            spawnDraggableNote(noteId, title, text, tag, tagClass);
            
            // Disable page item visual to show it's torn out
            item.style.opacity = '0.3';
            item.style.pointerEvents = 'none';
            tearBtn.textContent = 'Torn Out';
        });
    });

    // Spawn Draggable Note Sheet on Canvas
    function spawnDraggableNote(id, title, text, tag, tagClass) {
        const note = document.createElement('div');
        note.className = 'draggable-note-sheet';
        note.id = `canvas-${id}`;
        
        // Random placement near center
        const rect = workbench.getBoundingClientRect();
        const randX = Math.floor(Math.random() * (rect.width - 250)) + 30;
        const randY = Math.floor(Math.random() * (rect.height - 300)) + 50;
        
        note.style.left = `${randX}px`;
        note.style.top = `${randY}px`;
        // Small random rotation to look scattered
        const randRot = Math.floor(Math.random() * 12) - 6;
        note.style.transform = `rotate(${randRot}deg)`;
        
        note.innerHTML = `
            <div class="note-sheet-header">
                <span class="note-tag ${tagClass}">${tag}</span>
                <button class="close-note-btn">×</button>
            </div>
            <div class="note-sheet-body">
                <h4 style="font-size:0.8rem; font-weight:800; margin-bottom:6px; color:#2C3E50;">${title}</h4>
                <p>${text}</p>
            </div>
        `;
        
        // Drag events
        note.addEventListener('mousedown', dragStart);
        
        // Touch Drag support
        note.addEventListener('touchstart', (e) => {
            const touch = e.touches[0];
            dragStart({
                target: note,
                clientX: touch.clientX,
                clientY: touch.clientY,
                preventDefault: () => e.preventDefault()
            });
        });
        
        // Double-click to toggle zoom
        note.addEventListener('dblclick', () => {
            note.classList.toggle('zoomed');
            showToast(note.classList.contains('zoomed') ? "Zoomed In on note." : "Zoomed Out.");
        });
        
        // Close Button (Crumple Discard)
        const closeBtn = note.querySelector('.close-note-btn');
        closeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            note.classList.add('crumple-discard');
            showToast("Crumpled and discarded note!");
            
            setTimeout(() => {
                note.remove();
                // Re-enable notebook items in sidebar
                const originalPage = document.querySelector(`.spiral-page-item[data-note-id="${id}"]`);
                if (originalPage) {
                    originalPage.style.opacity = '1';
                    originalPage.style.pointerEvents = 'all';
                    originalPage.querySelector('.tear-btn').textContent = 'Tear Out';
                }
            }, 500);
        });
        
        workbench.appendChild(note);
        showToast(`Tore out: ${title.split('. ')[1]}`);
    }

    // Drag Core Mechanics
    function dragStart(e) {
        // Bring to front
        const activeNotes = document.querySelectorAll('.draggable-note-sheet');
        activeNotes.forEach(n => n.style.zIndex = '5');
        
        draggedElement = e.target.closest('.draggable-note-sheet');
        draggedElement.style.zIndex = '50';
        
        const rect = draggedElement.getBoundingClientRect();
        offsetX = e.clientX - rect.left;
        offsetY = e.clientY - rect.top;
        
        document.addEventListener('mousemove', dragMove);
        document.addEventListener('mouseup', dragEnd);
        
        document.addEventListener('touchmove', touchDragMove, { passive: false });
        document.addEventListener('touchend', dragEnd);
    }

    function dragMove(e) {
        if (!draggedElement) return;
        const rect = workbench.getBoundingClientRect();
        let newX = e.clientX - rect.left - offsetX;
        let newY = e.clientY - rect.top - offsetY;
        
        // Constrain to workspace
        newX = Math.max(0, Math.min(newX, rect.width - draggedElement.offsetWidth));
        newY = Math.max(0, Math.min(newY, rect.height - draggedElement.offsetHeight));
        
        draggedElement.style.left = `${newX}px`;
        draggedElement.style.top = `${newY}px`;
    }

    function touchDragMove(e) {
        if (!draggedElement) return;
        const touch = e.touches[0];
        dragMove({
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        e.preventDefault(); // Stop scrolling while dragging
    }

    function dragEnd() {
        draggedElement = null;
        document.removeEventListener('mousemove', dragMove);
        document.removeEventListener('mouseup', dragEnd);
        document.removeEventListener('touchmove', touchDragMove);
        document.removeEventListener('touchend', dragEnd);
    }

    // Workbench Buttons
    document.getElementById('btn-clear-canvas').addEventListener('click', () => {
        const spawnedNotes = document.querySelectorAll('.draggable-note-sheet');
        spawnedNotes.forEach(n => {
            n.classList.add('crumple-discard');
        });
        
        setTimeout(() => {
            spawnedNotes.forEach(n => n.remove());
            // Restore all notebook sidebar items
            notebookItems.forEach(item => {
                item.style.opacity = '1';
                item.style.pointerEvents = 'all';
                item.querySelector('.tear-btn').textContent = 'Tear Out';
            });
            showToast("Workspace cleared.");
        }, 500);
    });

    document.getElementById('btn-reset-layout').addEventListener('click', () => {
        const spawnedNotes = document.querySelectorAll('.draggable-note-sheet');
        if (spawnedNotes.length === 0) return;
        
        spawnedNotes.forEach((note, index) => {
            note.classList.remove('zoomed');
            // Arrange in a clean row/grid
            const col = index % 3;
            const row = Math.floor(index / 3);
            note.style.left = `${30 + col * 230}px`;
            note.style.top = `${100 + row * 280}px`;
            note.style.transform = `rotate(0deg)`;
        });
        
        showToast("Arranged notes cleanly.");
    });

    // ==========================================
    // TOAST ALERTS HELPER
    // ==========================================
    let toastTimeout;
    function showToast(text) {
        const toast = document.getElementById('instructions-toast');
        const content = document.getElementById('instructions-text');
        
        content.textContent = text;
        toast.classList.add('show');
        
        clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }

    // --- Boot Initialisation ---
    renderQueue();
    loadActiveFile();
    initSignaturePad();
});
