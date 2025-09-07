const positiveWords = new Set([
  "good","great","excellent","amazing","fantastic","wonderful","awesome",
  "brilliant","outstanding","perfect","love","loved","best","superb",
  "incredible","marvelous","terrific","fabulous","magnificent","stunning",
  "beautiful","gorgeous","delightful","charming","impressive","remarkable",
  "exceptional","phenomenal","spectacular","breathtaking","inspiring",
  "enjoyable","entertaining","fun","funny","hilarious","engaging",
  "compelling","captivating","thrilling","exciting","satisfying"
]);

const negativeWords = new Set([
  "bad","terrible","awful","horrible","disgusting","hate","hated",
  "worst","disappointing","boring","stupid","dumb","annoying","irritating",
  "frustrating","confusing","messy","chaotic","disorganized","unclear",
  "poor","weak","pathetic","ridiculous","absurd","nonsense","garbage",
  "trash","waste","pointless","useless","meaningless","empty","shallow",
  "predictable","cliché","overrated","underwhelming","mediocre","average",
  "bland","dull","lifeless","dead","flat","uninspiring","uninteresting"
]);

const strongPositive = new Set([
  "fantastic","amazing","outstanding","brilliant","perfect","excellent","incredible",
  "wonderful","superb","magnificent","spectacular","phenomenal","exceptional",
  "marvelous","terrific","fabulous","stunning","breathtaking","inspiring","masterpiece",
  "flawless","seamless"
]);

const strongNegative = new Set([
  "terrible","awful","horrible","disgusting","worst","disaster","nightmare","torture",
  "painful","unbearable","miserable","depressing","devastating","ruined","destroyed",
  "pathetic","ridiculous","absurd","garbage","trash","waste","pointless","useless"
]);

function classifySentiment(text) {
  const words = text.toLowerCase().split(/\s+/).filter(Boolean);
  let pos = 0, neg = 0;

  for (const w of words) {
    if (strongPositive.has(w)) pos += 3;
    else if (strongNegative.has(w)) neg += 3;
    else if (positiveWords.has(w)) pos += 1;
    else if (negativeWords.has(w)) neg += 1;
  }

  const total = pos + neg;
  if (total === 0) {
    return { prediction: "Neutral", confidence: 0.5, pos_score: pos, neg_score: neg };
  }

  let confidence = 0.8;
  if (words.some(w => strongPositive.has(w) || strongNegative.has(w))) confidence += 0.1;
  if ((pos > 0 && neg === 0) || (neg > 0 && pos === 0)) confidence += 0.05;
  if (total >= 3) confidence += 0.05;
  confidence = Math.min(confidence, 0.95);

  let prediction = "Neutral";
  if (pos > neg) prediction = "Positive";
  else if (neg > pos) prediction = "Negative";
  else confidence = 0.5;

  return { prediction, confidence, pos_score: pos, neg_score: neg };
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === "/classify" && request.method === "POST") {
      try {
        const body = await request.json();
        const text = (body?.text || "").trim();
        if (!text) {
          return json({ error: "No text provided" }, 400);
        }
        return json(classifySentiment(text));
      } catch (e) {
        return json({ error: String(e) }, 500);
      }
    }

    // Serve static UI from /public
    return env.ASSETS.fetch(request);
  }
};

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json" }
  });
}
