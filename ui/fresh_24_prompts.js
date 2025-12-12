export { FRESH_24_PROMPTS, getRandomPrompts };
// This file will be loaded by the UI to provide prompt suggestions for Fresh 24
// Copy this file to the ui/ folder if you want to serve it statically

const FRESH_24_PROMPTS = [
  {"section_id": "1", "title": "FRESH-24 project. Strategic Production & Trade Engine of the MAJESTIC Platform", "prompt": "Tell me about FRESH-24 project. Strategic Production & Trade Engine of the MAJESTIC Platform in Fresh 24."},
  {"section_id": "2", "title": "Project summary:", "prompt": "Tell me about Project summary: in Fresh 24."},
  {"section_id": "3", "title": "Project problem statement and objectives.", "prompt": "What problem will Fresh 24 solve? What are its objectives?"},
  {"section_id": "4", "title": "Fresh-24 Main Objective.", "prompt": "What problem will Fresh 24 solve? What are its objectives?"},
  {"section_id": "5", "title": "FRESH-24 market opportunity.", "prompt": "What is the market analysis for Fresh 24?"},
  {"section_id": "6", "title": "Product & Service Offering", "prompt": "Tell me about Product & Service Offering in Fresh 24."},
  {"section_id": "7", "title": "Production & Infrastructure Model", "prompt": "Tell me about Production & Infrastructure Model in Fresh 24."},
  {"section_id": "8", "title": "FILPROC: Fully Integrated Production and Logistic Corridors", "prompt": "Tell me about FILPROC: Fully Integrated Production and Logistic Corridors in Fresh 24."},
  {"section_id": "9", "title": "Consolidation and distribution centers.", "prompt": "Tell me about Consolidation and distribution centers. in Fresh 24."},
  {"section_id": "10", "title": "Operations & Logistics", "prompt": "Tell me about Operations & Logistics in Fresh 24."},
  {"section_id": "11", "title": "Financial Projections", "prompt": "What are the financial risks for Fresh 24?"},
  {"section_id": "12", "title": "Identified Revenue Streams:", "prompt": "Tell me about Identified Revenue Streams: in Fresh 24."},
  {"section_id": "13", "title": "Cost structure", "prompt": "Tell me about Cost structure in Fresh 24."},
  {"section_id": "14", "title": "Tax strategy", "prompt": "Tell me about Tax strategy in Fresh 24."},
  {"section_id": "15", "title": "Financial Strategy: Structured Profit Allocation for Sustainable Growth", "prompt": "What are the financial risks for Fresh 24?"},
  {"section_id": "16", "title": "TEAM AND GOVERNANCE", "prompt": "How is the Fresh 24 team structured and governed?"},
  {"section_id": "17", "title": "Governance: Modular Autonomy, Unified Strategy", "prompt": "How is the Fresh 24 team structured and governed?"},
  {"section_id": "18", "title": "RISK MANAGEMENT STRATEGY", "prompt": "What are the risk management strategy for Fresh 24?"},
  {"section_id": "19", "title": "MARKET RISK ANALYS", "prompt": "What are the market risk analys for Fresh 24?"},
  {"section_id": "20", "title": "COMPETITORS RISK ANALYSIS", "prompt": "What are the competitors risk analysis for Fresh 24?"},
  {"section_id": "21", "title": "OPERATIONAL / TECHNOLOGICAL RISKS", "prompt": "Tell me about OPERATIONAL / TECHNOLOGICAL RISKS in Fresh 24."},
  {"section_id": "22", "title": "FINANCIAL RISKS ANALYSIS", "prompt": "What are the financial risks for Fresh 24?"},
  {"section_id": "23", "title": "TEAM / MANAGEMENT RISK ANALYSIS", "prompt": "How is the Fresh 24 team structured and governed?"},
  {"section_id": "24", "title": "REGULATORY AND POLITICAL RISK ANALYSIS", "prompt": "Tell me about REGULATORY AND POLITICAL RISK ANALYSIS in Fresh 24."}
];

// Utility to get N random prompts from the list, without repeats
function getRandomPrompts(promptList, n, excludeIndices = []) {
  const available = promptList
    .map((p, i) => ({ ...p, _idx: i }))
    .filter(p => !excludeIndices.includes(p._idx));
  if (available.length <= n) return available;
  const shuffled = available.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, n);
}

export { FRESH_24_PROMPTS, getRandomPrompts };
