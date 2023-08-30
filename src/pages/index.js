import { useEffect, useState } from "react";

const HomePage = () => {
  // const [visualizationData, setVisualizationData] = useState(null);

  // useEffect(() => {
  //   fetch("/api/get_visualization_data")
  //     .then((response) => response.json())
  //     .then((data) => setVisualizationData(data))
  //     .catch((error) => console.error("Error fetching data:", error));
  // }, []);

  return (
    <>
      <h1>Covid </h1>
      <iframe
        src="http://127.0.0.1:5000/"
        style={{ width: "100%", height: "500px", border: "none" }}
        title="COVID-19 Visualization"
      ></iframe>
    </>
    // <div>
    //   <h1>COVID-19 Visualization</h1>
    //   {visualizationData && (
    //     <div dangerouslySetInnerHTML={{ __html: visualizationData }} />
    //   )}
    // </div>
  );
};

export default HomePage;
