const { execFileSync, execSync } = require('child_process');

const GOG = 'C:\\Users\\aryan\\.gemini\\antigravity\\bin\\gog.exe';
const ACCOUNT = "aryan.kori14@gmail.com";

function runGog(args, retries=3) {
    const fullArgs = ["--no-input", "--account", ACCOUNT, ...args];
    
    for (let i = 0; i < retries; i++) {
        try {
            const out = execFileSync(GOG, fullArgs, { encoding: 'utf-8' });
            return out;
        } catch (e) {
            console.error(`Attempt ${i+1} failed: ${e.stderr ? e.stderr : e.message}`);
            if (i === retries - 1) return null;
            execSync("powershell -command Start-Sleep -Seconds 2");
        }
    }
}

const title = "AIGGPA Final Fieldwork Questionnaire";
console.log(`Creating form: ${title}`);
const out = runGog(["forms", "create", "--title", title, "--json"]);
if (!out) {
    console.error("Failed to create form");
    process.exit(1);
}

const formId = JSON.parse(out).form.formId;
console.log("Created Form ID:", formId);

function section(num, titleEn, titleHi) {
    // Add section header as a text question, because Forms CLI lacks "add-section"
    // runGog(["forms", "add-question", formId, "--title", `--- SECTION ${num}: ${titleEn} ---`, "--type", "text"]);
    // execSync("powershell -command Start-Sleep -Milliseconds 800");
    return []; 
}

function q(questionText, typeHint, options) {
    let gtype = "text";
    if (typeHint === "short") gtype = "text";
    if (typeHint === "para") gtype = "paragraph";
    if (typeHint === "radio") gtype = "radio";
    if (typeHint === "scale") gtype = "scale";

    const args = ["forms", "add-question", formId, "--title", questionText, "--type", gtype];
    if (options && typeHint === "radio") {
        options.split('|').forEach(opt => {
            args.push("-o");
            args.push(opt.trim());
        });
    }
    
    process.stdout.write(`Adding: ${questionText.substring(0, 40)}... `);
    const res = runGog(args);
    if(res) console.log("OK"); else console.log("FAIL");
    
    execSync("powershell -command Start-Sleep -Milliseconds 1200");
    return [];
}

function qCheck(questionText, options) {
    const args = ["forms", "add-question", formId, "--title", questionText, "--type", "checkbox"];
    options.split('|').forEach(opt => {
        args.push("-o");
        args.push(opt.trim());
    });
    
    process.stdout.write(`Adding Checkbox: ${questionText.substring(0, 40)}... `);
    const res = runGog(args);
    if(res) console.log("OK"); else console.log("FAIL");
    
    execSync("powershell -command Start-Sleep -Milliseconds 1200");
    return [];
}

