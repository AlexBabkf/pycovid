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
        <optgroup label="- Confirmed Cases">
          <option value="europe-timeline">
            Choropleth Map of Confirmed Cases in Europe{" "}
          </option>
          <option value="world-timeline">
            Choropleth Map of Confirmed Cases in the World
          </option>
          <option value="asia-timeline">
            Choropleth Map of Confirmed Cases in Asia
          </option>
          <option value="scatterplot">Scatterplot of Confirmed Cases</option>
        </optgroup>
        <optgroup label="- Recovered Cases">
          <option value="choro-recovered">
            Choropleth Map of Recovered Cases
          </option>
          <option value="scatter-recovered">
            Scatterplot of Recovered Cases
          </option>
        </optgroup>
      </select>

      <iframe
        // src={`http://127.0.0.1:5000/${selectedVisualization}`} // development
        src={`https://pycovid.vercel.app/${selectedVisualization}`} // deployment
        style={{ width: "100%", height: "500px", border: "none" }}
        title={selectedVisualization}
      ></iframe>
    </>
  );
};

export default HomePage;
