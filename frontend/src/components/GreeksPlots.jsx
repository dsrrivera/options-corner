import { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';

import './GreeksPlots.css'

export default function GreeksPlot({ submittedForm }) {
  const [plotsData, setPlotsData] = useState(null)

  useEffect(() => {
    // nothing is fetched if the form is not submitted, fix later to be empty plots waiting for data
    if (!submittedForm) return; 
    const fetchGreeksPlots = async () => {
      try{
        const plotsResponse = await fetch('http://localhost:8000/api/greeks-plots', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(submittedForm)
        });
        if (!plotsResponse.ok) throw new Error(`Request failed: ${plotsResponse.status}`);

        const result = await plotsResponse.json();

        setPlotsData(JSON.parse(result.delta_plot)); // delta_plot's value is a JSON string so we need to parse it, check main.py /greeks-plot endpoint configuration
        console.log("PlotsDelta:", plotsData);  

      } catch (err) {
        console.err('Error fetching Greeks plots:', err);
      }
  };
    fetchGreeksPlots();
  }, [submittedForm]); // reruns every time submittedForm changes

  return (
    // this will change, just a placeholder return for now...
    <div> {!submittedForm ? (<p>Waiting for options data...</p>) : !plotsData ? (<p>Loading plot...</p>) : (<Plot data={plotsData.data} layout={plotsData.layout}/>)}
    </div>
  );
}