const majesticPltPrompts = [
  {
    section_id: "1",
    title: "EXECUTIVE SUMMARY.",
    prompt: "Tell me about EXECUTIVE SUMMARY. in Majestic P.L.T.."
  },
  {
    section_id: "2",
    title: "The MAJESTIC P.L.T Program seeks to leverage these capabilities developing three major areas:",
    prompt: "Tell me about The MAJESTIC P.L.T Program seeks to leverage these capabilities developing three major areas: in Majestic P.L.T.."
  },
  {
    section_id: "3",
    title: "LOGISTICS:",
    prompt: "Tell me about LOGISTICS: in Majestic P.L.T.."
  },
  {
    section_id: "4",
    title: "TECHNOLOGY: the initiative backbone.",
    prompt: "Tell me about TECHNOLOGY: the initiative backbone. in Majestic P.L.T.."
  },
  {
    section_id: "5",
    title: "MAJESTIC P.L.T. is set to revolutionize global commerce.",
    prompt: "Tell me about MAJESTIC P.L.T. is set to revolutionize global commerce. in Majestic P.L.T.."
  },
  {
    section_id: "6",
    title: "CORPORATE OVERVIEW",
    prompt: "Tell me about CORPORATE OVERVIEW in Majestic P.L.T.."
  },
  {
    section_id: "7",
    title: "B&L Worldwide",
    prompt: "Tell me about B&L Worldwide in Majestic P.L.T.."
  },
  {
    section_id: "8",
    title: "ILTT. (International Liquor and Tobacco Trading N.V.)",
    prompt: "Tell me about ILTT. (International Liquor and Tobacco Trading N.V.) in Majestic P.L.T.."
  },
  {
    section_id: "9",
    title: "MAJESTIC P.L.T. CORPORATE STATEMENT.",
    prompt: "Tell me about MAJESTIC P.L.T. CORPORATE STATEMENT. in Majestic P.L.T.."
  },
  {
    section_id: "10",
    title: "Leadership and Team",
    prompt: "How is the Majestic P.L.T. team structured and governed?"
  },
  {
    section_id: "11",
    title: "Board of Directors Overview",
    prompt: "Tell me about Board of Directors Overview in Majestic P.L.T.."
  },
  {
    section_id: "12",
    title: "MARKET, INDUSTRY AND OPPRTUNITY ANALYSIS",
    prompt: "What is the market analysis for Majestic P.L.T.?"
  },
  {
    section_id: "13",
    title: "Logistics Industry in 2025.",
    prompt: "Tell me about Logistics Industry in 2025. in Majestic P.L.T.."
  },
  {
    section_id: "14",
    title: "Key Challenges Facing the Logistics Sector:",
    prompt: "Tell me about Key Challenges Facing the Logistics Sector: in Majestic P.L.T.."
  },
  {
    section_id: "15",
    title: "Technology Integration Gaps",
    prompt: "Tell me about Technology Integration Gaps in Majestic P.L.T.."
  },
  {
    section_id: "16",
    title: "Technology Trends in Production & Logistics.",
    prompt: "Tell me about Technology Trends in Production & Logistics. in Majestic P.L.T.."
  },
  {
    section_id: "17",
    title: "Implementation Challenges",
    prompt: "Tell me about Implementation Challenges in Majestic P.L.T.."
  },
  {
    section_id: "18",
    title: "Tech Leaders and Industry Alignment",
    prompt: "Tell me about Tech Leaders and Industry Alignment in Majestic P.L.T.."
  },
  {
    section_id: "19",
    title: "Majestic Program Opportunities analysis.",
    prompt: "Tell me about Majestic Program Opportunities analysis. in Majestic P.L.T.."
  },
  {
    section_id: "20",
    title: "Strengthening the USA Trade Balance Through Ally-Supported Growth.",
    prompt: "Tell me about Strengthening the USA Trade Balance Through Ally-Supported Growth. in Majestic P.L.T.."
  },
  {
    section_id: "21",
    title: "Supporting traditional Allies and Building Regional Resilience",
    prompt: "Tell me about Supporting traditional Allies and Building Regional Resilience in Majestic P.L.T.."
  },
  {
    section_id: "22",
    title: "MAJESTIC Standard Risk Management Process",
    prompt: "What are the majestic standard risk management process for Majestic P.L.T.?"
  },
  {
    section_id: "23",
    title: "Methodology Overview: Quantifying Risk, Structuring Response",
    prompt: "What are the methodology overview: quantifying risk, structuring response for Majestic P.L.T.?"
  }
];

function getRandomPrompts(promptList, n, excludeIndices = []) {
  const available = promptList
    .map((p, i) => ({ ...p, _idx: i }))
    .filter(p => !excludeIndices.includes(p._idx));
  if (available.length <= n) return available;
  const shuffled = available.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, n);
}

export { majesticPltPrompts as MAJESTIC_PLT_PROMPTS, getRandomPrompts };
