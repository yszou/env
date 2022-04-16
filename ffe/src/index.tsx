import React from "react";
import ReactDOM from "react-dom";
import { Index } from "./Index";

if (document.getElementById("app")) {
  ReactDOM.render(<Index />, document.getElementById("app"));
}
