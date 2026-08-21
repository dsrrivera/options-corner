import { API_URL } from "../config";
import { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';

import './GreeksPlots.css'

export default function GreeksPlot({ submittedForm }) {
  const [deltaPlotData, setDeltaPlotData] = useState(null)
  const [gammaPlotData, setGammaPlotData] = useState(null)
  const [thetaPlotData, setThetaPlotData] = useState(null)
  const [vegaPlotData, setVegaPlotData] = useState(null)
  const [rhoPlotData, setRhoPlotData] = useState(null)
  const [thetaSurfacePlotData, setThetaSurfacePlotData] = useState(null)

  useEffect(() => {
    // nothing is fetched if the form is not submitted, fix later to be empty plots waiting for data
    if (!submittedForm) return; 
    const fetchGreeksPlots = async () => {
      try{
        const plotsResponse = await fetch(`${API_URL}/api/greeks-plots`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(submittedForm)
        });
        if (!plotsResponse.ok) throw new Error(`Request failed: ${plotsResponse.status}`);

        const result = await plotsResponse.json();

        // result.plot value is a JSON string so we need to parse it, check main.py /greeks-plot endpoint configuration
        setDeltaPlotData(JSON.parse(result.delta_plot)); 
        setGammaPlotData(JSON.parse(result.gamma_plot)); 
        setThetaPlotData(JSON.parse(result.theta_plot)); 
        setVegaPlotData(JSON.parse(result.vega_plot)); 
        setRhoPlotData(JSON.parse(result.rho_plot)); 
        setThetaSurfacePlotData(JSON.parse(result.theta_surface));

      } catch (err) {
        console.err('Error fetching Greeks plots:', err);
      }
  };
    fetchGreeksPlots();
  }, [submittedForm]); // reruns every time submittedForm changes

  return (
    <div> 
      {!submittedForm ? 
      <div className='greeks-plots'>
        <div className='plot'> <Plot data={[]} layout={{title: 'Empty Chart', xaxis: { title: 'X Axis' }, yaxis: { title: 'Y Axis' }}} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={[]} layout={{title: 'Empty Chart', xaxis: { title: 'X Axis' }, yaxis: { title: 'Y Axis' }}} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={[]} layout={{title: 'Empty Chart', xaxis: { title: 'X Axis' }, yaxis: { title: 'Y Axis' }}} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={[]} layout={{title: 'Empty Chart', xaxis: { title: 'X Axis' }, yaxis: { title: 'Y Axis' }}} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={[]} layout={{title: 'Empty Chart', xaxis: { title: 'X Axis' }, yaxis: { title: 'Y Axis' }}} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={[]} layout={{title: 'Empty Chart', xaxis: { title: 'X Axis' }, yaxis: { title: 'Y Axis' }}} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
      </div> : 

      !deltaPlotData ? (<p>Loading plot...</p>) : 
      
      <div className='greeks-plots'>
        <div className='plot'> <Plot data={deltaPlotData.data} layout={deltaPlotData.layout} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={gammaPlotData.data} layout={gammaPlotData.layout} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={thetaPlotData.data} layout={thetaPlotData.layout} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={vegaPlotData.data} layout={vegaPlotData.layout} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={rhoPlotData.data} layout={rhoPlotData.layout} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
        <div className='plot'> <Plot data={thetaSurfacePlotData.data} layout={thetaSurfacePlotData.layout} useResizeHandler={true} style={{ width: '100%', height: '100%' }}/> </div>
      </div>
      }
    </div>
  );
}