// ─── All questions from build_aiggpa.js ────────────────────────────────────────────────────────────
const children = [
  // ── SECTION 1: Personal Information ────────────────────────────────────────
  ...section(1, 'Personal Information', 'व्यक्तिगत जानकारी'),
  ...q('Name / नाम', 'short'),
  ...q('Designation / Post: / पदनाम / पद:', 'short'),
  ...q('Mobile Number / मोबाइल नंबर', 'short'),
  ...q('Email Address / ईमेल पता', 'short'),
  ...q('Job Role / Level: / कार्य भूमिका / स्तर:', 'short'),
  ...q('Age group: / आयु वर्ग:', 'radio', 'Below 30 | 30–45 | 46–60'),
  ...q('Gender: / लिंग:', 'radio', 'Male | Female | Other'),
  ...q('Years of service: / सेवा के वर्ष:', 'radio', '0–5 | 6–10 | 11–20 | 21+'),
  ...q('Highest education: / उच्चतम शिक्षा:', 'radio', 'Up to 12th | Grad | PG | Prof'),

  // ── SECTION 2: Opinion & Attitude ──────────────────────────────────────────
  ...section(2, 'Opinion & Attitude on Digital Tools', 'डिजिटल उपकरणों पर राय'),
  ...q('Do you think government employees should adopt digital tools in their daily work? / क्या आप मानते हैं कि सरकारी कर्मचारियों को अपने दैनिक कार्य में डिजिटल उपकरण अपनाने चाहिए?', 'radio', 'Yes - strongly agree | Yes - somewhat | Neutral | No - not necessary | No - not suitable'),
  ...q('Digital tools help me complete tasks faster than paper. / डिजिटल उपकरण मुझे कागज़ की तुलना में कार्य तेज़ी से पूरा करने में मदद करते हैं।', 'scale'),
  ...q('Digital tools improve the quality/accuracy of my work. / डिजिटल उपकरण मेरे काम की गुणवत्ता/सटीकता में सुधार करते हैं।', 'scale'),
  ...q('Using digital tools increases my overall productivity. / डिजिटल उपकरणों का उपयोग मेरी समग्र उत्पादकता बढ़ाता है।', 'scale'),
  ...q('The digital tools available are well-suited to my actual job tasks. / उपलब्ध डिजिटल उपकरण मेरे वास्तविक कार्यों के लिए उपयुक्त हैं।', 'scale'),
  ...q('How difficult do you find digital tools to use? / डिजिटल उपकरणों का उपयोग आपको कितना कठिन लगता है?', 'scale'),
  ...q('I am confident in my ability to use digital tools for my work. / मुझे डिजिटल उपकरण उपयोग करने की अपनी क्षमता पर विश्वास है।', 'scale'),
  ...q('My superiors encourage the use of digital tools. / मेरे वरिष्ठ अधिकारी डिजिटल उपकरणों के उपयोग को प्रोत्साहित करते हैं।', 'scale'),
  ...q('My colleagues regularly use digital tools in their work. / मेरे सहकर्मी नियमित रूप से डिजिटल उपकरणों का उपयोग करते हैं।', 'scale'),
  ...q('There is a formal mandate/order requiring digital tool use in my department. / मेरे विभाग में डिजिटल उपकरण के लिए औपचारिक आदेश है।', 'radio', "Yes | No | Don't know"),

  // ── SECTION 3: IT Infrastructure ───────────────────────────────────────────
  ...section(3, 'IT Infrastructure & Connectivity', 'आईटी इंफ्रास्ट्रक्चर और कनेक्टिविटी'),
  ...qCheck('What digital devices are available at your workstation? / आपके कार्यस्थल पर कौन-से डिजिटल उपकरण उपलब्ध हैं?', 'Desktop | Laptop | Tablet | Phone | None'),
  ...q('Do you share your device with other employees? / क्या आप अपना उपकरण अन्य कर्मचारियों के साथ साझा करते हैं?', 'radio', 'Yes – always | Sometimes | No – dedicated'),
  ...q('Rate internet connectivity at your office: / अपने कार्यालय में इंटरनेट कनेक्टिविटी का मूल्यांकन करें:', 'scale'),
  ...q('How often do you experience internet outages per week? / सप्ताह में कितनी बार इंटरनेट बंद होता है?', 'radio', 'Never | 1–2 times | 3–5 times | Daily'),
  ...q('Is IT helpdesk / technical support available? / क्या IT हेल्पडेस्क / तकनीकी सहायता उपलब्ध है?', 'radio', 'Yes | No'),
  ...q('If yes, how quickly are issues resolved? / यदि हाँ, तो समस्याएँ कितनी जल्दी हल होती हैं?', 'radio', 'Same day | 2–3 days | 1 week+ | Never resolved'),

  // ── SECTION 4: General Usage ────────────────────────────────────────────────
  ...section(4, 'General Digital Tool Usage', 'सामान्य डिजिटल उपकरण उपयोग'),
  ...q('How often do you use digital tools for work? / आप कितनी बार काम के लिए डिजिटल उपकरणों का उपयोग करते हैं?', 'radio', 'Daily | Weekly | Monthly | Rarely | Never'),
  ...q('What percentage of your work is done digitally? / आपके कार्य का कितना प्रतिशत डिजिटल रूप से होता है?', 'radio', '0–20% | 21–40% | 41–60% | 61–80% | 81–100%'),
  ...q('Learning to use a new portal/app takes me: / एक नया पोर्टल/ऐप सीखने में मुझे लगता है:', 'radio', 'Less than 1 day | A few days | 1–2 weeks | More than 2 weeks'),
  ...q('The design/interface of most government portals is user-friendly. / अधिकांश सरकारी पोर्टलों का डिज़ाइन उपयोगकर्ता-अनुकूल है।', 'scale'),
  ...qCheck('Which general tools are you aware of? / आप किन सामान्य उपकरणों से अवगत हैं?', 'e-Office | CM Helpline | PFMS | SPARROW | iGOT | MP eDistrict'),
  ...q('Primary interaction with digital tools: / डिजिटल उपकरणों के साथ आपकी प्राथमिक भूमिका:', 'radio', "Data entry | Review/approve | Field verification | Don't use | Other"),
  ...q('Is there one person who does most portal work for others? / क्या कोई एक व्यक्ति दूसरों का पोर्टल कार्य करता है?', 'radio', 'Yes – one person | A few share | Everyone does own | N/A'),
  ...q('Do senior officers use digital tools themselves? / क्या वरिष्ठ अधिकारी स्वयं डिजिटल उपकरण उपयोग करते हैं?', 'radio', "Yes | Rely on subordinates | Mixed | Don't know"),
  ...q('Have digital tools changed the work expected at your level? / क्या डिजिटल उपकरणों ने आपके स्तर पर अपेक्षित कार्य बदला है?', 'scale'),
  ...q('When a portal gives an error, what do you do? / जब पोर्टल त्रुटि देता है, तो आप क्या करते हैं?', 'radio', 'Wait for IT | Ask colleague | Use paper | Fix myself | Tell supervisor | Abandon'),

  // ── SECTION 5: Other Digital Tools (CENTERPIECE) ───────────────────────────
  ...section(5, 'Other Digital Tools Used at Work', 'कार्य में उपयोग किए जाने वाले अन्य डिजिटल उपकरण'),
  ...q('Do you use any non-government apps or tools to help with your work? / क्या आप अपने काम में कोई गैर-सरकारी ऐप्स या उपकरण उपयोग करते हैं?', 'radio', 'Yes | No'),
  ...qCheck('Which of these do you use for work-related tasks? (tick all) / इनमें से कौन-से आप कार्य के लिए उपयोग करते हैं?', 'WhatsApp | Google Docs / Drive | ChatGPT / AI tools | YouTube | Personal email | MS Office | Google Translate | Other'),
  ...qCheck('What do you mainly use these tools for? (tick all) / आप इन उपकरणों का मुख्य रूप से किसलिए उपयोग करते हैं?', 'Drafting documents | Translating | Coordinating with team | Learning portals | Backup / storage | Sharing files | Other'),
  ...q('How often do you use these personal tools for official work? / आप कितनी बार इन व्यक्तिगत उपकरणों का आधिकारिक काम के लिए उपयोग करते हैं?', 'radio', 'Daily | A few times a week | Occasionally | Rarely | Never'),
  ...q("Do you feel these tools fill a gap that government systems don't cover? / क्या ये उपकरण सरकारी प्रणालियों की कमी पूरी करते हैं?", 'scale'),
  ...q('Any concerns about using personal tools for official work? / व्यक्तिगत उपकरणों के आधिकारिक उपयोग में कोई चिंता?', 'para'),

  // ── SECTION 6: Barriers & Challenges ───────────────────────────────────────
  ...section(6, 'Barriers & Challenges', 'बाधाएँ और चुनौतियाँ'),
  ...qCheck('What issues do you face? (tick all) / आपको क्या समस्याएँ आती हैं?', 'Slow internet | System crashes | No dedicated device | Complex UI | No training provided | No support available | Power cuts'),
  ...q('How often do digital issues disrupt your work? / डिजिटल समस्याएँ कितनी बार आपके काम में बाधा डालती हैं?', 'radio', 'Daily | Weekly | Monthly | Rarely | Never'),

  // ── SECTION 7: Training & Support ──────────────────────────────────────────
  ...section(7, 'Training & Support Needs', 'प्रशिक्षण और सहायता आवश्यकताएँ'),
  ...q('Have you attended any digital skills training in the last 2 years? / क्या पिछले 2 वर्षों में आपने कोई डिजिटल कौशल प्रशिक्षण लिया है?', 'radio', 'Yes | No'),
  ...q('If yes, how many training sessions? / यदि हाँ, तो कितने प्रशिक्षण सत्र?', 'radio', '1 | 2–3 | 4–5 | More than 5'),
  ...q('Rate the quality of training received: / प्राप्त प्रशिक्षण की गुणवत्ता का मूल्यांकन करें:', 'scale'),
  ...q('Was the training sufficient for your actual job needs? / क्या प्रशिक्षण आपकी वास्तविक कार्य आवश्यकताओं के लिए पर्याप्त था?', 'scale'),
  ...q('What topics need more training? / किन विषयों में अधिक प्रशिक्षण चाहिए?', 'para'),
  ...q('Is the training appropriate for your specific job role? / क्या प्रशिक्षण आपकी विशिष्ट भूमिका के लिए उपयुक्त है?', 'scale'),
  ...q('Are there digital tasks beyond your current skill level? / क्या कोई डिजिटल कार्य आपके कौशल स्तर से परे हैं?', 'radio', 'Yes | No'),
  ...q('Should training differ based on job level? / क्या प्रशिक्षण पद स्तर के अनुसार अलग होना चाहिए?', 'radio', 'Yes | Somewhat | No'),
  ...q('I feel comfortable asking for help with digital tools. / मुझे डिजिटल उपकरणों के लिए सहायता माँगने में सहजता है।', 'scale'),
  ...q('My organisation provides adequate support for digital tools. / मेरा संगठन डिजिटल उपकरणों के लिए पर्याप्त सहायता प्रदान करता है।', 'scale'),
  ...q('My department is committed to digital transformation. / मेरा विभाग डिजिटल परिवर्तन के प्रति प्रतिबद्ध है।', 'scale'),
  ...q('Rank these priorities (1=highest, 5=lowest): / इन प्राथमिकताओं को क्रम दें (1=सर्वोच्च, 5=न्यूनतम):', 'para'),
  ...q('What one change would most improve your use of digital tools? / कौन-सा बदलाव आपके डिजिटल उपकरण उपयोग में सबसे अधिक सुधार करेगा?', 'para'),
  ...q("Has digital tool adoption improved service delivery to citizens? / क्या डिजिटल उपकरणों से नागरिकों को सेवा वितरण में सुधार हुआ है?", 'radio', "Yes – significantly | Somewhat | No change | Worsened | Can't say"),

  // ── SECTION 8: Revenue Department ──────────────────────────────────────────
  ...section(8, 'Revenue Department Tools', 'राजस्व विभाग के उपकरण'),
  ...qCheck('[Revenue] Which Revenue digital tools are you aware of? / राजस्व विभाग के कौन-से डिजिटल उपकरणों से आप अवगत हैं?', 'Bhulekh / WebGIS | RCMS | SAARA | SAMPADA | e-Court | None of the above'),
  ...q('[Revenue] Has Bhulekh/WebGIS improved speed and accuracy of land record verification? / क्या भूलेख/WebGIS ने भूमि अभिलेख सत्यापन की गति और सटीकता में सुधार किया है?', 'scale'),
  ...q('[Revenue] How difficult is RCMS to use for tracking revenue cases? / राजस्व मामलों की ट्रैकिंग के लिए RCMS का उपयोग कितना कठिन है?', 'scale'),
  ...q('[Revenue] What percentage of land records still need physical paper files? / भूमि अभिलेखों का कितना प्रतिशत अभी भी कागज़ी फाइलों की ज़रूरत है?', 'radio', '0–20% | 21–40% | 41–60% | 61–80% | 81–100%'),
  ...q('[Revenue] How often do citizens visit expecting services through digital tools? / नागरिक कितनी बार डिजिटल सेवाओं की अपेक्षा से आते हैं?', 'scale'),
  ...q('[Revenue] When you process a mutation case, which steps are digital and which on paper? / दाखिल-खारिज प्रक्रिया में कौन-से चरण डिजिटल और कौन-से कागज़ पर हैं?', 'para'),
  ...q('[Revenue] Has SAMPADA 2.0 reduced property registration time? / क्या SAMPADA 2.0 ने संपत्ति पंजीकरण का समय कम किया है?', 'scale'),

  // ── SECTION 9: Rural Development ───────────────────────────────────────────
  ...section(9, 'Rural Development Tools', 'ग्रामीण विकास उपकरण'),
  ...qCheck('[Rural Dev] Which Rural Development tools are you aware of? / ग्रामीण विकास के कौन-से उपकरणों से आप अवगत हैं?', 'NREGASoft / NMMS | e-Gram Swaraj | PMAY-G | SBM-G | Panchayat Darpan | PFMS | None of the above'),
  ...q('[Rural Dev] How difficult is managing multiple portals at the same time? / एक साथ कई पोर्टलों का प्रबंधन कितना कठिन है?', 'scale'),
  ...q('[Rural Dev] Rate internet connectivity at block/panchayat offices: / ब्लॉक/पंचायत कार्यालयों में इंटरनेट कनेक्टिविटी का मूल्यांकन करें:', 'scale'),
  ...q('[Rural Dev] Has the NMMS app improved accuracy of MGNREGA attendance? / क्या NMMS ऐप ने मनरेगा उपस्थिति की सटीकता में सुधार किया है?', 'scale'),
  ...q('[Rural Dev] How much of your working day is spent entering data into portals? / आपके कार्यदिवस का कितना समय पोर्टलों में डेटा दर्ज करने में लगता है?', 'radio', 'Less than 1 hr | 1–2 hrs | 2–4 hrs | 4+ hrs | Almost all day'),
  ...q('[Rural Dev] When preparing muster rolls and wage lists, which steps are digital? / मस्टर रोल और मज़दूरी सूची बनाते समय कौन-से चरण डिजिटल हैं?', 'para'),
  ...q('[Rural Dev] When e-Gram Swaraj or NREGASoft is down, what do you do? / जब ई-ग्राम स्वराज या NREGASoft बंद हो, तो आप क्या करते हैं?', 'radio', 'Wait / retry | Use paper, upload later | Go to block office | Ask a colleague | Skip the task'),

  // ── SECTION 10: Forest Department ──────────────────────────────────────────
  ...section(10, 'Forest Department Tools', 'वन विभाग के उपकरण'),
  ...qCheck('[Forest] Which Forest department digital tools are you aware of? / वन विभाग के कौन-से डिजिटल उपकरणों से आप अवगत हैं?', 'e-Green Watch | AI Alert system | GIS tools | Forest Offence MIS | Nursery MIS | None of the above'),
  ...q('[Forest] Has the AI alert system improved detection of illegal activity? / क्या AI अलर्ट प्रणाली ने अवैध गतिविधि की पहचान में सुधार किया है?', 'scale'),
  ...q('[Forest] How difficult do you find GIS tools? / GIS उपकरण आपको कितने कठिन लगते हैं?', 'scale'),
  ...q('[Forest] Do you have a GPS-enabled device for field verification? / क्या आपके पास क्षेत्र सत्यापन के लिए GPS उपकरण है?', 'radio', 'Dept-issued device | Personal device | Not available'),
  ...q('[Forest] When you receive an AI alert, what do you do step by step? / जब आपको AI अलर्ट मिलता है, तो आप क्या करते हैं?', 'para'),

  // ── SECTION 11: Health Department ──────────────────────────────────────────
  ...section(11, 'Health Department Tools', 'स्वास्थ्य विभाग के उपकरण'),
  ...qCheck('[Health] Which Health department digital tools are you aware of? / स्वास्थ्य विभाग के कौन-से डिजिटल उपकरणों से आप अवगत हैं?', 'ANMOL | HMIS | Nikshay | eVIN | IHIP | ABHA | MPCDSR | None of the above'),
  ...q('[Health] Has ANMOL MP or ABHA improved your ability to track patients? / क्या ANMOL या ABHA ने मरीज़ ट्रैकिंग में सुधार किया है?', 'scale'),
  ...q('[Health] How much does mandatory IHIP disease reporting add to your workload? / अनिवार्य IHIP रोग रिपोर्टिंग आपके कार्यभार में कितना जोड़ती है?', 'scale'),
  ...q('[Health] When registering a pregnant woman for ANC, which steps are on ANMOL? / गर्भवती महिला का ANC पंजीकरण करते समय कौन-से चरण ANMOL पर हैं?', 'para'),
  ...q('[Health] When there is a disease outbreak, how do you report it? / जब कोई रोग प्रकोप होता है, तो आप इसकी रिपोर्ट कैसे करते हैं?', 'para'),
];

console.log("\n==========================================");
console.log(`Done! Created form successfully.`);
console.log(`URL: https://docs.google.com/forms/d/${formId}/edit`);
console.log("==========================================");
