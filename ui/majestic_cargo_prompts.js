// This file provides prompt suggestions for Majestic Air Cargo.

const MAJESTIC_CARGO_PROMPTS = [
  {"section_id": "1", "title": "MAJESTIC AIR CARGO low cost, perishable specialized, with zero intermediation.", "prompt": "Tell me about MAJESTIC AIR CARGO low cost, perishable specialized, with zero intermediation."},
  {"section_id": "2", "title": "Majestic Air Cargo is built around a clear set of objectives: perishable specialization, low-cost operations, minimal intermediation, and democratized access to air freight. The platform is designed to bring general cargo accessibility to the level of passenger flights, offering predictable schedules, transparent pricing, and corridor-level service guarantees. While FRESH-24 remains the anchor client, Majestic is open to third-party shippers, SMEs, and regional producers, creating a scalable logistics backbone for the broader hemispheric economy. The shared technology stack ensures that external customers benefit from the same predictive routing, compliance automation, and ESG tracking that powers MAJESTIC’s internal operations.", "prompt": "What problem will Majestic Air Cargo solve? What are its objectives?"},
  {"section_id": "3", "title": "The management team behind Majestic Air Cargo brings decades of aviation experience, spanning commercial operations, cargo optimization, regulatory compliance, and fleet management. Their expertise ensures that the airline is not only operationally sound but strategically aligned with MAJESTIC’s modular governance and corridor activation logic. From aircraft selection to route planning and customs integration, every decision reflects a deep understanding of both aviation mechanics and platform economics.", "prompt": "How is the Majestic Air Cargo team structured and governed?"},
  {"section_id": "4", "title": "Looking ahead, Majestic Air Cargo will explore intermodal integration opportunities, linking air corridors with rail, maritime, and last-mile logistics to create seamless, multi-layered trade flows. This next phase will also include ESG-linked fleet upgrades, AI-driven load optimization, and corridor-specific carbon tracking, ensuring that growth is not only scalable, but sustainable. The shared data infrastructure between Majestic and FRESH-24 will continue to evolve, enabling predictive risk modeling, automated compliance workflows, and real-time performance dashboards across every corridor, aircraft, and shipment.", "prompt": "What are the future integration opportunities for Majestic Air Cargo?"},
  {"section_id": "5", "title": "INDUSTRY OVERVIEW", "prompt": "Tell me about the industry overview for Majestic Air Cargo."},
  {"section_id": "6", "title": "MARKET ANALYSIS", "prompt": "What is the market analysis for Majestic Air Cargo?"},
  {"section_id": "7", "title": "United States – Target Market Analysis", "prompt": "What is the market analysis for Majestic Air Cargo?"},
  {"section_id": "8", "title": "Colombia – Target Market Analysis", "prompt": "What is the market analysis for Majestic Air Cargo?"},
  {"section_id": "9", "title": "Latin America – Target Market Overview (2025)", "prompt": "What is the market analysis for Majestic Air Cargo?"},
  {"section_id": "10", "title": "Cargo & O&D Demand", "prompt": "Tell me about Cargo & O&D Demand for Majestic Air Cargo."},
  {"section_id": "11", "title": "COMPETITIVE ANALYSIS", "prompt": "Tell me about the competitive analysis for Majestic Air Cargo."},
  {"section_id": "12", "title": "Incumbent Airlines in the Latin American Marketplace (2025)", "prompt": "What is the market analysis for Majestic Air Cargo?"},
  {"section_id": "13", "title": "Barriers to Market Entry in Latin American Air Cargo (2025)", "prompt": "What is the market analysis for Majestic Air Cargo?"},
  {"section_id": "14", "title": "OPPORTUNITY", "prompt": "Tell me about the opportunity for Majestic Air Cargo."},
  {"section_id": "15", "title": "SERVICE OFFERING", "prompt": "Tell me about the service offering for Majestic Air Cargo."},
  {"section_id": "16", "title": "COMPANY CORPORATE STATEMENT", "prompt": "Tell me about the company corporate statement for Majestic Air Cargo."},
  {"section_id": "17", "title": "Objectives", "prompt": "What problem will Majestic Air Cargo solve? What are its objectives?"},
  {"section_id": "18", "title": "OPERATIONAL SCOPE OF THE PROJECT", "prompt": "Tell me about the operational scope of the project for Majestic Air Cargo."},
  {"section_id": "19", "title": "Operational description", "prompt": "Tell me about the operational description for Majestic Air Cargo."},
  {"section_id": "20", "title": "PRODUCT OFFERING", "prompt": "Tell me about the product offering for Majestic Air Cargo."},
  {"section_id": "21", "title": "AIRCRAFT SELECTION", "prompt": "Tell me about the aircraft selection for Majestic Air Cargo."},
  {"section_id": "22", "title": "OPERATIONS PLAN", "prompt": "Tell me about the operations plan for Majestic Air Cargo."},
  {"section_id": "23", "title": "ADMINISTRATIVE, CUSTOMER SERVICE, AND LABOR FRAMEWORK", "prompt": "Tell me about the administrative, customer service, and labor framework for Majestic Air Cargo."},
  {"section_id": "24", "title": "FINANCIAL ANALYSIS", "prompt": "What are the financial risks for Majestic Air Cargo?"},
  {"section_id": "25", "title": "Cost Structure", "prompt": "Tell me about the cost structure for Majestic Air Cargo."},
  {"section_id": "26", "title": "RISK ANALYSIS", "prompt": "What is the risk analysis for Majestic Air Cargo?"},
  {"section_id": "27", "title": "Market Risk Analysis:", "prompt": "What is the market risk analysis for Majestic Air Cargo?"},
  {"section_id": "28", "title": "Competitors risk Analysis", "prompt": "What is the competitors risk analysis for Majestic Air Cargo?"},
  {"section_id": "29", "title": "Operational / Technological Risk analysis", "prompt": "What is the operational / technological risk analysis for Majestic Air Cargo?"},
  {"section_id": "30", "title": "Financial Risk Analysis", "prompt": "What is the financial risk analysis for Majestic Air Cargo?"},
  {"section_id": "31", "title": "Team / Management risk analysis", "prompt": "What is the team / management risk analysis for Majestic Air Cargo?"},
  {"section_id": "32", "title": "Regulatory / Political risk Management", "prompt": "What is the regulatory / political risk management for Majestic Air Cargo?"},
  {"section_id": "33", "title": "Team and Governance Team", "prompt": "How is the Majestic Air Cargo team structured and governed?"},
  {"section_id": "34", "title": "IMPLEMENTATION SCHEDULE", "prompt": "Tell me about the implementation schedule for Majestic Air Cargo."},
  {"section_id": "35", "title": "CAPITALIZATION PLAN", "prompt": "Tell me about the capitalization plan for Majestic Air Cargo."}
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

export { MAJESTIC_CARGO_PROMPTS, getRandomPrompts };
