import { createReducer } from '../utils';
import {
  LOGIN_USER_REQUEST,
  LOGIN_USER_SUCCESS,
  LOGIN_USER_FAILURE,
  LOGOUT_USER
} from '../constants';
import { pushState } from 'redux-router';

const initialState = {
  account: null,
  isAuthenticated: false,
  isAuthenticating: false,
  statusText: null
};

export default createReducer(initialState, {
  [LOGIN_USER_REQUEST]: (state, payload) => {
    return Object.assign({}, state, {
      'isAuthenticating': true,
      'statusText': null
    });
  },
  [LOGIN_USER_SUCCESS]: (state, payload) => {
    console.log('LOGIN_USER_SUCCESS');
    return Object.assign({}, state, {
      'isAuthenticating': false,
      'isAuthenticated': true,
      'account': payload.account,
      'statusText': 'You have been successfully logged in.'
    });
  },
  [LOGIN_USER_FAILURE]: (state, payload) => {
    return Object.assign({}, state, {
      'isAuthenticating': false,
      'isAuthenticated': false,
      'account': null,
      'statusText': `Authentication Error: ${payload.status} ${payload.statusText}`
    });
  },
  [LOGOUT_USER]: (state, payload) => {
    return Object.assign({}, state, {
      'isAuthenticated': false,
      'account': null,
      'statusText': 'You have been successfully logged out.'
    });
  }
});