import React, { useState } from "react";

function App() {
  const [records, setRecords] = useState(100);
  const [message, setMessage] = useState("");

  const generateData = async () => {
    try {
      const response = await fetch(`http://localhost:8000/generate?records=${records}`, { method: "POST" });

      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error(error);
      setMessage("Error generating data");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h2>Automated Student Onboarding</h2>

      <input
        type="number"
        value={records}
        onChange={(e) => setRecords(e.target.value)}
        placeholder="Enter number of records"
      />

      <br /><br />

      <button onClick={generateData}>
        Generate CSV & Process
      </button>

      <p>{message}</p>
    </div>
  );
}

export default App;