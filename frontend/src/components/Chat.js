import React, { useState } from "react";

const Chat = () => {
  const [messages, setMessages] = useState([
    { text: "Welcome! How can I assist you?", type: "bot" },
  ]);

  return (
    <div className="chat">
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.type}`}>
          <p>{msg.text}</p>
        </div>
      ))}
    </div>
  );
};

export default Chat;
