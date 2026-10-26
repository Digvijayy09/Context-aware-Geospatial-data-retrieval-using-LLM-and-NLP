import React from "react";
import Header from "./components/Header";
import Chat from "./components/Chat";
import Map from "./components/Map";
import InputContainer from "./components/InputContainer";

const App = () => {
  const [locations, setLocations] = React.useState([]);

  return (
    <div className="app">
      <Header />
      <div className="content">
        <Chat />
        <Map locations={locations} />
      </div>
      <InputContainer setLocations={setLocations} />
    </div>
  );
};

export default App;
