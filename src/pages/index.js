import { useEffect, useState } from "react";

const HomePage = () => {
  const [selectedVisualization, setSelectedVisualization] =
    useState("europe-timeline");

  const handleVisualizationChange = (event) => {
    setSelectedVisualization(event.target.value);
  };

  return (
    <>
      <h1>COVID-19 Visualizations</h1>
      <select
        value={selectedVisualization}
        onChange={handleVisualizationChange}
      >
        <option value="europe-timeline">
          Choropleth Map of Confirmed Cases in Europe{" "}
        </option>
        <option value="world-timeline">
          Choropleth Map of Confirmed Cases in the World
        </option>
      </select>
      <iframe
        src={`http://127.0.0.1:5000/${selectedVisualization}`}
        style={{ width: "100%", height: "500px", border: "none" }}
        title={selectedVisualization}
      ></iframe>
    </>
  );
};

export default HomePage;
