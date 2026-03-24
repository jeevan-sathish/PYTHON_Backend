import React, { useState } from "react";

const App = () => {
  const [array, setarray] = useState([]);
  const [dict, setDict] = useState([]);
  const [detail, setDetail] = useState({});
  const [msg, setMsg] = useState("");
  const data = { name: "raju", age: 35 };
  async function fetchData() {
    try {
      const res = await fetch("http://127.0.0.1:5000/data/2", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      const result = await res.json();

      setarray(result.array);
      setDict(result.data);
      setDetail(result.details);
      setMsg(result.message);
    } catch (err) {
      console.log("error:", err);
    }
  }
  return (
    <div>
      <button onClick={fetchData}>get request</button>
      <div>
        {array.map((ele) => (
          <p>{ele}</p>
        ))}
      </div>

      <div>
        {dict.map((ele) => (
          <div>
            <p>{ele.name}</p>
            <p>{ele.age}</p>
          </div>
        ))}
      </div>

      <div>
        <p>{detail.name}</p>
        <p>{detail.name}</p>
        <p>{msg}</p>
      </div>
    </div>
  );
};

export default App;
