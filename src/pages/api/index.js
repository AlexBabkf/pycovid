export default async function handler(req, res) {
  try {
    const baseUrl =
      process.env.NODE_ENV === "development"
        ? "http://127.0.0.1:5000"
        : "https://pycovid.vercel.app";
    console.log(req);
    const selectedVisualization = req.url;

    const response = await fetch(`${baseUrl}/${selectedVisualization}`);
    const visualizationData = await response.json();

    res.status(200).json(visualizationData);
  } catch (error) {
    console.error("Error fetching visualization data:", error);
    res.status(500).json({ error: "Error fetching visualization data" });
  }
}
