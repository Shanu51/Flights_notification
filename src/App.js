import './App.css';
// import { Route, Routes } from "react-router-dom"
import './App.css';
import { useState } from "react"
// import First from "./component/first/First.js"
function App() {
  const [flightNumber, setflightNumber] = useState("")
  const [date, setdate] = useState("")
  const handleSubmit = () => {
    if(flightNumber == "" && date==""){
      alert("Please Enter Details")
    }
    else if(flightNumber == ""){
      alert("Please Enter Flight Numer")
    }
   else if(date==""){
      alert("Please Enter Departure Date")
    }

  }
  return (
    <div className="App">
      <input className='inp' placeholder='Enter Flight Number' type='number' onChange={(e) => setflightNumber(e.target.value)} />
      <input type='date' className='inp' onChange={(e) => setdate(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default App;

// import { Route, Routes } from "react-router-dom"
// import './App.css';
// import First from "./component/first/First.js"

// function App() {
//   return (
//     <div className="App">
//       <Routes>
//         <Route path='/main' element={First} />
//       </Routes>

//     </div>
//   );
// }

// export default App;
