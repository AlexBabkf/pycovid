export default async function handler(req, res) {
  try {
    const response = await fetch("http://127.0.0.1:5000/");
    const visualizationData = await response.json();
    res.status(200).json(visualizationData);
  } catch (error) {
    console.error("Error fetching visualization data:", error);
    res.status(500).json({ error: "Error fetching visualization data" });
  }
}
