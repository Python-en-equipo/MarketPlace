import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import "./fonts.css"
import App from "./App";
import { Provider } from 'react-redux'
import store from "./store";
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <BrowserRouter>
    <Provider store={store}>
      <App className="bg-[#E5E5E5]" />
    </Provider>
    </BrowserRouter>
  </>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
