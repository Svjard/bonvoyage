import React, { PropTypes } from 'react';
import { Link } from 'react-router';

const Navbar = () => {
    return (
      <div id="header" className="header navbar navbar-default navbar-fixed-top">
        <div className="container-fluid">
          <div className="navbar-header">
            <a href="/" className="navbar-brand">
              <img src="/images/logo.png" className="logo" /> Flight Path
            </a>
            <button type="button" className="navbar-toggle">
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>
          </div>
          <ul className="nav navbar-nav">
            <li>
              <Link to="/home" className="nav-link active">Home</Link>
            </li>
            <li>
              <Link to="/company" className="nav-link">My Company</Link>
            </li>
            <li>
              <Link to="/fleet" className="nav-link">My Fleet</Link>
            </li>
            <li>
              <Link to="/map" className="nav-link">Live Map</Link>
            </li>
          </ul>
          <ul className="nav navbar-nav navbar-right">
            <li className="dropdown navbar-user">
              <a href="#" className="dropdown-toggle">
                <span className="image">
                  <img src="images/user_profile.jpg" alt="" />
                </span>
                <span className="hidden-xs">Marc Fisher</span> <b className="caret"></b>
              </a>
              <ul className="dropdown-menu pull-right">
                <li>
                  <a href="/settings">Settings</a>
                </li>
                <li>
                  <a href="/events">Upcoming Events</a>
                </li>
                <li className="divider"></li>
                <li>
                  <a href="/about">About Flight Path...</a>
                </li>
                <li className="divider"></li>
                <li>
                  <a href="/logout">Log Out</a>
                </li>
              </ul>
            </li>
            <li>
              <a href="#" data-click="right-sidebar-toggled">
                <i className="fa fa-align-left"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>
    );
};

export default Navbar;
