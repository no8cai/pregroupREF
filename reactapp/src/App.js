import { csrfFetch } from "./store/csrf";
import { useDispatch } from "react-redux";
import React, { useState, useEffect } from 'react';


function App() {

  const dispatch = useDispatch();
  const [currentData, setCurrentData] = useState("");

  useEffect(() => {
    fetch('/test').then(res => res.json()).then(data=>setCurrentData(data.hello))
  }, [currentData]);

  return (
    <h1>{currentData}</h1>
  );
}

export default App;
