import React, { useEffect, useState } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch(`${API_URL}/`)
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="App">
      <h1 className="brand-name">OnchainX</h1>
      {message && <p className="api-message">{message}</p>}
    </div>
  );
}

export default App;
