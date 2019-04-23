import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Predict from "./components/Predict"

class App extends Component {
  render() {
    return (
      <div className="login">
        <nav class="navbar" role="navigation" aria-label="main navigation">
          <div class="navbar-brand">
            <a class="navbar-item" href="https://bulma.io">
              <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28"/>
            </a>
          </div>

          <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-end">
              <div class="navbar-item">
                <div class="buttons">
                  <a class="button is-primary">
                    <strong>Sign up</strong>
                  </a>
                  <a class="button is-light">
                    Log in
                  </a>
                </div>
              </div>
            </div>
          </div>
        </nav>
        <div>
          <Predict></Predict>
        </div>
      </div>
    );
  }
}

export default App;
